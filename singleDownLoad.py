import requests
from bs4 import BeautifulSoup
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
    
archive_url = "http://www-personal.umich.edu/~csev/books/py4inf/media/"
def get_video_links():
  #create response object
    r = requests.get(archive_url)
    #create beautiful-soup object
    soup = BeautifulSoup(r.content,'html.parser')
    #find all links on web-page
    links = soup.findAll('a')
    #filter the link ending with .mp4
    video_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp4')]
    
    return video_links   
        
def download_video_series(video_links):
 
  for link in video_links:
    
   # iterate through all links in video_links
    # and download them one by one
    #obtain filename by splitting url and getting last string
    file_name = link.split('/')[-1]  
 
    print ("Downloading file:%s"%file_name)
 
    #create response object
    r = requests.get(link, stream = True)
 
    #download started
    with open(file_name, 'wb') as f:
      for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
          f.write(chunk)
 
    print ("%s downloaded!\n"%file_name)
 
  print ("All videos downloaded!")
  return
 
if __name__ == "__main__":
  #getting all video links
  video_links = get_video_links()
  download_video_series(video_links)