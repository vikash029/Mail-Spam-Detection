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

## Installation

1. **Clone the repository:**
```bash

git clone https://github.com/yourusername/email-spam-detection-ui.git
cd email-spam-detection-ui
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Python script:

bash
Copy code
python EMAIL_SPAM_DETECTION_UI.py

Enter your email text, click Predict & Send Alert, and view:

Prediction: spam or ham

Alert Status: confirmation if email alert was sent

Example
vbnet
Copy code
Email: You won a free lottery ticket! Click here to claim
Prediction: spam
Alert: Alert email sent for spam!

Email: Hi John, are we still on for the meeting tomorrow?
Prediction: ham
Alert: Alert email sent for ham!
Notes
Make sure to use a Gmail App Password for email alerts.

For public sharing, set share=True in demo.launch() to generate a temporary public URL.

Tested with Python 3.13+.

Dependencies
pandas

scikit-learn

gradio

Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
License
This project is open-source and available under the MIT License.

yaml
Copy code

---

If you want, I can also **write the `requirements.txt` and make a complete GitHub-ready folder** so you can push it directly.  

Do you want me to do that next?






