# Project 8 : Youtube Video Downloader

# from pytube import YouTube
#
# # link = input("Enter the link : ")
# link = "https://youtube.com/"
# youtube_1 = YouTube(link)
#
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
#
# # videos = youtube_1.streams.all()
# videos = youtube_1.streams.filter(only_audio=True)
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
#
# print()
# strm = int(input("enter:"))
# videos[strm].download()
# print("success")


# ********* Download full Playlist *********

from pytube import Playlist

py = Playlist("https://youtube.com/")

print(f'Downloading : {py.title}')

for video in py.videos():
    video.streams.first().download()