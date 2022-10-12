import urllib.request
import os

class Globals:
    num = 0

#MAKE SUPPORT path as parameter
def video_download(url,target_folder_name):
    try:
        if not os.path.exists(target_folder_name):
            os.makedirs(target_folder_name)
        urllib.request.urlretrieve(url, f"{target_folder_name}/{Globals.num}.mp3")
        Globals.num += 1

    except Exception as e:
        if e == urllib.error.HTTPError:
            print("Blob")
            # Blob to MP4
        else:
            print(e)
