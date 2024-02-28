from django.shortcuts import render
from django.views.generic import View
from .models import *

import math

num=1

class Home(View):

    def get(self, request, *args, **kwargs):
        newss=News.objects.order_by('-date')[:4]
        news=newss[0]
        newss=newss[1:]
        anno=Announcements.objects.order_by('-date')[:3]
        eve=Events.objects.order_by('-date')[:4]

        context={
            "news": news,
            "newss":newss,
            "anno":anno,
            "eve":eve,
        }
        return render(request,"instsite/home.html",context)

    def post(self, request, *args, **kwargs): 
        pass

class VerifyCertificate(View):

    def get(self,request):
        return render(request,"instsite/verify_certificate.html")
        
    def post(self,request):
        hash_r=str(request.body).split('&')[1].split("=")[1].replace("'","")
        context={
            "hash":hash_r,
        }
        try:
            Hashes.objects.get(hash=hash_r)
            context["success"]=1
        except:
            context["success"]=0
        return render(request,"instsite/certificate.html",context)

def about(request):
    context={}
    return render(request,"instsite/about.html",context)
def director(request):
    context={}
    return render(request,"instsite/director.html",context)
def acad_btech(request):
    context={}
    return render(request,"instsite/acad_btech.html",context)
def faqs(request):
    context={}
    return render(request,"instsite/faqs.html",context)

def news_det(request,news_id):
    newss=News.objects.all()
    for i in newss:
        if(i.id==news_id):
            newss=i
            break
    context={
        "news_id":news_id,
        "newss":newss,
    }
    return render(request,"instsite/news_det.html",context)

def anno_det(request,anno_id):
    annos=Announcements.objects.all()
    for i in annos:
        if(i.id==anno_id):
            annos=i
            break
    context={
        "anno_id":anno_id,
        "annos":annos,
    }
    return render(request,"instsite/anno_det.html",context)

def eve_det(request,eve_id):
    eves=Events.objects.all()
    for i in eves:
        if(i.id==eve_id):
            eves=i
            break
    context={
        "eve_id":eve_id,
        "eves":eves,
    }
    return render(request,"instsite/eve_det.html",context)

def all_news(request,page=0):
    # num=2
    no_news=len(News.objects.all())
    no_pages=int(math.ceil(no_news/num))
    newss=News.objects.order_by('-date')[page*num:num+page*num]
    context={
        "no_news":no_news,
        "newss":newss,
        "no_pages":no_pages,        
        "page":page,
    }
    return render(request,"instsite/all_news.html",context)

def all_anno(request,page=0):
    # num=2
    no_anno=len(Announcements.objects.all())
    no_pages=int(math.ceil(no_anno/num))
    annos=Announcements.objects.order_by('-date')[page*num:num+page*num]
    context={
        "no_anno":no_anno,
        "annos":annos,
        "no_pages":no_pages,        
        "page":page,
    }
    return render(request,"instsite/all_anno.html",context)

def all_eve(request,page=0):
    # num=2
    no_eve=len(Events.objects.all())
    no_pages=int(math.ceil(no_eve/num))
    eves=Events.objects.order_by('-date')[page*num:num+page*num]
    context={
        "no_eve":no_eve,
        "eves":eves,
        "no_pages":no_pages,        
        "page":page,
    }
    return render(request,"instsite/all_eve.html",context)