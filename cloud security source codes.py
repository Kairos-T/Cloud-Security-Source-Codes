# 01: DATA ENCRYPTION BEFORE UPLOADING TO CLOUD
import boto3
import hashlib
import os

def encrypt_data(data, key):
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    padding = AES.block_size - len(data) % AES.block_size
    data += bytes([padding]) * padding
    ciphertext = encryptor.encrypt(data)
    return iv + ciphertext

def upload_encrypted_data_to_s3(bucket, key, data, keyfile):
    s3 = boto3.client('s3')
    with open(keyfile, 'rb') as f:
        key = f.read()
    encrypted_data = encrypt_data(data, key)
    s3.put_object(Bucket=bucket, Key=key, Body=encrypted_data)

#02: ACCESS CONTROLS MANAGEMENT FOR CLOUD RESOURCES (AWS SDK)
import boto3

def grant_bucket_access_to_user(bucket, user):
    s3 = boto3.resource('s3')
    bucket_acl = s3.BucketAcl(bucket)
    response = bucket_acl.grants
    grant = boto3.s3.acl.Grant(full_control, user)
    bucket_acl.put(Grant)

def revoke_bucket_access_for_user(bucket, user):
    s3 = boto3.resource('s3')
    bucket_acl = s3.BucketAcl(bucket)
    response = bucket_acl.grants
    grant = boto3.s3.acl.Grant(full_control, user)
    bucket_acl.revoke_grant(grant)

def create_iam_user(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    return response['User']['Arn']

#03 CLOUD RESOURCES FOR VULNERABILITIES (OpenSCAP Python API)
import os
import openscap_api

def scan_ec2_instance_for_vulnerabilities(instance_id):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(instance_id)
    ip_address = instance.public_ip_address
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    target = "sshd://%s@%s" % (username, ip_address)
    oscap = openscap_api.Oscap(target)
    oscap.scap_scan("/usr/share/openscap/cpe/openscap-cpe-dictionary.xml", "xccdf_org.ssgproject.content_profile_pci-dss", "/usr/share/openscap/policies/pci-dss-policy.xml")