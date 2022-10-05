
from secrets import access_key, secret_key
import boto3
import os


client = boto3.client('s3',
                      aws_access_key_id =access_key,
                      aws_secret_access_key =secret_key
                      )
#https://www.geeksforgeeks.org/python-os-listdir-method/#:~:text=listdir()%20method%20in%20python,working%20directory%20will%20be%20returned.

for file in os.listdir():#iterating over the working directory; os.listdir(path='.'
    
    if '.py' in file:#speficy file type
        
        bucket_to_upload_too = 'pythondownloads'
    #file will be stored in file called downloads, STR{I} WILL BE THE NAME OF FILE
        upload_file_key = 'downloads/'+str(file)
        
        client.upload_file(file, bucket_to_upload_too, upload_file_key)
