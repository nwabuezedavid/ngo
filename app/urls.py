from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("service/",service, name="service"),
    path("contact/",contact, name="contact"),
    path("donate/",donate, name="donate"),
    path("partner/",partner, name="partner"),
    path("pastjob/",pastjob, name="pastjob"),
    path("jobdetail/",jobdetail, name="jobdetail"),
    path("press/",press, name="press"),
    path("newdetail/<pk>/",newdetail, name="newdetail"),
    path("ourteam/",ourteam, name="ourteam"),
    path("newstory/",newstory, name="newstory"),
    path("project/",project, name="project"),
    path("projectupdate/",projectupdate, name="projectupdate"),
    path("publications/",publications, name="publications"),
    path("report/",report, name="report"),
    path("traning/",traning, name="traning"),
    path("siteclinic/",siteclinic, name="siteclinic"),
    path("projectupdate/",projectupdate, name="projectupdate"),
]