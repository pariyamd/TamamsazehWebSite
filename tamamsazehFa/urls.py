"""Tamamsazeh-WebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from tamamsazehFa.views import *
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from tamamsazeh.models import Article

urlpatterns = [
    path('projects/', projects),
    path('projectView/<int:id>', projectView),
    path('main_page/', main_page),
    path('base/', base),
    path('certifications/<int:num>', certifications),
    path('certifications/', certificationsNon),
    path('aboutus/', aboutus),
    path('crew/', crew),
    path('article/', article),
    path('articleView/<path:link>', articleView),
    path('blog/', blog),
    path('',main_page)
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
