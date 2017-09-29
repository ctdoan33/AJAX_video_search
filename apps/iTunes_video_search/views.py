# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
import requests

def index(request):
    return render(request, "iTunes_video_search/index.html")
def get_movie(request):
    artist = request.POST['user_input'].replace(' ', '')
    url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
    response = requests.get(url).content
    return HttpResponse(response, content_type='application/json')