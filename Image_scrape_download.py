import requests
import io
from selenium.webdriver.common.by import By
from PIL import Image #from Pillow library convert memory(bytes) to image
from selenium import webdriver
import time

path = r'C:\Users\16075\Documents\work\automationScrap\chromedriver.exe'

driver = webdriver.Chrome(path)

# saveLocation =r'C:\Users\16075\Documents\work\scrape_download\oneItemDownload'


def get_images(driver, delay, limit):
    #click on item, grab main resoultin, scroll
    def scroll(driver):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #exceute script will use javascript to scroll
        time.sleep(delay) 
        
    url ='https://www.google.com/search?q=cyberpunk+outfit&tbm=isch&hl=en&nfpr=1&rlz=1C1ONGR_enUS1022US1022&sa=X&ved=2ahUKEwj1wY_1scf6AhUxg2oFHc_6AY4QBXoECAEQIw&biw=975&bih=764'
    driver.get(url)
    #use a SET to prevent having duplicate URLs
    image_urls=set()#use on line 30
    nextOne=0 #account for the skipping if the same image and thumbnails repeat
    
    while len(image_urls) + nextOne < limit:
         scroll(driver)
         #were they are presented togather under same class
         thumbnails = driver.find_elements(By.CLASS_NAME,"Q4LuWd")
         
         for img in thumbnails[len(image_urls) +nextOne: limit]:#limit is slice to reach the  max
            try:
                 img.click()
                 time.sleep(delay)
            except:
                continue
            #after being clicked looking up the big image, orginal to it self  
            full_images= driver.find_elements(By.CLASS_NAME,'n3VNCb')
            for image in full_images:
                #if the same image is repeating, increment it len imural,prevent inifit loop
                if image.get_attribute('src') in image_urls:
                    limit += 1
                    nextOne += 1
                    break
                
                #return only atribute declared in html, like class, tag
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    # download_image(file/,image.get_attribute('src'), 'name") possible to use for download
                    
                    print(f"Found {len(image_urls)}")
            #iterate to find proper image source if repeates, to get the source
    return image_urls
            
urls = get_images(driver,0.7,10)
print(urls)
#url is the item to be downloaded
def download_image(download_path, url, file_name):
    try:
    #http request to url
        imageContent = requests.get(url).content
        
        image_file= io.BytesIO(imageContent) #store file in memory with io
        
        image= Image.open(image_file)
        
        file_path= download_path + file_name #path to save the file
        #where the downloading occures
        with open(file_path, 'wb') as f:
            image.save(f,"JPEG")# save to f in a JPEG file
            
        print('Finished')
        driver.quit()
    except Exception as e:
        print('FAILER - ', e)
        
#uwe use enumerate becse of SET
for idx, url in enumerate(urls):
    download_image('harvesImages/',url, str(idx)+'.jpg') #harvest is the folder, idx to give them uniqe names with contatination

driver.quit()



#another way to scroll down
# from selenium.webdriver.common.keys import Keys

# down = driver.find_element(By.TAG_NAME,'html')
# down.send_keys(Keys.END)

