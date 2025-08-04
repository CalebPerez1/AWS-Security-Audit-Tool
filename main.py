# main.py

import argparse
from datetime import datetime

from modules.iam_check import check_iam_policies
from modules.s3_check import check_s3_buckets
from modules.sg_check import check_security_groups
from modules.mfa_check import check_mfa
from modules.slack_notify import send_slack_notification
from modules.splunk_notify import send_to_splunk  # 👈 Added for Splunk

# Slack webhook
slack_webhook_url = "https://hooks.slack.com/services/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"

# Splunk config
splunk_url = "https://localhost:8088/services/collector"
splunk_token = "b1c5b6c9-8319-4a85-bbc6-4328eac71de8"  

# Parse command line arguments
parser = argparse.ArgumentParser(description="AWS Security Audit Tool")
parser.add_argument('--check', choices=['iam', 's3', 'sg', 'mfa'], help='Run a specific check only')
args = parser.parse_args()

# Generate timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")

# Start building the result message
result = f"📋 *AWS Security Audit Results*\n🕒 *Timestamp:* {timestamp}\n\n"

splunk_log = {
    "timestamp": timestamp
}

# Run individual or all checks
if args.check == 'iam' or not args.check:
    iam_result = check_iam_policies()
    result += "*--- IAM ---*\n" + iam_result + "\n\n"
    splunk_log["iam"] = iam_result

if args.check == 's3' or not args.check:
    s3_result = check_s3_buckets()
    result += "*--- S3 ---*\n" + s3_result + "\n\n"
    splunk_log["s3"] = s3_result

if args.check == 'sg' or not args.check:
    sg_result = check_security_groups()
    result += "*--- SECURITY_GROUPS ---*\n" + sg_result + "\n\n"
    splunk_log["security_groups"] = sg_result

if args.check == 'mfa' or not args.check:
    mfa_result = check_mfa()
    result += "*--- MFA ---*\n" + mfa_result + "\n"
    splunk_log["mfa"] = mfa_result

# Save audit to file
with open("/Users/caleb/aws_security_audit_tool/audit.log", "a") as log_file:
    log_file.write(result + "\n")

# Send to Slack
send_slack_notification(slack_webhook_url, result)

# Send to Splunk
send_to_splunk(splunk_log, splunk_url, splunk_token)

# Print to terminal
print(result)
