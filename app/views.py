from django.shortcuts import render
from .models import * 
# Create your views here.
def home(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all() ,
     
     "home": homepage.objects.get(idx=1)   ,
     
    }
    return render(request, "home.html", conx)
def about(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "about.html", conx)
def service(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "service.html", conx)
def contact(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "contact.html", conx)
def donate(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "donate.html", conx)
def partner(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "partner.html", conx)
def pastjob(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "job": job.objects.all()   ,
        
    }
    return render(request, "pastjob.html", conx)
def press(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "press.html", conx)
def siteclinic(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "siteclinic.html", conx)
def ourteam(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "teams": teams.objects.all()   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "ourteam.html", conx)
def newdetail(request,pk):
    
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "item": news.objects.get(uuids=pk),
        
    }
    return render(request, "newdetail.html", conx)
def newstory(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "news": news.objects.all(),
        
    }
    return render(request, "newstory.html", conx)
def project(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "projects.html", conx)
def jobdetail(request,pk):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "item": job.objects.get(uuids = pk)   ,
        
    }
    return render(request, "jobdetail.html", conx)
def projectupdate(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "projectupdate.html", conx)
def publications(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "publications.html", conx)
def report(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
    "report": reportx.objects.all()   ,
        
    }
    return render(request, "report.html", conx)
def traning(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "traning.html", conx)
def projectupdate(request):
    conx={
    "site": siteedit.objects.get(idx=1)   ,
    "news": news.objects.all()   ,
        
    }
    return render(request, "projectupdate.html", conx)