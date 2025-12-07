# 📧 Spam Email Detector (Flask & Machine Learning)

## 📌 Project Overview
This is a Machine Learning Mini-Project that detects whether an email is **Spam** or **Ham (Not Spam)** based on its content. The application is built using **Python** and **Flask** and uses the **Multinomial Naive Bayes** algorithm for classification.

## 🚀 Features
* **Real-time Prediction:** Instantly classifies emails as Spam or Safe.
* **Explainable AI:** Highlights "Trigger Words" (e.g., *free, win, cash*) to explain why an email was flagged.
* **Live History:** Displays a session history of analyzed emails (Spam vs. Safe).
* **Continuous Learning:** Automatically saves new user inputs to the dataset (`spam.csv`) for future model retraining.
* **User Interface:** A clean, responsive web interface using HTML/CSS.

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS, Jinja2 Template
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn (Naive Bayes), Pandas, CountVectorizer

## 📂 Project Structure
```text
SpamDetector/
├── app.py               # Main Flask application
├── train_model.py       # Script to train the ML model
├── spam.csv             # Dataset (Updated dynamically)
├── spam_model.pkl       # Saved Model file
├── vectorizer.pkl       # Saved Vectorizer file
├── requirements.txt     # List of dependencies
└── templates/
    └── index.html       # Frontend HTML file
