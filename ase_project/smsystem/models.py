from django.db import models
from django.utils import timezone
class Student(models.Model):
	student_id=models.CharField(primary_key=True,max_length=20)
	roll_no=models.CharField(max_length=15,default='')
	first_name=models.CharField(max_length=50,default='')
	middle_name=models.CharField(max_length=50,default='')
	last_name=models.CharField(max_length=50,default='')
	regis_year=models.IntegerField(default='2016')
	gender=models.CharField(max_length=1,default='m')
	curr_year=models.IntegerField(default=3)
	regis_deg=models.CharField(max_length=20,default='B.Tech')
	regis_deg_dur=models.IntegerField(default=3)
	curr_sem=models.IntegerField(default=7)
	blood_grp=models.CharField(max_length=20,default='B-')
	email=models.EmailField(default='example@iiits.in')
	def __str__(self):
		return self.roll_no


class Sport(models.Model):
	sport_id=models.AutoField(primary_key=True)
	sport_name=models.CharField(max_length=50)
	equipment=models.CharField(max_length=50)
	category=models.CharField(max_length=50)
	no_of_players=models.IntegerField(default=0)
	def __str__(self):
		return str(self.sport_id)

class Coach(models.Model):
	coach_id=models.AutoField(primary_key=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	coach_name=models.CharField(max_length=50)
	coach_type=models.CharField(max_length=50)
	experience=models.IntegerField(default=0)
	contact=models.CharField(max_length=20)
	def __str__(self):
		return str(self.coach_id)
class Player(models.Model):
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return str(self.id)
class Performance(models.Model):
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	role=models.CharField(max_length=50)
	performance_score=models.IntegerField()
	datetime=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.sport_id)+self.student_id


class Tournament(models.Model):
	tournament_id=models.AutoField(primary_key=True)
	tournament_name=models.CharField(max_length=50)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()
	level=models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.tournament_id)


class Complaint(models.Model):
	complaint_id=models.AutoField(primary_key=True)
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	about=models.CharField(max_length=500)
	status=models.IntegerField(default=0)
	datetime=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.complaint_id)

class Announcement(models.Model):
	announcement_id=models.AutoField(primary_key=True)
	receiver=models.CharField(max_length=50)
	sender=models.CharField(max_length=50)
	message=models.CharField(max_length=500)
	datetime=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.announcement_id)

class Schedule(models.Model):
	schedule_id=models.AutoField(primary_key=True,default='')
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	tournament=models.ForeignKey(Tournament,on_delete=models.SET_NULL, null=True)
	venue=models.CharField(max_length=50,default='iiits')
	result=models.CharField(max_length=50,null=True)
	opponent_1=models.CharField(max_length=50)
	opponent_2=models.CharField(max_length=50)
	datetime=models.DateTimeField(default=timezone.now)	
	def __str__(self):
		return str(self.id)
