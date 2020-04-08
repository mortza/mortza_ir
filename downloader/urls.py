from django.urls import path
from downloader import views

app_name = 'downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_form, name='login'),
    path('do-login', views.do_login, name='do-login'),
    path('get', views.show_download_list, name='download-url')
]
