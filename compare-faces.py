import boto3  
import json
import os

aws_access_key_id = os.environ['ACCESS_KEY']
aws_secret_access_key = os.environ['SECRET_KEY']
region_name='us-west-2'

rk = boto3.client('rekognition', region_name=region_name, aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)
s3 = boto3.resource('s3', region_name=region_name, aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)

bucket = "name_of_your_bucket"
photo1 = 'source_photo.jpg'
photo2 = 'target_photo.jpg'

# Send it to Rekognition
results = rk.compare_faces(  
    SourceImage = {"S3Object": {"Bucket": bucket, "Name": photo1}},
    TargetImage = {"S3Object": {"Bucket": bucket, "Name": photo2}},
	SimilarityThreshold=50)
print json.dumps(results['FaceMatches'], indent=4)

