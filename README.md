# Email Spam Detection UI

This project uses a machine learning model to detect **spam** and **ham** emails.  
It features a **Gradio web UI** and sends email alerts when a message is detected.

---

## Features
- Detects spam and ham emails using **Naive Bayes** classifier.
- Sends alert emails for both spam and ham messages.
- Interactive and user-friendly **Gradio UI**.
- Copy-paste enabled textbox for easy usage.

---

Installation

1. **Clone the repository:**

git clone https://github.com/yourusername/email-spam-detection-ui.git
cd email-spam-detection-ui

2. Install dependencies:

pip install -r requirements.txt


Usage

Run the Python script:

python EMAIL_SPAM_DETECTION_UI.py


Open the browser at http://127.0.0.1:7867.

Enter your email text, click Predict & Send Alert, and view:

Prediction: spam or ham

Alert Status: confirmation if email alert was sent

Example
Email: You won a free lottery ticket! Click here to claim
Prediction: spam
Alert: Alert email sent for spam!

Email: Hi John, are we still on for the meeting tomorrow?
Prediction: ham
Alert: Alert email sent for ham!

Notes

Use a Gmail App Password for email alerts.

For public sharing, set share=True in demo.launch() to generate a temporary public URL.

Tested with Python 3.13+.

Dependencies

pandas

scikit-learn

gradio

Install all dependencies using:

pip install -r requirements.txt

License

This project is open-source and available under the MIT License.


---

### `requirements.txt` example
pandas==2.1.1
scikit-learn==1.3.2
gradio==3.50.1
---
