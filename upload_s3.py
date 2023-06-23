import boto3
import json


class S3Uploader:
    def __init__(self):
        self.bucket_name = "cx-poc-sustainability"
        self.session = boto3.Session(
            aws_access_key_id="*****",
            aws_secret_access_key="******"
        )

    def upload_json_file(self, file_name, data):
        s3_client = self.session.client('s3')
        s3_client.put_object(
            Body=json.dumps(data),
            Bucket=self.bucket_name,
            Key=file_name
        )
        print(f"Uploaded file '{file_name}' to S3 bucket '{self.bucket_name}'.")

