from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import youtube_dl


# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def show_download_list(request):
    print("asd")
    opt = {
        'format': '360p',
        'writethumbnail': True,
        'outtmpl': 'dl/%(title)s' + '.mp4',
    }
    yt_dl = youtube_dl.YoutubeDL(opt)
    yt_dl.download([request.POST['url']])
    resp = redirect('/')
    return resp
