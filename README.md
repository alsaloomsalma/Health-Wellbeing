# Health-Wellbeing
# From Lifestyle to Life Satisfaction: Predictive Modeling of Wellbeing

## Project Overview
This project explores how lifestyle factors influence **Work-Life Balance (WLB)** and overall wellbeing. Using data-driven techniques, the project identifies patterns in lifestyle habits and their relationship to wellbeing, and demonstrates clustering and dimensionality reduction for segmentation analysis.

---

## Problem Statement
Maintaining a healthy work-life balance is a challenge for many, impacting mental health and productivity. Few tools proactively guide individuals in improving wellbeing based on their habits.

**Who is affected?**
- Employees at risk of burnout
- Employers concerned with retention and engagement
- Wellness coaches and HR professionals
- Individuals striving for better lifestyle balance

**Why it matters?**
- Helps individuals understand how habits influence wellbeing
- Enables organizations to identify at-risk groups
- Supports data-driven wellness strategies

---

## Dataset
- **Source:** Kaggle – Wellbeing and Lifestyle Dataset
- **Size:** Includes multiple lifestyle factors such as:
  - Daily exercise
  - Sleep hours
  - Stress levels
  - Screen time
- **Target:** Wellbeing indicators (e.g., Work-Life Balance score)

---

## Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - Data Handling: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - ML & Analysis: `scikit-learn` (PCA, clustering)
  - Tabular display: `tabulate`

---

## Key Steps
1. **Data Cleaning**
   - Dropped irrelevant columns
   - Handled missing values and duplicates
2. **Exploratory Data Analysis**
   - Distribution and box plots by group
   - Correlation heatmap of lifestyle variables
3. **Dimensionality Reduction**
   - Applied PCA to reduce high-dimensional data
4. **Clustering**
   - KMeans and DBSCAN for lifestyle-based segmentation
5. **Visualization**
   - t-SNE for cluster visualization

---

## Visual Insights
- Correlation heatmap of lifestyle factors vs WLB
- PCA scatter plots
- t-SNE plots for cluster separation

---

## Usage
Run the Jupyter Notebook:
```bash
jupyter notebook "Project 4 - Capstone.ipynb"
