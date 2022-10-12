from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import boto3
import os



location_of_chromDriver= r'C:\Users\16075\Documents\work\chromedriver.exe'
driver = webdriver.Chrome(location_of_chromDriver)
driver.get('https://www.youtube.com/')

time.sleep(2)

search = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.send_keys('barstoo sports')
search.send_keys(Keys.ENTER)

time.sleep(4)

down = driver.find_element(By.TAG_NAME,'html')
down.send_keys(Keys.END)   
time.sleep(2)
driver.save_screenshot('screenShot_placement/youtube_screenGrab.png')


client = boto3.client('s3',
                      aws_access_key_id ='access_key',
                      aws_secret_access_key ='secret_key'
                      )
# C:\Users\16075\Documents\work\scrape_download\oneItemDownload\Music_Folder
# C:\Users\16075\Documents\work\scrape_download\harvesImages

def send_PythonFiles_inDirectory_toTheCloud():
    
    for file in os.listdir('screenShot_placement'):#iterating over the working directory; os.listdir(path='.'
        print(file)
        if  '.png'in file:#speficy file type, if not will assocate with ally files & FOLDERS
            bucket_to_upload_too = 'pythondownloads'
            print('--------------the world--------------')
                        #file will be stored in file called downloads, STR{I} WILL BE THE NAME OF FILE
            upload_file_key = 'exp7/'+str(file)
            thePath='screenShot_placement/'+file
            client.upload_file(thePath, bucket_to_upload_too, upload_file_key)      
        


driver.quit()