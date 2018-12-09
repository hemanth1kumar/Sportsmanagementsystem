from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *	
import requests,json
import datetime
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
#login function
def signin(request):
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
				coach_id=coach[0].coach_id
				print(coach_id)
				if coach[0].coach_password==password:
					return redirect('/coachhome/'+str(coach_id))

		#if(request.post['somename']=='Admin'):
		#	return redirect('/adminhome')

		#if(request.post['somename']=='Coach'):
		#	return redirect('/coachhome')

		#if(request.post['somename']=='Student'):
		#	return redirect('/studenthome')
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements}
	return render(request,'smsystem/login.html',context)


#signout function
def signout(request):
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'complaints':complaints,'announcements':announcements}
	return render(request,'smsystem/login.html',context)



#student details retrival function	
def studenthome(request,token_id):
	payload={'token':token_id,'secret':"f007a8547bf8019ea1742912515767008a95520292ebabcf8e8804b116f7b9df34b69045f5503cfc9e8817c15342a53df7527bc50e951815c27007e6cafdb3d8"}
	url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
	response=requests.post(url,data=payload)
	data=response.json()
	print(data)
	stu=Student.objects.all().filter(student_id=data['student'][0]['Student_ID'])
	if len(stu)!=0:
		student_id=data['student'][0]['Student_ID']
		
	else:
		student_obj=Student()
		student_obj.student_id=data['student'][0]['Student_ID']
		student_id=data['student'][0]['Student_ID']
		student_obj.first_name=data['student'][0]['Student_First_Name']
		student_obj.last_name=data['student'][0]['Student_Last_name']
		student_obj.middle_name=data['student'][0]['Student_Middle_Name']
		student_obj.gender=data['student'][0]['Student_Gender']
		student_obj.email=data['student'][0]['Student_Email']
		student_obj.current_year=data['student'][0]['Student_Cur_YearofStudy']
		student_obj.save()

	return redirect('/studentdashboard/'+student_id)
	
#student dashboard function
def studentdashboard(request,student_id):
	student=Student.objects.filter(student_id=student_id)
	performances=Performance.objects.filter(student=student[0])
	totalscore=0
	if len(performances)!=0:
		for x in performances:
			totalscore=totalscore+x.performance_score
		totalscore=totalscore/len(performances)
	else:
		totalscore=1
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'performances':performances,'student':student[0],'totalscore':totalscore}
	return render(request,'smsystem/studenthome.html',context)




#studentsettings function
def studentsettings(request,student_id):
	student=Student.objects.filter(student_id=student_id)
	if request.method == 'POST':
		sport1=request.POST['sport1']
		sport2=request.POST['sport2']
		sport3=request.POST['sport3']
		sport4=request.POST['sport4']
		if sport1!='':
			player=Player()
			sport_obj=Sport.objects.filter(sport_name=sport1)
			player.student=student[0]
			player.sport=sport_obj[0]
			player.save()
		if sport2!='':
			player=Player()
			sport_obj=Sport.objects.filter(sport_name=sport2)
			player.student=student[0]
			player.sport=sport_obj[0]
			player.save()
		if sport3!='':
			player=Player()
			sport_obj=Sport.objects.filter(sport_name=sport3)
			player.student=student[0]
			player.sport=sport_obj[0]
			player.save()
		if sport4!='':
			player=Player()
			sport_obj=Sport.objects.filter(sport_name=sport4)
			player.student=student[0]
			player.sport=sport_obj[0]
			player.save()
	game1=''
	game2=''
	game3=''
	game4=''
	player=Player.objects.filter(student=student[0])
	if len(player)>=4:
		game1=player[0].sport.sport_name
		game2=player[1].sport.sport_name
		game3=player[2].sport.sport_name
		game4=player[3].sport.sport_name
	elif len(player)>=3:
		game1=player[0].sport.sport_name
		game2=player[1].sport.sport_name
		game3=player[2].sport.sport_name
	elif len(player)>=2:
		game1=player[0].sport.sport_name
		game2=player[1].sport.sport_name
		
	elif len(player)>=1:
		game1=player[0].sport.sport_name

	print(game1,game2)
	sports=Sport.objects.all()
	student=Student.objects.filter(student_id=student_id)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'student':student[0],'sports':sports,'game1':game1}
	return render(request,'smsystem/studentsettings.html',context)


#student sending complaints
def studentcomplaints(request,student_id):
	if request.method == 'POST':
		m_obj=Complaint()
		student_obj=Student.objects.filter(student_id=student_id)
		m_obj.student=student_obj[0]
		m_obj.about=request.POST['about']
		m_obj.created_by=student_obj[0].first_name
		m_obj.save()
	student=Student.objects.filter(student_id=student_id)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'student':student[0]}
	return render(request,'smsystem/studentcomplaints.html',context)


#students matchresults viewing 
def studentmatchresults(request,student_id):
	order="A"
	schedules=Schedule.objects.all().order_by('-datetime')
	if request.method=='POST':
		order=request.POST['order']
		print(order)
		if order=='A':
			schedules=Schedule.objects.all().order_by('-datetime')
			order='D'
		else:
			schedules=Schedule.objects.all().order_by('datetime')
			order='A'
	announcements=Announcement.objects.all().order_by('-datetime')
	student=Student.objects.filter(student_id=student_id)
	sched=schedules.order_by('datetime')
	print(sched)
	
	context={'announcements':announcements,'schedules':schedules,'student':student[0],'order':order}
	return render(request,'smsystem/studentmatchresults.html',context)

