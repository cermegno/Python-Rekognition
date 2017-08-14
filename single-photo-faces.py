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
results = rk.detect_faces(  
    Image = {'Bytes': img_data},
    Attributes = ['ALL'])
#print json.dumps(results['FaceDetails'], indent=4)

# Display results
for each_face in results['FaceDetails']:  
    print "\n" + str(int(each_face['Confidence'])) + "% confidence"
    print "  Gender :\t " + each_face['Gender']['Value']
    print "  Age    :\t" + str(each_face['AgeRange']['Low']) + " to " + str(each_face['AgeRange']['High'])
    for emotion in each_face['Emotions']:
        print "  {}  :\t {}%".format(emotion['Type'].title(), str(int(emotion['Confidence'])))
