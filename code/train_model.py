import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Load Dataset
# Note: encoding='latin-1' is often required for this dataset
df = pd.read_csv("D:\project\SPAM\spam.csv.txt", encoding="latin-1")
df.dropna(how="any", inplace=True)

# 2. Rename columns for clarity (v1 is label, v2 is message)
df.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)

# 3. Convert text to numbers (Vectorization)
cv = CountVectorizer()
X = cv.fit_transform(df['message']) # X is the "features"
y = df['label']                     # y is the "target" (spam or ham)

# 4. Train the Model (Naive Bayes)
model = MultinomialNB()
model.fit(X, y)

# 5. Save the Model and Vectorizer
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(cv, open("vectorizer.pkl", "wb"))

print("Success! Model and Vectorizer saved.")