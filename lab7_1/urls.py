"""lab7_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from my_lab7_1.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signin/$', signin, name='signin'),
    url(r'^signin/success/$', signin_success),
    url(r'^signup/$', signup, name='signup'),
    url(r'^signup/success/$', signup_success),
    url(r'^logout/$', logout_view, name='logout')
]
