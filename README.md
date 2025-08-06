# AWS Security Audit Tool 🔐

A simple CLI-based Python tool to automatically audit key AWS security configurations. This tool checks:

- **IAM Policies**
- **S3 Bucket Permissions**
- **Security Groups**
- **MFA Enforcement**

It sends results to:
- **Slack** (via Incoming Webhook)
- **Splunk** (via HTTP Event Collector)

---

## 🔧 Features

✅ Automated audit results every 12 hours  
✅ Slack notifications with clear pass/warning formatting  
✅ Splunk log forwarding for SIEM integration  
✅ Simple cronjob-based automation  
✅ Timestamped audit logs saved locally  

---

## 📁 File Structure

aws_security_audit_tool/
├── modules/
│   ├── iam_check.py
│   ├── s3_check.py
│   ├── sg_check.py
│   ├── mfa_check.py
│   ├── slack_notify.py
│   └── splunk_notify.py
├── audit.log
├── main.py
├── README.md
└── requirements.txt

---

## 🚀 How It Works

1. Scans AWS IAM users, S3 buckets, and security groups.  
2. Validates if MFA is enforced for all users.  
3. Builds a timestamped report.  
4. Sends the report to Slack and Splunk.  
5. Appends results to a local `audit.log`.

---

## 📦 Requirements

- Python 3.9+
- boto3
- requests
- AWS IAM credentials with read-only permissions
- Slack Incoming Webhook URL
- Splunk HEC Token (if using Splunk)

Install dependencies:
pip install -r requirements.txt

---

## ⚙️ Setup Instructions

Follow these steps to configure and run the AWS Security Audit Tool on your system.


1. ✅ Set Up AWS Credentials

Make sure you have the AWS CLI installed. Then run:

```bash
aws configure



2. 📦 Install Dependencies

Ensure you’re inside your virtual environment (if using one), then install the required Python packages:
pip install -r requirements.txt

Dependencies include:
	•	boto3 – AWS SDK for Python
	•	requests – for Slack and Splunk HTTP requests



3. 🔗 Configure Slack Webhook

In main.py, replace the placeholder webhook with your actual Slack Incoming Webhook URL:slack_webhook_url = "https://hooks.slack.com/services/your/webhook/url"



4. 📄 Run the Tool

To run all checks and send the results to Slack and/or Splunk: python main.py
To run a specific check only:
python main.py --check iam
python main.py --check s3
python main.py --check sg
python main.py --check mfa 

---

## 🧠 Example Use Case

Imagine a business with an expanding AWS footprint. The security team wants daily visibility into potential risks without relying on expensive enterprise tooling.  
They deploy this tool on a dedicated macOS machine and schedule it to run every 12 hours using LaunchAgents.  
It scans for risky IAM permissions, open security groups, public S3 buckets, and users without MFA.  
The results are automatically pushed to a Slack channel and indexed into Splunk for visualization and audit logs.  
With minimal setup and no ongoing cloud costs, the team now gets actionable alerts and visibility.

---

## 💡 Future Ideas

- 📧 Email alert support (SMTP integration)  
- 📊 Export results as CSV or JSON  
- 🧩 Build a lightweight Flask GUI for visual reports  
- 🏢 Add AWS Organizations multi-account support  
- 🔐 Detect overly permissive IAM roles (e.g., `iam:*`)  
- 📍 Geo-location insights for suspicious IPs (CloudTrail lookup)  
- ☁️ Support for Azure and GCP in the future

---

## 👤 Author

Built by Caleb Oduro  
Information Systems Intern | Cybersecurity Student.

This project was created as part of a personal portfolio to demonstrate:

- 🛠 Hands-on AWS security experience  
- 🧠 Familiarity with IAM, S3, and network policies  
- 🔔 Slack alert integration  
- 📈 Splunk logging and monitoring  
- ⏰ Automation via macOS scheduling

---

## 🔗 Connect

Follow the journey on  
[GitHub](https://github.com/CalebPerez1) • [LinkedIn](https://www.linkedin.com/in/caleb-perez-o)

---
