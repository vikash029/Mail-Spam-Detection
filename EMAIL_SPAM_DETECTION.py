# -*- coding: utf-8 -*-
"""
EMAIL_SPAM_DETECTION.py

Improved version of your Colab notebook:
- Clean structure
- Clear function separation
- Added comments
"""

# ================
# 1. IMPORTS
# ================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# ================
# 2. LOAD DATA
# ================
# Example: Load from CSV (replace with your dataset path)
# Dataset must have columns: 'text' and 'label'

data = pd.read_csv("/Users/vvikash/Desktop/AL:MLproject /spam 2.csv" , encoding='ISO-8859-1')

# Check the first rows

print("Dataset preview:")
print(data.head())

# ================
# 3. PREPROCESSING
# ================
# Use the correct columns
X = data['v2']  # text messages
y = data['v1']  # labels
        # spam / ham

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text to numerical features
vectorizer = CountVectorizer(stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# ================
# 4. MODEL TRAINING
# ================
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# ================
# 5. EVALUATION
# ================
y_pred = model.predict(X_test_counts)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ================
# 6. USAGE EXAMPLE
# ================
new_emails = [
    "You won a free lottery ticket! Click here to claim",
    "Hi John, are we still on for the meeting tomorrow?"
]

new_counts = vectorizer.transform(new_emails)
predictions = model.predict(new_counts)

for email, label in zip(new_emails, predictions):
    print(f"\nEmail: {email}\nPrediction: {label}")
