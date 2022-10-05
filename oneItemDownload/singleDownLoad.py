import requests
# from bs4 import BeautifulSoup
from pytube import YouTube

python_image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

#both owrk for files and imagee NOT videos or any moving media


def download_image_in_folder(python_image_url):
    response = requests.get(python_image_url) #http response object
    with open("python_Logo.png","wb") as f:
        f.write(response.content) #this will send it to the current directory


def google_icon_different_method():
    url = 'http://google.com/favicon.ico'
    response = requests.get(url, allow_redirects=True)
    open('google.ico', 'wb').write(response.content)

#https://www.codementor.io/@aviaryan/downloading-files-from-urls-in-python-77q3bs0un

video_url= "https://www.youtube.com/watch?v=9bZkp7q19f0"

# def video_downLoad(url):
    
#     h = requests.head(url,allow_redirects=True)
#     header= h.headers

#     content_type = header.get('Content-type')
#     if 'text' in content_type.lower():
#         return False
#     if 'html' in content_type.lower():
#         return False


    # return True

def youtube_download():
    save_path = r"C:\Users\16075\Downloads\pythonDownload"

    try:
        yt = YouTube(video_url)
    except:
        print("Error: Not able to find your link")

    print(yt.title)
    print(yt.author)
    print(yt.description)

    # lst = yt.streams.filter()
    #mp4 only streeams will give audio only
    #progressive equals true contain both
    # for el in lst:
    #     print(el)
        
    highResVideo= yt.streams.filter(progressive=True).get_highest_resolution().itag

    try:#output_Path makes folder, filename to the name the file, if not placed, will download 
        #directly in the directory
        yt.streams.get_by_itag(highResVideo).download(output_path='Music Folder')
    except:
        print("Error in downloading the video")


def youtube_audio():
    save_path = r"C:\Users\16075\Downloads\pythonDownload"
    print('enter sound')
    try:
        yt = YouTube(video_url)
    except:
        print("Error: Not able to find your link")

    print(yt.title)
    print(yt.author)
    print(yt.description)
        
    videoSound= yt.streams.filter(only_audio=True).get_audio_only().itag

    try:
        yt.streams.get_by_itag(videoSound).download(output_path='sound Folder')
    except:
        print("Error in downloading the video")
    print('audio complete')
   


#test to see if everyting is installed in the right spots and works
#should get tow images, and a folder with a music video by Psy
download_image_in_folder(python_image_url)
google_icon_different_method()
youtube_download()   
   
 