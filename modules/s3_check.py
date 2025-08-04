import boto3

def check_s3_buckets():
    session = boto3.Session(profile_name="audit")
    s3 = session.client("s3")
    findings = []

    try:
        buckets = s3.list_buckets()["Buckets"]
        for bucket in buckets:
            bucket_name = bucket["Name"]
            try:
                acl = s3.get_bucket_acl(Bucket=bucket_name)
                for grant in acl["Grants"]:
                    grantee = grant["Grantee"]
                    if grantee.get("URI") in [
                        "http://acs.amazonaws.com/groups/global/AllUsers",
                        "http://acs.amazonaws.com/groups/global/AuthenticatedUsers",
                    ]:
                        findings.append(f"⚠️ Bucket '{bucket_name}' is publicly accessible via ACL.")
            except Exception as e:
                findings.append(f"❌ Could not check ACL for bucket '{bucket_name}': {str(e)}")
    except Exception as e:
        findings.append(f"❌ Error listing buckets: {str(e)}")

    if not findings:
        return "✅ No issues found."
    return "\n".join(findings)
