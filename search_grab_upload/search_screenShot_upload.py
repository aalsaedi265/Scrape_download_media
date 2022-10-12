from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


location_of_chromDriver= r'C:\Users\16075\Documents\work\chromedriver.exe'
driver = webdriver.Chrome(location_of_chromDriver)
driver.get('https://www.youtube.com/')

time.sleep(2)

search = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
search.send_keys('barstoo sports')
search.send_keys(Keys.ENTER)

time.sleep(4)

# down = driver.find_element(By.TAG_NAME,'html')
# down.send_keys(Keys.END)   
# time.sleep(2)
# driver.save_screenshot('screenShot_placement/youtube_screenGrab.png')

driver.quit()