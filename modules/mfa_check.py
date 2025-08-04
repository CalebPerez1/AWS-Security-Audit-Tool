# modules/mfa_check.py

import boto3

def check_mfa():
    session = boto3.Session(profile_name="audit")
    iam = session.client("iam")
    findings = []

    try:
        users = iam.list_users()["Users"]
        for user in users:
            username = user["UserName"]
            mfa_devices = iam.list_mfa_devices(UserName=username)["MFADevices"]

            if not mfa_devices:
                findings.append(f"🛑 User '{username}' does NOT have MFA enabled.")
                findings.append(f"👉 To enable MFA:")
                findings.append(f"   - Sign in to the IAM console as an admin")
                findings.append(f"   - Visit: https://console.aws.amazon.com/iam/home#/users/{username}?section=security_credentials")
                findings.append(f"   - Click \"Assign MFA device\"")
                findings.append(f"   - Choose \"Virtual MFA device\" (e.g., Google Authenticator, Authy)")
                findings.append(f"   - Follow the prompts to scan the QR code and complete setup\n")
    except Exception as e:
        findings.append(f"❌ Error checking MFA: {str(e)}")

    if not findings:
        return "✅ All users have MFA enabled."
    return "\n".join(findings)
