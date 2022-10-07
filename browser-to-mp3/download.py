import urllib.request


def video_download(url):
    try:
        urllib.request.urlretrieve(url, "1.mp3")
    except Exception as e:
        if e == urllib.error.HTTPError:
            print("Blob")
            # Blob to MP4
        else:
            print(e)
