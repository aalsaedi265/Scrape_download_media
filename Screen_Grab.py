from selenium import webdriver
import time

location_of_chromDriver= r'C:\Users\16075\Documents\work\chromedriver.exe'
driver = webdriver.Chrome(location_of_chromDriver) #if in dir, no need to spefilcy location

driver.get('https://www.gamingbible.co.uk/cdn-cgi/image/width=720,quality=70,format=jpeg,fit=pad,dpr=1/https%3A%2F%2Fs3-images.gamingbible.co.uk%2Fs3%2Fcontent%2F6ccf97f95ff4b02ba816d6832fbd90db.png')

time.sleep(2)

driver.save_screenshot('oneItemDownload/screenShot_target/keanu_plays_johnney.png')

#scroll, click, inpute, grab, dqonload, upload.

driver.quit()