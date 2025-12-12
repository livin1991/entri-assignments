import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load data
df = pd.read_excel("Dry_Bean_Dataset.xlsx")
df = df.drop_duplicates()

# Encode target
label_map = {
    'DERMASON':0,'SIRA':1,'SEKER':2,
    'HOROZ':3,'CALI':4,'BARBUNYA':5,'BOMBAY':6
}

X = df.drop(columns=['Class']).values
y = df['Class'].map(label_map).values

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2022
)

# Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train FINAL MODEL ✅
model = LogisticRegression(max_iter=150)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save artifacts ✅
pickle.dump(model, open("model.pkl","wb"))
pickle.dump(scaler, open("scaler.pkl","wb"))
pickle.dump(label_map, open("label_map.pkl","wb"))
