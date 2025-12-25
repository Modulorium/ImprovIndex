import json
import boto3

class EnvSecrets:
    def __init__(self):
        import os
        client = boto3.client('secretsmanager', region_name="us-east-2")
        secret_env = os.environ.get("ENV_SECRET_NAME", "INT_SECRETS")
        response = client.get_secret_value(SecretId=secret_env)
        secret_str = response.get('SecretString')
        secret_data = json.loads(secret_str)
        # Set environment secret attributes
        self.ENV_SECRETS_NAME: str = os.environ.get("ENV_SECRET_NAME", "INT_SECRETS")
        self.API_BASE_URL: str = secret_data.get('API_BASE_URL')

class SecretsManagerService:
    def __init__(self):
        self.client = boto3.client('secretsmanager', region_name="us-east-2")

    def get_secret(self, secret_name):
        response = self.client.get_secret_value(SecretId=secret_name)
        return response.get('SecretString')
