import urllib.request
  
class Num:
    num = 0

#MAKE SUPPORT path as parameter
def video_download(url):
    try:
        urllib.request.urlretrieve(url, f"audio/{Num.num}.mp3")
        Num.num += 1
    except Exception as e:
        if e == urllib.error.HTTPError:
            print("Blob")
            # Blob to MP4
        else:
            print(e)
