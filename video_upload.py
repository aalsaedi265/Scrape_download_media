from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import boto3
import os
from pytube import YouTube

PATH = r'C:\Users\16075\Documents\work\chromedriver.exe'

driver = webdriver.Chrome(PATH)

# driver.get('https://www.youtube.com/results?search_query=cyberpunk+2077+best+friend')

def scroll_down():
    down = driver.find_element(By.TAG_NAME,'html')
    down.send_keys(Keys.END)   
    time.sleep(1)

def download_video():
    page=0
    while page <2:
        scroll_down()
        link_list=driver.find_elements(By.XPATH,'//*[@id="thumbnail"]')
        
        for link in link_list:
            idx=1
            url= (link.get_attribute('href') )
            if url == None:
                continue   
            
            video = YouTube(url)
            print(url)  
            try:
                
                video.streams.get_highest_resolution().download(output_path="dowLoadToo")
            except:
                print('Error in downloading')
        
        page+=1
                
        
client = boto3.client('s3',
                      aws_access_key_id ="your access key",
                      aws_secret_access_key ="you secret aws key"
                      )
def send_video_AWS():

    for file in os.listdir('video_downloads'):
        if '.mp4' in file:
            print(file)
            bucket_to_upload_too= 'pythondownloads'
            
            thepath= 'dowLoadToo/'+file
            
            upload_file_key= 'exp7_videos/'+ str(file)
            
            client.upload_file(thepath, bucket_to_upload_too, upload_file_key)
            print('--------')
            
send_video_AWS()
driver.quit()
    