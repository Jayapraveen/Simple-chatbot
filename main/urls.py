from django.conf.urls import include,url
from django.contrib import admin
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from main import views
from main.views import ChatterBotApiView
from django.views.decorators.csrf import csrf_exempt


app_name = 'main'

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', csrf_exempt(views.home), name='home'),
  url(r'^api/chatterbot/', csrf_exempt(ChatterBotApiView.as_view()), name='chatterbot'),
]
