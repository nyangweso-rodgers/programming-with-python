from pytube import YouTube
print(dir(YouTube))

DOWNLOAD_FOLDER = "/Users/HP/Downloads"
video_url = "https://www.youtube.com/watch?v=Ymkl0t0FOcw&list=RDYmkl0t0FOcw&start_radio=1"
video_obj = YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)