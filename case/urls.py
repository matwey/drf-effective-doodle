from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^hello/$', ListView.as_view()),
]
