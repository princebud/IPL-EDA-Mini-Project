# IPL Exploratory Data Analysis (EDA) Mini Project

**Coursework project:** Explore an IPL-inspired dataset using Python, Pandas, and Matplotlib.

> **Dataset notice:** The included dataset is synthetically generated for this coursework. It is not official IPL match data and the KPIs/insights must not be described as real IPL statistics.

## Project requirements covered
- Dataset loading and exploration
- Data type checks and corrections
- Missing value handling
- Duplicate detection and removal
- Outlier detection and capping using the IQR method
- Clean dataset export
- 8+ KPIs and visualizations
- Insights and conclusion

## Files
- `data/ipl_matches_original.csv` — generated raw dataset with intentional data-quality issues
- `data/ipl_matches_cleaned.csv` — cleaned dataset
- `notebooks/IPL_EDA_Project.ipynb` — full walkthrough notebook
- `clean_data.py` — reproducible cleaning script
- `outputs/` — charts created when notebook is run

## How to run (Google Colab)
1. Download or clone the repository.
2. Open `notebooks/IPL_EDA_Project.ipynb` in Google Colab or Jupyter.
3. If using Colab, upload the repository folder or open notebook from GitHub.
4. Run **Runtime → Run all** (or execute cells top to bottom).

## How to run locally
```bash
python -m pip install -r requirements.txt
cd notebooks
jupyter notebook IPL_EDA_Project.ipynb
```

## KPIs included
1. Total matches analyzed
2. Average first-innings score
3. Average second-innings score
4. Toss winner also won match percentage
5. Most winning team in generated sample
6. Chasing wins and percentage
7. Defending wins and percentage
8. Average combined runs per match
9. Average winning margin

## Limitations
Because records are simulated, all charts and findings describe only this sample. They cannot be used to infer actual IPL history or team performance.
