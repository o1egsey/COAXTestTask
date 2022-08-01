"""
You are working on a project for TikTok. The future project will be a web-site of all public GIF images.
You need to write a function that converts TikTok video to GIF. The input parameter is url address of TikTok video,
i.e. "TikTok example". The output parameter is path to GIF image, i.e. "/home/user/TikTok-example-1.gif".
"""
import os.path
import requests
from moviepy.editor import VideoFileClip


def convertVideoToGIF(url):
    chunk_size = 256
    r = requests.get(url, stream=True)
    with open('tikTok.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

    clip = VideoFileClip('tikTok.mp4')
    clip.write_gif('tikTok.gif')

    path = os.path.abspath('tikTok.gif')

    return path


convertVideoToGIF('https://v16-webapp.tiktok.com/5fcfd55d15113f4496c3048d3a2f31bc/62e835d6/video/tos/useast2a/tos-useast2a-ve-0068c003/10dc97771396494f9fb8ee304afa1909/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2516&bt=1258&btag=80000&cs=0&ds=3&ft=ar5S8qT2mo0PDFStVuaQ9BeJzObpkV1PCo&mime_type=video_mp4&qs=0&rc=ODw4OjQ7ZjY1OmY8Njw4ZEBpMzc3NTk6ZjlzZDMzNzczM0A0M18tYy1gNl4xNi5fNmM2YSNiXmowcjQwZWxgLS1kMTZzcw%3D%3D&l=202208011420580101920432340E359601')