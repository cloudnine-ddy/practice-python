# This is using pytube, but once YouTube changes something, it doesn't work anymore

# from pytube import YouTube

# video_url = input("\nPlease insert the video URL that you would like to download: ")

# try:
#     print("Analysing video......")
#     yt = YouTube(video_url)

#     print(f"\nVideo Title : {yt.title}")
#     print(f"\nVideo Length: {yt.length} s")

#     stream = yt.streams.get_highest_resolution()

#     print("\nVideo downloading......")
#     stream.download()
#     print("\nVideo downloaded! Check your folder!")

# except Exception as e:
#     print("\nSomething went wrong......")
#     print(f"\nreason: \n{e}")





# This is another method using yt_dlp, 
# it's the most powerful version of YouTube Video Downloaderfor now

import yt_dlp

video_url = input("\nPlease insert the video URL that you would like to download: ")

ydl_opts = {
    'format'    : 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl'   : '%(title)s.%(ext)s',
}

try:
    print("Analysing video......")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print("\nVideo downloaded! Check your folder!")

except Exception as e:
    print("\nSomething went wrong......")
    print(f"\nreason: \n{e}")
