import boto3
import json


class S3Uploader:
    def __init__(self):
        self.bucket_name = "cx-poc-sustainability"
        self.session = boto3.Session(
            aws_access_key_id="****",
            aws_secret_access_key="****"
        )

#    def upload_json_file(self, file_name, data):
#        s3_client = self.session.client('s3')
#        s3_client.put_object(
#            Body=json.dumps(data),
#            Bucket=self.bucket_name,
#            Key=file_name
#        )

    def upload_json_file(self, file_name, data):
        s3_client = self.session.client('s3')
        # Convert JSON data to a string without escape characters
        json_string = json.dumps(data)

        s3_client.put_object(
            Body=json_string,
            Bucket=self.bucket_name,
            Key=file_name
        )
        print(f"Uploaded file '{file_name}' to S3 bucket '{self.bucket_name}'.")

    def upload_file(self, file_path):
        s3_client = self.session.client('s3')
        file_name = os.path.basename(file_path)

        try:
            s3_client.upload_file(file_path, self.bucket_name, "")
            print("File uploaded successfully to S3.")
        except Exception as e:
            print("Error uploading file to S3:", str(e))
