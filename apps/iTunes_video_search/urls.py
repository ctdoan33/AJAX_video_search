from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.index),
    url(r'^main/get_movie$', views.get_movie),
]