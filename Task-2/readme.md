# 🎯 Internship Success Prediction Using Machine Learning

This project builds a predictive model to estimate **internship success** using synthetic student performance data. It applies multiple classification algorithms and compares their performance using various metrics.

---

## 📌 Project Overview

- **Goal**: Predict whether a student will succeed in an internship based on features like GPA, projects, participation hours, domain, etc.
- **Dataset**: Synthetic dataset of 500 students with academic and engagement features.
- **Target Variable**: `Success` (1 = Success, 0 = Failure)

---

## 📊 Features Used

- GPA
- Projects Completed
- Participation Hours
- Prior Internships
- Domain (One-hot encoded)

---

## 🧠 Models Applied

- ✅ Logistic Regression
- ✅ Random Forest Classifier
- ✅ Support Vector Machine (SVM)

Each model is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score (via classification report)**

---

## 📈 Outputs

- 📊 **Model Performance Comparison**  
  A bar chart comparing accuracy, precision, and recall across models  
  → **`model_performance.png`**

- 🔍 **Feature Importance**  
  A horizontal bar chart showing top contributing features (via Random Forest)  
  → **`feature_importance.png`**

---

## 🛠️ Tech Stack

- Python 3
- pandas, numpy
- scikit-learn
- matplotlib, seaborn

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
2. Run the script:
    python task2_success_prediction.py


📁 Files Included:-

    ├── task2_success_prediction.py      # Main Python script
    ├── model_performance.png            # Bar chart comparing model metrics
    ├── feature_importance.png           # Random Forest feature importance plot
    ├── README.md                        # Project documentation
