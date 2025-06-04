import joblib
import numpy as np

# Load trained model and vectorizer
model = joblib.load("app/model.pkl")
vectorizer = joblib.load("app/vectorizer.pkl")

#  Function to Return just the predicted category
def classify_question(text: str) -> str:
    X = vectorizer.transform([text])
    return model.predict(X)[0]

# Function to Return predicted category and confidence
def predict_category(question: str):
    X = vectorizer.transform([question])
    probabilities = model.predict_proba(X)[0]
    max_index = np.argmax(probabilities)
    predicted_class = model.classes_[max_index]
    confidence = probabilities[max_index]
    return predicted_class, round(confidence, 3)
