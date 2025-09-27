<img width="2520" height="1572" alt="image" src="https://github.com/user-attachments/assets/d9bd950e-19ec-4050-a65d-ab19af7e8473" />



Folder structure:

email-spam-detection-ui/

├── EMAIL_SPAM_DETECTION_UI.py

├── spam_2.csv  # Place your dataset here

├── requirements.txt

└── README.md

---


# requirements.txt

```
pandas
scikit-learn
gradio
```

---

# README.md

```
# Email Spam Detection UI

Detect spam and ham emails with a Naive Bayes classifier.

## Features
- Spam/Ham detection
- Sends alert emails
- Interactive Gradio UI
- Copy-paste enabled textbox

## Installation

1. Clone repository:
```

git clone https://github.com/vikash029/Mail-Spam-Detection

cd email-spam-detection-ui

```

2. Install dependencies:
```

pip install -r requirements.txt

```

## Usage
```

python EMAIL_SPAM_DETECTION_UI.py

```
Enter email text, sender/receiver Gmail, and app password. Click Predict & Send Alert.

## Notes
- Use Gmail App Password for email alerts.

1. Enable 2-Step Verification on Gmail

Go to your Google Account Security
 page.

Under “Signing in to Google”, find 2-Step Verification and click Turn on.

Follow the steps to enable it (usually via SMS or Google Authenticator).

2. Generate a Gmail App Password

Go to App Passwords
 in your Google Account.

Under Select app, choose Other (Custom name).

Give it a name like EmailSpamAlert.

Click Generate.

Google will give you a 16-character app password. Copy it (you’ll need it in your script).

- Tested with Python 3.13+

 ```
---
## Author   Vitthal Vikash
---
