from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *	
import datetime
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
global_coachid=0
def signin(request):
	global global_coachid
	if request.method == 'POST':
		username=request.POST['username']
		password = request.POST['password']

		print(username,password)
		user = authenticate(username = username,password = password)
		if user is not None:
			if user.is_active:
				login(request,user)
				if(user.is_staff):
					return redirect('/adminhome')
				else:
					return redirect('/studenthome')
			else:
				return render(request,'smsystem/login.html')
		else:
			coach=Coach.objects.all().filter(coach_name=username)
			if len(coach)!=0:
				global_coachid=coach[0].coach_id
				print(global_coachid)
				if coach[0].coach_password==password:
					return redirect('/coachhome')

		#if(request.post['somename']=='Admin'):
		#	return redirect('/adminhome')

		#if(request.post['somename']=='Coach'):
		#	return redirect('/coachhome')

		#if(request.post['somename']=='Student'):
		#	return redirect('/studenthome')
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements}
	return render(request,'smsystem/login.html',context)
def signout(request):
	global global_coachid
	global_coachid=0
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'complaints':complaints,'announcements':announcements}
	return render(request,'smsystem/login.html',context)

	
def studenthome(request):
	complaints = Complaint.objects.all().order_by('-datetime')
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'complaints':complaints,'announcements':announcements}
	return render(request,'smsystem/studenthome.html',context)



def studentsettings(request):
	student=Student.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements}
	return render(request,'smsystem/studentsettings.html',context)

def studentcomplaints(request):
	if request.method == 'POST':
		m_obj=Complaint()
		m_obj.about=request.POST['about']
		m_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements}
	return render(request,'smsystem/studentcomplaints.html',context)
def studentmatchresults(request):
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	context={'announcements':announcements,'schedules':schedules}
	return render(request,'smsystem/studentmatchresults.html',context)
def studentschedules(request):
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	context={'announcements':announcements,'schedules':schedules}
	return render(request,'smsystem/studentschedules.html',context)




