from django.conf.urls import url
from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

app_name = 'music'

urlpatterns = [path('',views.index,name = 'index'),
               url(r'^(?P<album_id>[0-9]+)/$',views.detail,name = 'detail'),
               url(r'^(?P<album_id>[0-9]+)/favorite$',views.favorite,name = 'favorite'),
               url(r'^(?P<album_id>[0-9]+)/unfavorite$',views.unfavorite,name = 'unfavorite'),
               ]