#students schedules viewing
def studentschedules(request,student_id):
	schedules=Schedule.objects.all().order_by('-datetime')
	announcements=Announcement.objects.all().order_by('-datetime')
	student=Student.objects.filter(student_id=student_id)
	context={'announcements':announcements,'schedules':schedules,'student':student[0]}
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

@staff_member_required(login_url='/')  
@login_required(login_url='/')
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

#admin addschedules
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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

#admin add coaches function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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


#admin view coaches function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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


#admin view coaches function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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

#admin add games function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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

#admin viewperforamnce function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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

#admin filtering the performances function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
def adminviewperformance(request):
	if request.method == 'POST':
		game=request.POST['sportname']
		sport=Sport.objects.filter(sport_name=game)
		performances=Performance.objects.filter(sport=sport[0])
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'performances':performances,'sports':sports}
	return render(request,'smsystem/adminperformance.html',context)


#admin viewing complaints function
@staff_member_required(login_url='/')  
@login_required(login_url='/')
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












#coach howe function
def coachhome(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	coach=Coach.objects.filter(coach_id=coach_id)
	sport=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().filter(sport=sport[0])
	context={'announcements':announcements,'schedules':schedules,'coach':coach[0]}
	return render(request,'smsystem/coachhome.html',context)

#coach make schedules function
def coachschedules(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'schedules':schedules,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachschedules.html',context)

#coach add schedules function
def coachaddschedules(request,coach_id):
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
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'schedules':schedules,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachschedules.html',context)

#coach complaints viewing function
def coachcomplaints(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	complaints=Complaint.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	context={'announcements':announcements,'complaints':complaints,'coach':coach[0]}
	return render(request,'smsystem/coachcomplaints.html',context)

#coach settings function
def coachsettings(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	coach=Coach.objects.filter(coach_id=coach_id)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'coach':coach[0]}
	return render(request,'smsystem/coachsettings.html',context)
#coach update setting function
def coachupdatesettings(request,coach_id):
	message='sucessfully updated'
	if request.method == 'POST':
		coach_obj=Coach.objects.all()
		print(coach_id)
		for x in coach_obj:
			if x.coach_id==int(coach_id):
				x.coach_name=request.POST['name']
				x.experience=request.POST['experience']
				print (request.POST['experience'])
				x.contact=request.POST['contact']
				password1=request.POST['password1']
				password2=request.POST['password2']
				if (password2!='' and password1!='') or (password2=='' and password1!='') or (password2!='' and password1=='') :
					if password1==password2:
						x.coach_password=password1
				
					else:
						message='passwords does not match'
				else:
					message='details has been updated'
				x.save()

	coach=Coach.objects.filter(coach_id=coach_id)
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'announcements':announcements,'coach':coach[0],'message':message}
	return render(request,'smsystem/coachsettings.html',context)



#coach match results viewing function
def coachmatchresults(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	schedules=Schedule.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'schedules':schedules,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachmatchresults.html',context)


#coach adding match results functions
def coachaddmatchresults(request,coach_id):
	schedules=Schedule.objects.all().order_by('-datetime')
	if request.method == 'POST':
		result=request.POST['result']
		matchid=request.POST['matchid']
		sportname=request.POST['sportname']
		for x in schedules:
			print(x.datetime)
			if(x.sport.sport_name==sportname and x.schedule_id==int(matchid)):
				x.result=result
				x.save()
				
	announcements=Announcement.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'schedules':schedules,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachmatchresults.html',context)	

#coach performance viewing function
def coachperformance(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	sports=Sport.objects.all()
	announcements=Announcement.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	performances=Performance.objects.filter(sport=sports[0])
	context={'announcements':announcements,'performances':performances,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachperformance.html',context)
#coach filering performace function
def coachviewperformance(request,coach_id):
	if request.method == 'POST':
		game=request.POST['sportname']
		sport=Sport.objects.filter(sport_name=game)
		performances=Performance.objects.filter(sport=sport[0])
	
	announcements=Announcement.objects.all().order_by('-datetime')
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'performances':performances,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachperformance.html',context)

#coachupdate performance function
def coachupdateperformance(request,coach_id):
	if request.method == 'POST':
		m_obj=Announcement()	
		coach=Coach.objects.filter(coach_id=coach_id)
		m_obj.sender=coach[0].coach_name
		m_obj.message=request.POST['message']
		m_obj.save()
		print(m_obj.message)
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all()
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'performances':performances,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachupdateperformance.html',context)


#coach addperformance
def coachaddperformance(request,coach_id):
	if request.method == 'POST':
		p_obj=Performance()
		s_id=request.POST['studentid']
		sport_name=request.POST['sportname']
		print(s_id)
		student_obj=Student.objects.filter(student_id=s_id)
		sport_obj=Sport.objects.filter(sport_name=sport_name)
		p_obj.sport=sport_obj[0]
		p_obj.student=student_obj[0]
		p_obj.role=request.POST['role']
		p_obj.performance_score=request.POST['performance']
		coach_obj=Coach.objects.filter(coach_id=coach_id)
		p_obj.created_by=coach_obj[0].coach_name
		p_obj.save()
	announcements=Announcement.objects.all().order_by('-datetime')
	performances=Performance.objects.all()
	coach=Coach.objects.filter(coach_id=coach_id)
	sports=Sport.objects.filter(sport_name=coach[0].sport.sport_name)
	context={'announcements':announcements,'performances':performances,'sports':sports,'coach':coach[0]}
	return render(request,'smsystem/coachupdateperformance.html',context)


def error_404(request):
	return render(request,'smsystem/404.html')

def error_500(request):
	return render(request,'smsystem/500.html')