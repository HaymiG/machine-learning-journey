# 📊 Cardio Performance Analysis - Statistical Study

A comprehensive statistical analysis of cardio equipment usage data using Python, exploring customer demographics, product preferences, and performance patterns through descriptive statistics, categorical analysis, and regression modeling.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

<!-- --- -->

<!-- ## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis Tasks](#analysis-tasks)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact) -->

---

## 🎯 Overview

This project performs an in-depth statistical analysis of cardio equipment usage data to uncover insights about:
- Customer wealth distribution and income patterns
- Equipment usage patterns and miles logged
- Demographic characteristics (age, gender, education)
- Correlations between variables
- Elite athlete customer profiles

The analysis is presented in a Jupyter notebook format, making it easy to follow, reproduce, and adapt for similar datasets.

---

## ✨ Features

- **Descriptive Statistics**: Mean, median, mode, and distribution analysis
- **Visual Analytics**: Histograms, boxplots, scatter plots, and heatmaps
- **Outlier Detection**: Identification of anomalies in customer behavior
- **Correlation Analysis**: Discovering relationships between variables
- **Regression Modeling**: Predictive analysis with linear regression
- **Conditional Probability**: Gender-based product preference analysis
- **Customer Segmentation**: Elite athlete profile identification
- **Professional Visualizations**: All plots include titles, labels, and legends

---

## 📊 Dataset

The dataset contains customer information with the following features:

| Column | Description | Type |
|--------|-------------|------|
| `Income` | Customer annual income | Numerical |
| `Miles` | Miles logged on equipment | Numerical |
| `Age` | Customer age in years | Numerical |
| `Education` | Years of education | Numerical |
| `Usage` | Equipment usage frequency (times/week) | Numerical |
| `Fitness` | Fitness score (1-5 scale) | Numerical |
| `Product` | Product type (TM195, TM498, TM798) | Categorical |
| `Gender` | Customer gender | Categorical |


---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/HaymiG/machine-learning-journey
   cd customer-data-analysis
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

---


## 📈 Analysis Tasks

### Task 1: The Wealth Gap 💰
- Calculate mean, median, and mode for income
- Analyze data skewness
- Interpret wealth distribution patterns

### Task 2: The 5-Number Summary 📊
- Display min, Q1, median, Q3, and max for miles
- Create boxplot visualization
- Identify and analyze outliers

### Task 3: Age Distribution 👥
- Generate histogram with 10 bins
- Identify median age bracket
- Analyze customer age demographics

### Task 4: Product Popularity 🏆
- Create count plot for product sales
- Compare product performance
- Identify best-selling products

### Task 5: Income vs Product 💵
- Compare income across product types
- Identify high-income segment products
- Analyze pricing strategy implications

### Task 6: Gender Probability 🎲
- Calculate P(Female | TM195)
- Analyze gender-based product preferences
- Derive marketing insights

### Task 7: Correlation Heatmap 🔥
- Generate correlation matrix
- Identify strongest correlations with miles
- Discover variable relationships

### Task 8: Scatter Plot & Regression 📈
- Plot Usage vs Miles relationship
- Fit linear regression model
- Calculate R² score and interpret results

### Final Task: Elite Athlete Profile 🏅
- Filter customers with Fitness Score = 5
- Calculate average age, education, and income
- Compare elite athletes to general population

---

## 🛠️ Technologies Used

- **Python 3.10+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Scikit-learn**: Machine learning and regression
- **SciPy**: Scientific computing
- **Jupyter Notebook**: Interactive development environment

---

## 📁 Project Structure

```
cardio-performance-analysis/
│
├── cardio-performance-analysis.ipynb    # Main analysis notebook
├── README.md                            # This file
├── requirments.txt                      # Python dependencies (note: typo in filename)                             
└── data/                                # Dataset directory
```

---

## 📊 Results

### Key Findings

**Income Distribution**
- Data shows right-skewed distribution
- Mean income higher than median, indicating wealthy outliers
- Typical customer earns closer to median value

**Product Insights**
- TM498 is the most popular product
- TM798 targets high-income segment
- Clear income-based product segmentation

**Correlation Analysis**
- Usage shows strongest positive correlation with Miles (r = 0.85+)
- Strong predictive relationship between frequency and distance

**Elite Athlete Profile**
- Average age: ~28 years
- Higher education levels (16+ years)
- Above-average income ($70K+)
- Significantly higher usage and miles




---



**Kaggle Notebook**: [View on Kaggle](https://www.kaggle.com/code/haymig/cardio-performance-analysis)

---



## 📚 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Statistical Analysis with Python](https://www.scipy.org/)

---

## 🔖 Tags

`data-analysis` `statistics` `python` `jupyter-notebook` `pandas` `matplotlib` `seaborn` `machine-learning` `regression` `data-visualization` `kaggle` `customer-analytics` `business-intelligence`

---

