from django.urls import path
from downloader import views

app_name = 'downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.show_download_list, name='download-url')
]
