# modules/sg_check.py

import boto3

# Ports we consider sensitive
SENSITIVE_PORTS = [22, 3389, 3306, 80, 443]

def check_security_groups():
    session = boto3.Session(profile_name="audit")
    ec2 = session.client("ec2")
    findings = []

    try:
        # Get all security groups
        response = ec2.describe_security_groups()
        for sg in response["SecurityGroups"]:
            group_name = sg.get("GroupName", "Unnamed SG")
            group_id = sg.get("GroupId")

            for rule in sg.get("IpPermissions", []):
                from_port = rule.get("FromPort")
                to_port = rule.get("ToPort")
                ip_ranges = rule.get("IpRanges", [])

                for ip_range in ip_ranges:
                    cidr = ip_range.get("CidrIp", "")
                    if cidr == "0.0.0.0/0" and from_port in SENSITIVE_PORTS:
                        findings.append(
                            f"🚨 Security Group '{group_name}' ({group_id}) allows public access to port {from_port}"
                        )
    except Exception as e:
        findings.append(f"❌ Error checking security groups: {str(e)}")

    if not findings:
        return "✅ No issues found."
    return "\n".join(findings)
