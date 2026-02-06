import pytube 
import ffmpeg 

link = input("Enter the URL")
yt = pytube.YouTube(link)
for e in yt.streams:
    print(e)

#download audio only
yt.streams.filter(abr="160kbps", progressive=False).first().download(filename="audio.mp3")
audio = ffmpeg.input("audio.mp3")

#download video only
yt.streams.filter(res="1080p", progressive=False).first().download(filename="video.mp4")
video = ffmpeg.input("video.mp4")

ffmpeg.output(audio, video, "finished_video.mp4").run(overwrite_output=True)

