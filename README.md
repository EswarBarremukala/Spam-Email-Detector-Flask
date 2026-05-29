# 📨 Spam Email Detector (Flask & Machine Learning)

[![Production Deployment](https://img.shields.io/badge/Deployment-Vercel-blueviolet)](https://spam-email-detector-flask.vercel.app)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)

An end-to-end Machine Learning web application that classifies incoming text messages or emails as either **Spam** or **Ham (Legitimate)** in real-time. This project uses Natural Language Processing (NLP) to process textual data, a trained classification model to make predictions, and a lightweight Flask backend to serve the model through an interactive web interface.

The live application is deployed and accessible at: **[spam-email-detector-flask.vercel.app](https://spam-email-detector-flask.vercel.app)**

---

## 🚀 Key Features

* **Real-Time Classification:** Instantaneously processes user-inputted text and determines if it is safe or malicious.
* **NLP Pipeline:** Tokenizes and transforms raw text into numerical features using an optimized TF-IDF vectorizer.
* **Persistent Model Storage:** Pre-trained weights (`spam_model.pkl`) and vocabulary transformers (`vectorizer.pkl`) are serialized using Pickle for fast inference without re-training.
* **Clean Web UI:** A minimalist, mobile-responsive HTML frontend allows users to input data and view results clearly.
* **Modular Pipeline:** Separate scripts for training (`train_model.py`) and application serving (`app.py`), making it simple to swap or update the underlying ML architecture.

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | Flask | Handles routing, API requests, and model inference orchestration. |
| **Machine Learning** | Scikit-Learn | Powers the classification modeling and text feature extraction. |
| **Data Processing** | Pandas / NumPy | Handles structured dataset manipulations during training. |
| **Frontend** | HTML5 / CSS3 | Provides a clean, accessible interface for end-users. |
| **Deployment** | Vercel | Hosts the serverless Flask runtime environment. |

---

## 📁 Repository Structure

```text
├── templates/               # HTML frontend templates for Flask layout
├── app.py                   # Main Flask application and server routing
├── index.html               # Standard web entrypoint
├── requirements.txt         # Project software dependencies
├── spam.csv                 # Raw dataset utilized for model training
├── spam.csv.txt             # Text-formatted reference of the training dataset
├── spam_model.pkl           # Serialized predictive machine learning model
├── train_model.py           # Pipeline script to preprocess data and train the model
└── vectorizer.pkl           # Serialized TF-IDF text vectorizer feature extractor
