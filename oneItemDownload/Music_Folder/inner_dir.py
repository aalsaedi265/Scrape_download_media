# from secrets import access_key, secret_key
import boto3
import os


client = boto3.client('s3',
                      aws_access_key_id ='',
                      aws_secret_access_key =''
                      )

for file in os.listdir():#iterating over the working directory; os.listdir(path='.'
        print(file)
        if  '.mp4'in file: #speficy file type
            
                bucket_to_upload_too = 'pythondownloads'
                #file will be stored in file called downloads, STR{I} WILL BE THE NAME OF FILE
                upload_file_key = 'all_downloads/'+str(file)
                
                client.upload_file(file, bucket_to_upload_too, upload_file_key)



# import sys
# sys.path.append(r'C:\Users\16075\Documents\work\scrape_download')

# import awsLink_download

# awsLink_download.worked()

# awsLink_download.send_PythonFiles_inDirectory_toTheCloud()