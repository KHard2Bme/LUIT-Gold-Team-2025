import boto3

s3 = boto3.client('s3')

response = s3.create_bucket ( 
    Bucket = 'harding-boto3-051125'
)

print(response)
