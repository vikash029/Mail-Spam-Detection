"""
EMAIL_SPAM_DETECTION_UI.py

- Gradio UI for detecting spam/ham emails
- Sends email alerts for both spam and ham

"""

# ================
# 1. IMPORTS
# ================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import smtplib
from email.mime.text import MIMEText
import gradio as gr

# ================
# 2. LOAD DATA & TRAIN MODEL
# ================

data = pd.read_csv("/Users/vvikash/Desktop/AL:MLproject /spam 2.csv", encoding='ISO-8859-1')

X = data['v2']  # text messages
y = data['v1']  # labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

# ================
# 3. EMAIL ALERT FUNCTION
# ================

def send_email_alert(message, label):
    sender_email = "vitthalvikash02.smart@gmail.com"        # Replace with your email
    receiver_email = "vitthalvikash29@gmail.com"  # Replace with receiver email
    password = "ikdr wnqa hbfn jyhi"               # Use App Password for Gmail




    msg = MIMEText(f"{label} detected:\n\n{message}")
    msg["Subject"] = f"{label} Alert"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        return f"Alert email sent for {label}!"
    except Exception as e:
        return f"Failed to send email: {e}"

# ================
# 4. PREDICTION FUNCTION FOR GRADIO
# ================

def predict_email(email_text):
    counts = vectorizer.transform([email_text])
    prediction = model.predict(counts)[0]

    alert_status = send_email_alert(email_text, prediction)
    return prediction, alert_status

# ================
# 5. GRADIO UI
# ================

with gr.Blocks() as demo:
    gr.Markdown("## Email Spam Detection with Alert System")
    
    with gr.Row():
        email_input = gr.Textbox(
            label="Enter Email Text", 
            placeholder="Type your email here...", 
            lines=6,
            interactive=True,       # allows copy-paste in input
            show_copy_button=True   # adds copy button
        )
    
    with gr.Row():
        predict_btn = gr.Button("Predict & Send Alert")
    
    with gr.Row():
        output_label = gr.Textbox(
            label="Prediction",
            interactive=True,       # allows copy-paste
            show_copy_button=True   # adds copy button
        )
        email_status = gr.Textbox(
            label="Alert Status",
            interactive=True,       # allows copy-paste
            show_copy_button=True   # adds copy button
        )
    
    predict_btn.click(predict_email, inputs=email_input, outputs=[output_label, email_status])

# Launch the UI
demo.launch(share=True)

