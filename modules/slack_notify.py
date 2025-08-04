# modules/slack_notify.py

import requests

def send_slack_notification(webhook_url, message):
    payload = {
        "text": message
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print("✅ Slack notification sent.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Slack notification failed: {e}")
