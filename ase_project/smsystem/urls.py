from django.conf.urls import url,include
from django.urls import path,re_path
from . import views
urlpatterns = [
    url(r'^$',views.signin,name="login"),
    url(r'^$',views.signout,name="signout"),
    
    url(r'^studenthome/(?P<token_id>[\w\.-]+)/',views.studenthome,name="studenthome"),
    url(r'^studentdashboard/(?P<student_id>[\w\.-]+)/',views.studentdashboard,name="studentdashboard"),
    url(r'^studentcomplaints/(?P<student_id>[\w\.-]+)/',views.studentcomplaints,name="studentcomplaints"),
    url(r'^studentmatchresults/(?P<student_id>[\w\.-]+)/',views.studentmatchresults,name="studentmatchresults"),
    url(r'^studentschedules/(?P<student_id>[\w\.-]+)/',views.studentschedules,name="studentschedules"),
    url(r'^studentsettings/(?P<student_id>[\w\.-]+)/',views.studentsettings,name="studentsettings"),

    

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

    url(r'^coachhome/(?P<coach_id>[\w\.-]+)/',views.coachhome,name="coachhome"),
    url(r'^coachschedules/(?P<coach_id>[\w\.-]+)/',views.coachschedules,name="coachschedules"),
    url(r'^coachaddschedules/(?P<coach_id>[\w\.-]+)/',views.coachaddschedules,name="coachaddschedules"),
    url(r'^coachsettings/(?P<coach_id>[\w\.-]+)/',views.coachsettings,name="coachsettings"),
    url(r'^coachupdatesettings/(?P<coach_id>[\w\.-]+)/',views.coachupdatesettings,name="coachupdatesettings"),
    url(r'^coachperformance/(?P<coach_id>[\w\.-]+)/',views.coachperformance,name="coachperformance"),
    url(r'^coachmatchresults/(?P<coach_id>[\w\.-]+)/',views.coachmatchresults,name="coachmatchresults"),
    url(r'^coachviewperformance/(?P<coach_id>[\w\.-]+)/',views.coachviewperformance,name="coachviewperformance"),
    url(r'^coachaddmatchresults/(?P<coach_id>[\w\.-]+)/',views.coachaddmatchresults,name="coachaddmatchresults"),
    url(r'^coachaddperformance/(?P<coach_id>[\w\.-]+)/',views.coachaddperformance,name="coachaddperformance"),
    url(r'^coachupdateperformance/(?P<coach_id>[\w\.-]+)/',views.coachupdateperformance,name="coachupdateperformance"),
    url(r'^coachcomplaints/(?P<coach_id>[\w\.-]+)/',views.coachcomplaints,name="coachcomplaints"),
    


    
]
