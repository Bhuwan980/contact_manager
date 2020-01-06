from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=40)
	phone = models.IntegerField()
	info = models.TextField(max_length = 200, blank=True)
	email = models.EmailField(blank=True)
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to="images/",blank=True)
	gender = models.TextField(max_length = 40,choices=(('male','Male'),('female','Female')))

	def __str__(self):
		return self.name


