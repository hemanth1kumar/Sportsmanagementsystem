from django.db import models
from django.utils import timezone

#student model
class Student(models.Model):
	student_id=models.CharField(primary_key=True,max_length=255)
	first_name=models.CharField(max_length=50,default='')
	middle_name=models.CharField(max_length=50,default='')
	last_name=models.CharField(max_length=50,default='')
	gender=models.CharField(max_length=1,default='m')
	current_year=models.CharField(max_length=3)
	email=models.EmailField(default='')
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return self.student_id


#sportmodel
class Sport(models.Model):
	sport_id=models.AutoField(primary_key=True)
	sport_name=models.CharField(max_length=50)
	equipment=models.CharField(max_length=50)
	category=models.CharField(max_length=50)
	no_of_players=models.IntegerField(default=0)
	no_of_coaches=models.IntegerField(default=0)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.sport_id)


#coach model
class Coach(models.Model):
	coach_id=models.AutoField(primary_key=True)
	coach_password=models.CharField(max_length=50,default='iiitscoach')
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	coach_name=models.CharField(max_length=50)
	coach_type=models.CharField(max_length=50)
	experience=models.IntegerField(default=0)
	contact=models.CharField(max_length=20)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.coach_id)

#player model
class Player(models.Model):
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return str(self.id)

#performance model
class Performance(models.Model):
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	role=models.CharField(max_length=50)
	performance_score=models.IntegerField()
	datetime=models.DateTimeField(auto_now_add=True)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.sport_id)+':'+self.student_id

#tournament model
class Tournament(models.Model):
	tournament_id=models.AutoField(primary_key=True)
	tournament_name=models.CharField(max_length=50)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()
	level=models.CharField(max_length=50)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	
	def __str__(self):
		return str(self.tournament_id)

#complaint model
class Complaint(models.Model):
	complaint_id=models.AutoField(primary_key=True)
	student=models.ForeignKey(Student,on_delete=models.SET_NULL, null=True)
	about=models.CharField(max_length=500)
	status=models.IntegerField(default=0)
	datetime=models.DateTimeField(auto_now_add=True)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.complaint_id)

#announcement model
class Announcement(models.Model):
	announcement_id=models.AutoField(primary_key=True)
	sender=models.CharField(max_length=50)
	message=models.CharField(max_length=500)
	datetime=models.DateTimeField(auto_now_add=True)
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.announcement_id)

#schedule model
class Schedule(models.Model):
	schedule_id=models.AutoField(primary_key=True)
	sport=models.ForeignKey(Sport,on_delete=models.SET_NULL, null=True)
	venue=models.CharField(max_length=50,default='')
	result=models.CharField(max_length=50,null=True)
	opponent_1=models.CharField(max_length=50)
	opponent_2=models.CharField(max_length=50)
	datetime=models.DateTimeField(default=timezone.now)	
	created_by=models.CharField(max_length=50,default='')
	created_at=models.DateTimeField(auto_now_add=True,null=True)
	modified_by=models.CharField(max_length=50,default='')
	modified_at=models.CharField(max_length=50,default='')
	def __str__(self):
		return str(self.schedule_id)
