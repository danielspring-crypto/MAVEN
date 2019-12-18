from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='post')
	date_posted = models.DateTimeField("date published")
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title