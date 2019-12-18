from django.db import models

# Create your models here.
class Mentors(models.Model):
	mentor_name = models.CharField(max_length=255)
	post = models.CharField(max_length=255)
	pub_date = models.DateTimeField("date published")

	def __str__(self):
		return self.mentor_name

class Courses(models.Model):
	course_name = models.CharField(max_length=255)
	course_outline = models.TextField()

	def __str__(self):
		return self.course_name

class Register(models.Model):
	student_name = models.CharField(max_length=255)
	course = models.ForeignKey(Courses, on_delete=models.CASCADE)
	fees = models.CharField(max_length=255)
	duration = models.IntegerField()
	start = models.CharField(max_length=255)
	end = models.CharField(max_length=255)
	paid = models.BooleanField(default=False)

	def __str__(self):
		return self.student_name