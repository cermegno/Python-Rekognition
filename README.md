# Python-Rekognition
Sample Python scripts to interact with AWS Rekognition. Developed for Pied Piper program 2017
You can find a more elaborated discussion in the following article
http://anzpiper.blogspot.com.au/2017/08/image-analysis-with-aws-rekognition.html

## Usage
* Before starting make sure you install Boto3 module by running "*pip install boto3*"
* Then you need to ensure the AWS credentials are available to the script. You could accomplish this by means of:
  + Running the "*aws configure*" command if you have AWS CLI installed
  + Setting environment variables for access and secret keys
  + Creating an "*~/.aws/credentials*" file as follows. I couldn't find where the actual location for this file in Windows so I resorted to setting environment variables.
```SHELL
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
* Finally you are going to need an S3 bucket and photos. You will need to make sure you specify the region that contains your S3 bucket
