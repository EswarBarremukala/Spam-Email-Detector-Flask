from flask import Flask, render_template, request
import pickle
import csv  # New import for handling CSV files

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

# Global lists to store history for the current session
# These will show up in the "sections" on your screen
spam_history = []
ham_history = []

@app.route("/")
def home():
    return render_template("index.html", spam_history=spam_history, ham_history=ham_history)

@app.route("/predict", methods=["POST"])
def predict():
    email_id = request.form['email_id']
    message = request.form['message']

    # 1. Predict
    vectorized_msg = cv.transform([message]).toarray()
    prediction = model.predict(vectorized_msg)
    result = "SPAM" if prediction[0] == 'spam' else "NOT SPAM"

    # 2. Logic for Reason (The "Why")
    explanation = ""
    if result == "SPAM":
        spam_triggers = ['free', 'win', 'cash', 'urgent', 'prize', 'money', 'click', 'offer']
        found_words = [word for word in spam_triggers if word in message.lower()]
        if found_words:
            explanation = f"Detected suspicious words: {', '.join(found_words)}"
        else:
            explanation = "Sentence structure matches spam patterns."
    else:
        explanation = "Content appears safe."

    # 3. SAVE DATA TO CSV (The "Learning" Part)
    # We append: label, message, email_id
    label_to_save = "spam" if result == "SPAM" else "ham"
    
    with open('spam.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Writing in the order: label, message, email_id
        writer.writerow([label_to_save, message, email_id])

    # 4. Update the Front End Lists
    if result == "SPAM":
        spam_history.append({'email': email_id, 'msg': message})
    else:
        ham_history.append({'email': email_id, 'msg': message})

    return render_template("index.html", 
                           prediction=result, 
                           reason=explanation, 
                           email_id=email_id, 
                           message=message,
                           spam_history=spam_history,
                           ham_history=ham_history)

if __name__ == "__main__":
    app.run(debug=True)
