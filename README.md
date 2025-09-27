<img width="2520" height="1572" alt="image" src="https://github.com/user-attachments/assets/d9bd950e-19ec-4050-a65d-ab19af7e8473" />



📧 Email Spam Detection UI




Detect spam and ham emails using a Naive Bayes classifier.
Interactive Gradio UI with email alert functionality.

🚀 Features

✅ Spam/Ham email detection

✅ Sends alert emails for both spam and ham

✅ Interactive Gradio UI with copy-paste enabled textboxes

✅ Input validation for all fields

🗂 Folder Structure
email-spam-detection-ui/
├── EMAIL_SPAM_DETECTION_UI.py
├── spam_2.csv          # Place your dataset here
├── requirements.txt
└── README.md

⚡ Installation

Clone the repository:

git clone https://github.com/vikash029/Mail-Spam-Detection
cd email-spam-detection-ui


Install dependencies:

pip install -r requirements.txt


Run the app:

python EMAIL_SPAM_DETECTION_UI.py

🎯 Usage

Enter:

Sender Gmail

Receiver Gmail

Gmail App Password

Paste or type your email text.

Click Predict & Send Alert.

View Prediction and Alert Status.

🔐 Gmail App Password Setup

Required for sending email alerts.

1. Enable 2-Step Verification

Go to your Google Account Security

Under “Signing in to Google”, enable 2-Step Verification

2. Generate an App Password

Go to App Passwords

Select Other (Custom name) → e.g., EmailSpamAlert

Click Generate

Copy the 16-character app password and use it in the UI

📊 Dataset

Place spam_2.csv in the project folder

Required columns:

v1 → Label (spam/ham)

v2 → Email text

🛠 Dependencies

pandas

scikit-learn

gradio

Install with:

pip install -r requirements.txt

🖊 Author

Vitthal Vikash

✅ Tested with Python 3.13+
🌐 Gradio UI supports public sharing by setting share=True in demo.launch()

