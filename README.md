# IBM Applied Data Science Capstone — SpaceX Falcon 9 First-Stage Landing Prediction

**Author:** Hala Hagag
**Course:** [IBM Applied Data Science Capstone (DS0321EN)](https://www.coursera.org/learn/applied-data-science-capstone)

This repository contains the complete capstone project for the IBM Data Science Professional Certificate. The goal of the project is to predict whether the **first stage** of a SpaceX Falcon 9 rocket will land successfully — and, by extension, estimate the real cost of a launch. A reused booster brings the per-launch price from roughly $165M down to about $62M, so the landing outcome is the single biggest driver of cost.

## Repository structure

```
.
├── data/                                  -- prepared datasets
│   ├── dataset_part_1.csv                 -- raw collected data
│   ├── dataset_part_2.csv                 -- wrangled, with binary Class label
│   ├── dataset_part_3.csv                 -- one-hot encoded, ML-ready
│   ├── Spacex.csv                         -- table loaded into SQLite for EDA
│   └── spacex_launch_dash.csv             -- subset used by the Plotly Dash app
├── notebooks/
│   ├── 1_data_collection_api.ipynb        -- SpaceX REST API + Wikipedia scraping
│   ├── 2_data_wrangling.ipynb             -- cleaning + building Class label
│   ├── 3_eda_sql.ipynb                    -- 10 SQL queries on SPACEXTBL
│   ├── 4_eda_visualization.ipynb          -- Matplotlib / Seaborn EDA
│   ├── 5_folium_map.ipynb                 -- interactive Folium map
│   ├── 6_dash_app.py                      -- Plotly Dash dashboard
│   └── 7_ml_prediction.ipynb              -- LogReg / SVM / Tree / KNN with GridSearchCV
├── images/                                -- charts and map exports used in the slides
├── Data_Science_Capstone_Project_Report.pptx
└── Data_Science_Capstone_Project_Report.pdf
```

## Project pipeline

1. **Data Collection** — pulled launch records from the SpaceX REST API (`api.spacexdata.com/v4/launches/past`) and from the Falcon 9 Wikipedia page via BeautifulSoup web scraping.
2. **Data Wrangling** — filtered to Falcon 9 only, imputed missing payload masses with the column mean, and engineered a binary `Class` column from the `Outcome` field (1 = first stage landed, 0 = did not).
3. **EDA with SQL** — loaded the cleaned table into an in-memory SQLite database and answered the standard 10 questions used in the IBM lab (unique sites, total NASA payload, first ground-pad landing, ranked landing outcomes, etc.).
4. **EDA with Visualization** — Matplotlib / Seaborn scatter and bar charts for flight number vs site, payload vs site, orbit success rates, and the yearly trend.
5. **Interactive Visual Analytics**
   - **Folium** map with marker clusters (green = success, red = failure) and proximity circles to the nearest coastline, railway, highway and city.
   - **Plotly Dash** dashboard with a launch-site dropdown, a payload range slider, a success pie chart and a scatter plot coloured by booster version.
6. **Predictive Analysis** — standardised features, 80 / 20 train-test split, and `GridSearchCV` (cv = 10) on Logistic Regression, SVM, Decision Tree and K-Nearest Neighbors.

## Headline results

| Metric                                | Value                                       |
| ------------------------------------- | ------------------------------------------- |
| Launches analysed                     | 90                                          |
| Overall first-stage landing rate      | ~67%                                        |
| Mission outcomes                      | 99 Success / 1 Success (unclear) / 1 Failure|
| Best launch site (success rate)       | KSC LC-39A — ~77%                           |
| Best classifier (test accuracy)       | **Decision Tree — 94.4%** (max_depth=4)     |
| Yearly landing-success rate           | 40% (2010) → 86% (2020)                     |

## How to reproduce

```bash
pip install -r requirements.txt          # pandas, scikit-learn, folium, dash, matplotlib, seaborn
jupyter notebook notebooks/              # run the .ipynb files in order
python notebooks/6_dash_app.py            # open http://127.0.0.1:8050 for the dashboard
```

## Final deliverable

`Data_Science_Capstone_Project_Report.pdf` — the slide deck submitted for grading. It covers every required component (Executive Summary, Introduction, Methodology, EDA visual results, EDA SQL results, Folium map results, Plotly Dash results, Predictive Analysis results, Conclusion, Innovative Insights, Appendix and References).

## Acknowledgements

- IBM Skills Network — course materials and the public Falcon 9 dataset hosted on IBM Cloud Object Storage.
- SpaceX — the public REST API at `api.spacexdata.com`.
- Wikipedia contributors — the *List of Falcon 9 and Falcon Heavy launches* page used for web scraping.
