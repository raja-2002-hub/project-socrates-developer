# 🧠 Project Socrates Developer

An AI-powered Socratic dialogue web app built with **FastAPI**, **OpenAI GPT-4o**, and **Random Forest Classifier**. This app predicts the philosophical category of a user question and replies with a Socratic-style reflective prompt.

---

## 🎯 Objective

To simulate Socratic conversation using GPT-4o and accurately categorize questions into domains like **Ethics**, **Logic**, **Politics**, **Metaphysics**, **Epistemology**, and **AI** using a traditional ML model.

---

## 💻 Tech Stack

- 🔹 FastAPI (backend API)
- 🔹 OpenAI GPT-4o (LLM API)
- 🔹 HTML/CSS/JS (minimal frontend)
- 🔹 RandomForestClassifier (scikit-learn)
- 🔹 NLTK (lemmatization)
- 🔹 Joblib (model serialization)

---

## 🗂️ Project Structure

project-socrates-developer/
│
├── app/
│ ├── main.py # FastAPI application logic
│ ├── llm_api.py # Handles OpenAI API logic
│ ├── predictor.py # Category prediction with confidence
│ ├── classifier.py # Model training script
│ ├── nlp_utils.py # Preprocessing utilities
│ ├── socrates.py # LLM prompt logic
│ ├── socratic_data.py # Optional data extension
│ ├── model.pkl # Trained classifier
│ ├── vectorizer.pkl # TF-IDF vectorizer
│ └── Dataset.csv # 600+ labeled questions
│
├── frontend/
│ └── index.html # User interface
│
├── .env # API key file (not versioned)
├── requirements.txt # Python dependencies
├── Procfile # For deployment (Heroku/Render)
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/raja-2002-hub/project-socrates-developer.git
cd project-socrates-developer
```

2. Install Dependencies
pip install -r requirements.txt


3. Configure Environment Variables
Create a .env file in the root directory:

OPENAI_API_KEY=your-api-key-here
You can generate your key at: https://platform.openai.com/account/api-keys

🚀 Run the App Locally
uvicorn app.main:app --reload
Then visit: http://localhost:8000



