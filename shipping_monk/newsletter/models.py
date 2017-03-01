from django.db import models

# Create your models here.
class SignUp(models.Model):
	email  = models.EmailField() 
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email

class orderDetail(models.Model):
	Name = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add = True,auto_now=False)
	Address = models.CharField(max_length=200)
	orderId = models.CharField(max_length=200)
	hubId = models.IntegerField()


class shop(models.Model):
	hname = models.CharField(max_length=20)
	hubId = models.CharField(max_length=10)
	address = models.CharField(max_length=30)
	Auth_to = models.CharField(max_length=10)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12) #validators should be a list