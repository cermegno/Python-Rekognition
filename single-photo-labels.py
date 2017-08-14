import boto3  
import json
import os

aws_access_key_id = os.environ['ACCESS_KEY'],
aws_secret_access_key = os.environ['SECRET_KEY'],
region_name='us-west-2'

rk = boto3.client('rekognition')
s3 = boto3.resource('s3')

# Get a handle on the photo and read it
bucket = "name_of_your_bucket"
photo = 'photo_name.jpg'
image = s3.Object(bucket, photo)
img_data = image.get()['Body'].read()

# Send it to Rekognition
results = rk.detect_labels(
    Image={'Bytes': img_data},
    MaxLabels=10,
    MinConfidence=80)
##print json.dumps(results['Labels'], indent=4)

# Display results
for label in results["Labels"]:  
    print str(int(label['Confidence'])) + "% confidence for " + label['Name']
