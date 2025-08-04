# modules/splunk_notify.py

import requests
import json
import datetime

def send_to_splunk(log_data, splunk_url, token):
    headers = {
        'Authorization': f'Splunk {token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "time": datetime.datetime.now().timestamp(),
        "event": log_data
    }

    try:
        response = requests.post(splunk_url, headers=headers, data=json.dumps(payload), verify=False)
        if response.status_code == 200:
            print("[+] Splunk: Log sent successfully.")
        else:
            print(f"[!] Splunk: Failed to send log. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"[!] Splunk: Exception occurred - {e}")
