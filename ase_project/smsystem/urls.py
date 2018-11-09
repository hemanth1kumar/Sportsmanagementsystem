from django.conf.urls import url,include
from django.urls import path,re_path
from . import views
urlpatterns = [
    url(r'^$',views.signin,name="login"),
    url(r'^$',views.signout,name="signout"),
    
    url(r'^studenthome/(?P<token_id>[\w\.-]+)/',views.studenthome,name="studenthome"),
    url(r'^studentdashboard/$',views.studentdashboard,name="studentdashboard"),
    url(r'^studentcomplaints/$',views.studentcomplaints,name="studentcomplaints"),
    url(r'^studentmatchresults/$',views.studentmatchresults,name="studentmatchresults"),
    url(r'^studentschedules/$',views.studentschedules,name="studentschedules"),
    url(r'^studentsettings/$',views.studentsettings,name="studentsettings"),

    

    url(r'^adminhome/$',views.adminhome,name="adminhome"),
    url(r'^adminschedules/$',views.adminschedules,name="adminschedules"),
    url(r'^admincoaches/$',views.admincoaches,name="admincoaches"),
    url(r'^adminaddcoaches/$',views.adminaddcoaches,name="adminaddcoaches"),
    url(r'^adminaddschedules/$',views.adminaddschedules,name="adminaddschedules"),
    url(r'^admingames/$',views.admingames,name="admingames"),
    url(r'^adminaddgames/$',views.adminaddgames,name="adminaddgames"),
    url(r'^adminperformance/$',views.adminperformance,name="adminperformance"),
    url(r'^adminviewperformance/$',views.adminviewperformance,name="adminviewperformance"),
    url(r'^admincomplaints/$',views.admincomplaints,name="admincomplaints"),

    url(r'^coachhome/$',views.coachhome,name="coachhome"),
    url(r'^coachschedules/$',views.coachschedules,name="coachschedules"),
    url(r'^coachaddschedules/$',views.coachaddschedules,name="coachaddschedules"),
    url(r'^coachsettings/$',views.coachsettings,name="coachsettings"),
    url(r'^coachupdatesettings/$',views.coachupdatesettings,name="coachupdatesettings"),
    url(r'^coachperformance/$',views.coachperformance,name="coachperformance"),
    url(r'^coachmatchresults/$',views.coachmatchresults,name="coachmatchresults"),
    url(r'^coachviewperformance/$',views.coachviewperformance,name="coachviewperformance"),
    url(r'^coachaddmatchresults/$',views.coachaddmatchresults,name="coachaddmatchresults"),
    url(r'^coachaddperformance/$',views.coachaddperformance,name="coachaddperformance"),
    url(r'^coachupdateperformance/$',views.coachupdateperformance,name="coachupdateperformance"),
    url(r'^coachcomplaints/$',views.coachcomplaints,name="coachcomplaints"),
    


    
]
