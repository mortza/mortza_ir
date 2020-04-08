from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import youtube_dl


@login_required(login_url='downloader:login')
def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def show_download_list(request):
    print("asd")
    opt = {
        'format': '360p',
        'writethumbnail': True,
        'outtmpl': 'dl/%(title)s' + '.mp4',
    }
    yt_dl = youtube_dl.YoutubeDL(opt)
    yt_dl.download([request.POST['url']])
    return redirect('/')


def login_form(request):
    if request.user is not None:
        logout(request)
    return render(request, 'login.html')


@require_http_methods(['POST'])
def do_login(request):
    if request.user is not None:
        logout(request)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('downloader:index')
    else:
        return redirect('downloader:login')