@staff_member_required(login_url='/')  
@login_required(login_url='/')
def adminhome(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	context={'announcements':announcements,'schedules':schedules}
	return render(request,'smsystem/adminhome.html',context)

def adminschedules(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/adminschedules.html',context)

def adminaddschedules(request):
	if request.method == 'POST':
		schedule_obj=Schedule()
		sport_name=request.POST['sportname']
		sport_obj=Sport.objects.filter(sport_name=sport_name)
		schedule_obj.sport=sport_obj[0]
		schedule_obj.datetime=request.POST['datetime']
		schedule_obj.opponent_1=request.POST['opponent_1']
		schedule_obj.opponent_2=request.POST['opponent_2']
		schedule_obj.venue=request.POST['venue']
		schedule_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	schedules=Schedule.objects.all().order_by('-datetime')
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/adminschedules.html',context)


def adminaddcoaches(request):
	sports = Sport.objects.all()
	if request.method == 'POST':
		m_obj=Coach()
		m_obj.coach_name=request.POST['name']	
		sport_name=request.POST['sport']	
		sport_obj=Sport.objects.filter(sport_name=sport_name)
		m_obj.sport=sport_obj[0]
		m_obj.experience=request.POST['experience']
		m_obj.coach_type=request.POST['type']
		m_obj.contact=request.POST['contact']
		for x in sports:
			if(x.sport_name==sport_name):
				x.no_of_coaches = x.no_of_coaches+1
				x.save()
		m_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	coaches=Coach.objects.all()
	context={'announcements':announcements,'coaches':coaches}
	return render(request,'smsystem/admincoaches.html',context)

def admincoaches(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	coaches=Coach.objects.all()
	sports=Sport.objects.all()
	context={'announcements':announcements,'coaches':coaches,'sports':sports}
	return render(request,'smsystem/admincoaches.html',context)


def admingames(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	coaches=Coach.objects.all()
	context={'announcements':announcements,'sports':sports,'coaches':coaches}
	return render(request,'smsystem/admingames.html',context)

def adminaddgames(request):
	if request.method == 'POST':
		sport_obj=Sport()
		sport_obj.sport_name=request.POST['sport_name']
		sport_obj.equipment=request.POST['equipment']
		sport_obj.category=request.POST['category']
		sport_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	coaches=Coach.objects.all()
	context={'announcements':announcements,'sports':sports,'coaches':coaches}
	return render(request,'smsystem/admingames.html',context)
def adminperformance(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all().order_by('-performance_score')
	context={'announcements':announcements,'performances':performances,'sports':sports}
	return render(request,'smsystem/adminperformance.html',context)

def adminviewperformance(request):
	if request.method == 'POST':
		game=request.POST['sportname']
		sport=Sport.objects.filter(sport_name=game)
		performances=Performance.objects.filter(sport=sport[0])
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'performances':performances,'sports':sports}
	return render(request,'smsystem/adminperformance.html',context)


def admincomplaints(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	complaints=Complaint.objects.all().order_by('-datetime')
	for x in complaints:
		if(x.status!=1):
			x.status='pending'
	context={'announcements':announcements,'complaints':complaints}
	return render(request,'smsystem/admincomplaints.html',context)

def adminsettings(request):
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.sender='admin'
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements}
	return render(request,'smsystem/adminsettings.html',context)












def coachhome(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	context={'announcements':announcements,'schedules':schedules}
	return render(request,'smsystem/coachhome.html',context)

def coachschedules(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/coachschedules.html',context)


def coachaddschedules(request):
	if request.method == 'POST':
		schedule_obj=Schedule()
		sport_name=request.POST['sportname']
		sport_obj=Sport.objects.filter(sport_name=sport_name)
		schedule_obj.sport=sport_obj[0]
		schedule_obj.datetime=request.POST['datetime']
		schedule_obj.opponent_1=request.POST['opponent_1']
		schedule_obj.opponent_2=request.POST['opponent_2']
		schedule_obj.venue=request.POST['venue']
		schedule_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/coachschedules.html',context)

def coachcomplaints(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	complaints=Complaint.objects.all().order_by('-datetime')
	for x in complaints:
		if(x.status!=1):
			x.status='pending'
		else:
			x.status='completed '
	context={'announcements':announcements,'complaints':complaints}
	return render(request,'smsystem/coachcomplaints.html',context)

def coachsettings(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	coach=Coach.objects.filter(coach_id=global_coachid)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'coachdetails':coach[0]}
	return render(request,'smsystem/coachsettings.html',context)

def coachupdatesettings(request):
	global global_coachid
	message='sucessfully updated'
	if request.method == 'POST':
		coach_obj=Coach.objects.all()
		for x in coach_obj:
			if x.coach_id==global_coachid:
				x.coach_name=request.POST['name']
				x.experience=request.POST['experience']
				x.contact=request.POST['contact']
				password1=request.POST['password1']
				password2=request.POST['password2']
				if password2!=None and password1!=None:
					if password1==password2:
						x.coach_password=password1
				
					else:
						message='passwords does not match'
				else:
					message='password does not match'
				x.save()

	coach=Coach.objects.filter(coach_id=global_coachid)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'coachdetails':coach[0],'message':message}
	return render(request,'smsystem/coachsettings.html',context)

def coachmatchresults(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/coachmatchresults.html',context)

def coachaddmatchresults(request):
	schedules=Schedule.objects.all().order_by('-datetime')
	if request.method == 'POST':
		result=request.POST['result']
		team1=request.POST['team1']
		team2=request.POST['team2']
		sportname=request.POST['sportname']
		for x in schedules:
			print(x.datetime)
			if(x.sport.sport_name==sportname and x.opponent_1==team1 and x.opponent_2==team2):
				x.result=result
				x.save()
				
	announcements=Announcement.objects.all().order_by('-datetime')
	sports=Sport.objects.all()
	context={'announcements':announcements,'schedules':schedules,'sports':sports}
	return render(request,'smsystem/coachmatchresults.html',context)	

def coachperformance(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all()
	context={'announcements':announcements,'performances':performances,'sports':sports}
	return render(request,'smsystem/coachperformance.html',context)

def coachviewperformance(request):
	if request.method == 'POST':
		game=request.POST['sportname']
		sport=Sport.objects.filter(sport_name=game)
		performances=Performance.objects.filter(sport=sport[0])
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'performances':performances,'sports':sports}
	return render(request,'smsystem/coachperformance.html',context)

def coachupdateperformance(request):
	global global_coachid
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=global_coachid)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all()
	context={'announcements':announcements,'performances':performances}
	return render(request,'smsystem/coachupdateperformance.html',context)

def coachaddperformance(request):
	if request.method == 'POST':
		p_obj=Performance()
		s_id=request.POST['studentid']
		sport_name=request.POST['sportname']
		student_obj=Student.objects.filter(student_id=s_id)
		sport_obj=Sport.objects.filter(sport_name=sport_name)
		p_obj.sport=sport_obj[0]
		p_obj.student=student_obj[0]
		p_obj.role=request.POST['role']
		p_obj.performance_score=request.POST['performance']
		p_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all()
	context={'announcements':announcements,'performances':performances}
	return render(request,'smsystem/coachupdateperformance.html',context)