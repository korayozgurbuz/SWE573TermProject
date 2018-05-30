from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.bot_detector, name='bot_detector')
]