# Rare Earth Elements (REE) Production & Market Concentration Analysis

## 1. Project Goal & Questions
### Goal
To analyze global REE production trends, quantify market concentration risk, and forecast future supply to inform strategic sourcing decisions.

### Key Questions
* How concentrated is the global REE market? (Quantified by HHI)
* What is the projected global REE production trend over the next few. years?
* Which nations dominate the supply chain?

---

## 2. Data Source
* **File:** `mcs2024-raree_world-1.csv`
* **Source:** [USGS]
* **Time Period:** 2022–2023

---

## 3. Methodology & Tools
* **Environment:** Jupyter Notebook
* **Tools:** `pandas` for data manipulation, `plotly` for interactive visualization.
* **Advanced Analysis:** Calculation of the **Herfindahl-Hirshman Index (HHI)** for market concentration.
* **Modeling:** Predictive analysis using  `statsmodels`.

---

## 4. Key Findings & Results: Rare Earth Element (REE) Mine Production (2022–2023)

The analysis of 2022–2023 global Rare Earth Element (REE) mine production reveals a market structure characterized by **extreme supply concentration**, which poses a significant strategic sourcing risk.

---

## 5. Regression Analysis Key Findings

This section summarizes the primary insights from the Ordinary Least Squares (OLS) conducted in the notebook to explore the relationship
between production and reserves.

* **Highly Significant Predictor**: The independent variable ('prod_t_est_2023') is highly statistically significant.
* **Postive Correlation**: The corfficient of **254.6** indicates a strong positive relationship. An increase in
  production directly correlates with a substantial increase in reserves

### concerns
* **Numerical Instability**: The high condition number suggests the predictor variables are hoghly correlated with each other.

---

### Market Concentration (HHI)

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Global HHI** | **4,909** | Highly Concentrated Market (>2,500) |

* The Herfindahl-Hirshman Index (HHI) for the global REE market is **4,909** (based on 2023 estimated production).
* **China's dominance** is the primary driver of this concentration, with its squared market share contributing approximately **94%** of the total HHI value.
* > **Implication:** This ultra-high HHI highlights that the global REE supply chain is **highly vulnerable** to geopolitical risk, trade disputes, or production disruptions in a single country.

---

### Nations Dominating the Supply Chain

* **China** remains the undisputed global leader, accounting for the vast majority of mine production (approx. **240,000 metric tons** in 2023).
* **Secondary Producers (2023):**
    * United States: 43,000 mt
    * Burma: 38,000 mt
    * *Note: Their combined output is only a fraction of China's.*
* The **top five producers** (China, United States, Burma, Australia, and Thailand) collectively control the overwhelming majority of the global REE supply.

---

###  Production Trend (2022–2023)

* **Global Growth:** The overall global production trend from 2022 to 2023 was **positive**, driven by increases in a few key nations.
* **Notable Increases:**
    * **Burma** saw the largest relative growth, with production surging by approximately **217%** (from 12,000 mt to 38,000 mt).
    * **China** also increased its output by about **14.3%** in 2023.
    * The **United States** had a modest increase of about **2.4%**.
---

## 5. How to Run the Analysis (Reproducibility)
1.  Ensure you have Python 3.9+ installed.
2.  Install dependencies: `pip install pandas plotly statsmodels jupyter`.
3.  Place `mcs2024-raree_world-1.csv` in the root directory.
4.  Open the main analysis file: `jupyter notebook rare_earth_analysis.ipynb`.

