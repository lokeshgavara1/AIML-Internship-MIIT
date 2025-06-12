import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Create synthetic dataset
n_students = 500
domains = ['Machine Learning', 'Web Development', 'Data Science', 'Cybersecurity', 
           'Mobile App Development', 'Cloud Computing', 'IoT']
data = {
    'Student_ID': range(1, n_students + 1),
    'GPA': np.random.normal(3.5, 0.5, n_students).clip(2.0, 4.0),
    'Projects_Completed': np.random.randint(0, 10, n_students),
    'Participation_Hours': np.random.randint(10, 100, n_students),
    'Domain': np.random.choice(domains, n_students),
    'Prior_Internships': np.random.randint(0, 3, n_students),
    'Success': np.random.choice([0, 1], n_students, p=[0.3, 0.7])  # 1: Success, 0: Failure
}

df = pd.DataFrame(data)

# Preprocessing
df = pd.get_dummies(df, columns=['Domain'], drop_first=True)

# Define features and target
X = df.drop(['Student_ID', 'Success'], axis=1)
y = df['Success']

# Handle missing data
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42)
}

# Train and evaluate
results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    results.append({
        'Model': name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall
    })
    print(f"\nClassification Report for {name}:\n", classification_report(y_test, y_pred, zero_division=0))

# Results DataFrame
results_df = pd.DataFrame(results)

# Visualize model performance
plt.figure(figsize=(10, 6))
results_df.set_index('Model')[['Accuracy', 'Precision', 'Recall']].plot(kind='bar')
plt.title('Model Performance Comparison')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('model_performance.png')

# Feature importance (Random Forest)
rf = models['Random Forest']
feature_names = df.drop(['Student_ID', 'Success'], axis=1).columns  # FIXED HERE
importances = pd.Series(rf.feature_importances_, index=feature_names)
plt.figure(figsize=(10, 6))
importances.sort_values().plot(kind='barh')
plt.title('Feature Importance (Random Forest)')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig('feature_importance.png')

print("\nModel Performance Summary:\n", results_df)
