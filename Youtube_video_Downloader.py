from pytube import YouTube

link = "https://youtu.be/EAYlckSaviI"
yt_1 = YouTube(link)

videos = yt_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("enter : "))
videos[strm].download()
print("Successful")    