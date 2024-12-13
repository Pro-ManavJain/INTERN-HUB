import yt_dlp

def video_downloader():
    try:
        URL = input("Enter URL of YouTube video: ")
        #Downloading video at highest resolution
        ydl_opts = {
            "format": "best",
            "outtmpl": "%(title)s.%(ext)s",
        }

        #Downloading video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading your video.......")
            ydl.download([URL])
            print("Your video is Downloaded Successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

video_downloader()