"""
EMAIL_SPAM_DETECTION_UI.py

- Gradio UI for detecting spam/ham emails
- Sends email alerts for both spam and ham
- Allows dynamic Gmail input for sender, receiver, and app password
"""

# ========================
# 1. IMPORTS
# ========================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import smtplib
from email.mime.text import MIMEText
import gradio as gr

# ========================
# 2. LOAD DATA & TRAIN MODEL
# ========================
data = pd.read_csv("/Users/vvikash/Desktop/AL:MLproject /spam 2.csv", encoding='ISO-8859-1')

X = data['v2']  # text messages
y = data['v1']  # labels (spam/ham)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

# ========================
# 3. EMAIL ALERT FUNCTION
# ========================
def send_email_alert(message, label, sender_email, receiver_email, password):
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

# ========================
# 4. PREDICTION FUNCTION FOR GRADIO
# ========================
def predict_single_email(email_text, sender_email, receiver_email, password):
    counts = vectorizer.transform([email_text])
    prediction = model.predict(counts)[0]
    alert_status = send_email_alert(email_text, prediction, sender_email, receiver_email, password)
    return prediction, alert_status

# ========================
# 5. GRADIO UI
# ========================
with gr.Blocks() as demo:
    gr.Markdown("## Email Spam Detection with Alert System")
    gr.Markdown("Enter your email text, Gmail credentials, and click Predict & Send Alert.")
    
    
    with gr.Row():
        sender_input = gr.Textbox(label="Sender Gmail", placeholder="Your Gmail address")
        receiver_input = gr.Textbox(label="Receiver Email", placeholder="Receiver email address")
    with gr.Row():
        password_input = gr.Textbox(label="Gmail App Password", placeholder="Gmail App Password", type="password")
    with gr.Row():
        email_input = gr.Textbox(label="Email Text", placeholder="Type or paste your email here...", lines=6, show_copy_button=True)
    with gr.Row():
        predict_btn = gr.Button("Predict & Send Alert")
    with gr.Row():
        output_label = gr.Textbox(label="Prediction")
        email_status = gr.Textbox(label="Alert Status")
        
    
    predict_btn.click(
        predict_single_email,
        inputs=[email_input, sender_input, receiver_input, password_input],
        outputs=[output_label, email_status]
    )

# Launch the UI
demo.launch(share=True)
