from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *	
import datetime
# Create your views here.
def studenthome(request):
	complaints = Complaint.objects.all().order_by('-datetime')
	announcements=Announcement.objects.all().order_by('-datetime')
	context={'complaints':complaints,'announcements':announcements}
	return render(request,'smsystem/studenthome.html',context)

def sendannouncement(request):
	print('aasdfsd')
	if request.method == 'POST':
		m_obj=Announcement()
		m_obj.receiver=request.POST['receiver']
		m_obj.sender=request.POST['sender']
		m_obj.message=request.POST['message']
		#m_obj.datetime=datetime.datetime.now()
		m_obj.save()
		print(m_obj.message)
	return render(request,'smsystem/a.html')

def studentsettings(request):
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
	tournament=Tournament.objects.all()
	context={'announcements':announcements}
	return render(request,'smsystem/studentschedules.html',context)
