# IPL EDA project dataset utility
# This data is synthetic and intended only for coursework practice.
import pandas as pd
from pathlib import Path

source = Path('data/ipl_matches_original.csv')
df = pd.read_csv(source)
print('Raw dataset:', df.shape)
print('Missing values:\n', df.isna().sum())
print('Duplicate match IDs:', df.duplicated(subset='match_id').sum())
clean = df.drop_duplicates(subset='match_id').copy()
for col in clean.columns:
    if clean[col].isna().any():
        clean[col] = clean[col].fillna(clean[col].median() if pd.api.types.is_numeric_dtype(clean[col]) else clean[col].mode()[0])
for col in ['first_innings_runs','second_innings_runs','win_margin']:
    q1, q3 = clean[col].quantile([.25,.75]); iqr=q3-q1
    clean[col] = clean[col].clip(max(0,q1-1.5*iqr), q3+1.5*iqr).round().astype(int)
clean.to_csv('data/ipl_matches_cleaned.csv', index=False)
print('Saved cleaned dataset:', clean.shape)
