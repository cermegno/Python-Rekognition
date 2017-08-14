import boto3  
import json
import os

aws_access_key_id = os.environ['ACCESS_KEY'],
aws_secret_access_key = os.environ['SECRET_KEY'],
region_name='us-west-2'

rk = boto3.client('rekognition')
s3 = boto3.resource('s3')

bucket = s3.Bucket("name_of_your_bucket")

for image in bucket.objects.all():
    print "\n" + image.key
    img_data = image.get()['Body'].read()

    results = rk.detect_labels(
        Image = {'Bytes': img_data},
        MaxLabels=10,
        MinConfidence=80)

    for label in results["Labels"]:  
        print str(int(label['Confidence'])) + "% confidence for " + label['Name']

