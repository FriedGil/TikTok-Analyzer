import urllib.request
  
class Globals:
    num = 0

#MAKE SUPPORT path as parameter
def video_download(url,target_folder_name):
    try:
        urllib.request.urlretrieve(url, f"{target_folder_name}/{Globals.num}.mp3")
        Globals.num += 1
    except Exception as e:
        if e == urllib.error.HTTPError:
            print("Blob")
            # Blob to MP4
        else:
            print(e)
