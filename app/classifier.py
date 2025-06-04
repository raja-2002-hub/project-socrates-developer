import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

#  Loading dataset
df = pd.read_csv("app/dataset.csv")
X_text = df["question"]
y = df["category"]

#  Train and test dataset split
X_train_text, X_test_text, y_train, y_test = train_test_split(
    X_text, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorize
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

# Training model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

#  Evaluating the model
y_pred = model.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))

#  Save model and vectorizer
joblib.dump(model, "app/model.pkl")
joblib.dump(vectorizer, "app/vectorizer.pkl")

print("Model and vectorizer trained, validated, and saved.")
