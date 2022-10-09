
from secrets import access_key, secret_key
import boto3
import os


client = boto3.client('s3',
                      aws_access_key_id =access_key,
                      aws_secret_access_key =secret_key
                      )
# C:\Users\16075\Documents\work\scrape_download\oneItemDownload\Music_Folder
# C:\Users\16075\Documents\work\scrape_download\harvesImages

def send_PythonFiles_inDirectory_toTheCloud():
    
    for file in os.listdir('oneItemDownload/Music_Folder'):#iterating over the working directory; os.listdir(path='.'
        print(file)
        if  '.mp4'in file:#speficy file type, if not will assocate with ally files & FOLDERS
            bucket_to_upload_too = 'pythondownloads'
            print('--------------the world--------------')
                        #file will be stored in file called downloads, STR{I} WILL BE THE NAME OF FILE
            upload_file_key = 'music_downloads/'+str(file)
            thePath='oneItemDownload/Music_Folder/'+file
            client.upload_file(thePath, bucket_to_upload_too, upload_file_key)      
        

#send_PythonFiles_inDirectory_toTheCloud has two constraints
    #1. WILL ENGAGE ONLY WITH FILE IN ITS DIRECTORY
    #2. WILL NOT ACCEPT FOLDERS OR SPECIAL FILE (.git)
    
send_PythonFiles_inDirectory_toTheCloud()
def worked():
    print('imported')