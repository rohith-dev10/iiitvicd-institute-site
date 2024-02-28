"""inst_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from instsite import views as instsite_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",instsite_views.Home.as_view(),name="home"),
    path("about",instsite_views.about,name="about"),
    path("acad_btech",instsite_views.acad_btech,name="acad_btech"),
    path("director",instsite_views.director,name="director"),
    path("faqs",instsite_views.faqs,name="faqs"),
    path("news/<int:news_id>",instsite_views.news_det,name="news_det"),
    path("announcement/<int:anno_id>",instsite_views.anno_det,name="anno_det"),
    path("event/<int:eve_id>",instsite_views.eve_det,name="eve_det"),
    path("all_news/<int:page>",instsite_views.all_news,name="all_news"),
    path("all_anno/<int:page>",instsite_views.all_anno,name="all_anno"),
    path("all_eve/<int:page>",instsite_views.all_eve,name="all_eve"),
    path("verify_certificate",instsite_views.VerifyCertificate.as_view(),name="verify_certificate"),
]