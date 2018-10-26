from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^studenthome/$',views.studenthome,name="studenthome"),
    url(r'^studentcomplaints/$',views.studentcomplaints,name="studentcomplaints"),
    url(r'^studentmatchresults/$',views.studentmatchresults,name="studentmatchresults"),
    url(r'^studentschedules/$',views.studentschedules,name="studentschedules"),
    url(r'^studentsettings/$',views.studentsettings,name="studentsettings"),
    url(r'^sendannouncement/$',views.sendannouncement,name="sendannouncement"),
]
