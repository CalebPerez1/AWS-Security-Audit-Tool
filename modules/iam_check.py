import boto3

def check_iam_policies():
    session = boto3.Session(profile_name="audit")
    iam = session.client("iam")
    findings = []

    try:
        users = iam.list_users()["Users"]
        for user in users:
            username = user["UserName"]
            policies = iam.list_user_policies(UserName=username)["PolicyNames"]

            for policy_name in policies:
                policy = iam.get_user_policy(UserName=username, PolicyName=policy_name)
                statements = policy["PolicyDocument"]["Statement"]

                for stmt in statements:
                    actions = stmt.get("Action", [])
                    resources = stmt.get("Resource", [])

                    # Convert string to list if needed
                    if isinstance(actions, str):
                        actions = [actions]
                    if isinstance(resources, str):
                        resources = [resources]

                    if "*" in actions or "*" in resources:
                        findings.append(
                            f"⚠️ User '{username}' has overly permissive inline policy: '{policy_name}'"
                        )
    except Exception as e:
        findings.append(f"❌ Error checking IAM policies: {str(e)}")

    if not findings:
        return "✅ No issues found."
    return "\n".join(findings)
