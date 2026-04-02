# 🚢 Titanic Survival Analysis

> *Can we predict who survived the Titanic disaster using only data patterns and simple logic?*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)


## 📋 Overview

This project performs a comprehensive exploratory data analysis (EDA) on the [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic) (891 passenger records) to uncover survival patterns and validate the famous **"Women and Children First"** protocol — using real historical data.

The analysis culminates in a **hand-crafted heuristic model** (pure if/else logic, no ML libraries) that predicts passenger survival with **>75% accuracy**.

## 🎯 Key Objectives

| # | Task | Description |
|---|------|-------------|
| 1 | **Data Cleaning** | Handle missing values (`Age` → median imputation, drop `Cabin`/`Ticket`/`Name`) |
| 2 | **Probability Analysis** | Compute conditional survival probabilities — P(Survived \| Gender), P(Survived \| Pclass) |
| 3 | **Feature Engineering** | Create `FamilySize` and `IsAlone` features from `SibSp` + `Parch` |
| 4 | **Heuristic Prediction** | Build a rule-based survival predictor achieving >75% accuracy |

## 📊 Key Findings

- **Gender**: Females had a **~74%** survival rate vs **~19%** for males (3.5× higher)
- **Class**: 1st class passengers (**~63%**) were **2.5×** more likely to survive than 3rd class (**~24%**)
- **Age**: Children (≤10 years) had significantly higher survival rates — confirming "children first"
- **Family**: Passengers traveling with family survived at higher rates than solo travelers
- **Heuristic Model**: Simple if/else rules achieved **>75% accuracy** on all 891 passengers

## 🗂️ Project Structure

```
titanic_notebook/
├── titanic_survival_logic.ipynb   # Main analysis notebook
├── data / dataset-2.csv           # Titanic dataset 
└── README.md                      # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/HaymiG/machine-learning-journey
cd titanic-survival-analysis
```

### 2. Create a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```



### 4. Launch the Notebook

```bash
jupyter notebook titanic_survival_logic.ipynb
```

## 🛠️ Technologies Used

| Library | Purpose |
|---------|---------|
| **pandas** | Data manipulation & analysis |
| **numpy** | Numerical operations |
| **matplotlib** | Data visualization |
| **seaborn** | Statistical plotting |
| **jupyter** | Interactive notebook environment |

## 📓 Notebook Walkthrough

The notebook is structured into **4 main parts**:

### Part 1 — Data Integrity & Cleaning 🧹
- Identify and quantify missing data
- Impute missing `Age` values with the median (robust to outliers)
- Drop irrelevant columns (`Cabin`, `Ticket`, `PassengerId`, `Name`)
- Fill missing `Embarked` values with the mode

### Part 2 — "Women and Children First" Hypothesis 👩‍👦
- **Gender analysis**: Calculate P(Survived | Gender) with bar charts and count plots
- **Class analysis**: Calculate P(Survived | Pclass) — revealing the socio-economic divide
- **Age analysis**: KDE plots comparing survivor vs. non-survivor age distributions

### Part 3 — Feature Engineering ⚙️
- Create `FamilySize = SibSp + Parch`
- Create `IsAlone` binary indicator
- Analyze survival rates across family configurations

### Part 4 — Heuristic Prediction Model 🧠
- Build a pure if/else decision function based on discovered patterns
- Evaluate accuracy against actual survival outcomes
- Generate a manual confusion matrix with precision and recall metrics



---




**Kaggle Notebook**: [View on Kaggle](https://www.kaggle.com/code/haymig/titanic-survival-logic)

---


<p align="center">
  <i>Built with 🐍 Python & 📊 Data Science</i>
</p>
