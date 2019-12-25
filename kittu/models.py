from django.db import models

class funday(models.Model):
	idnum=models.CharField(max_length=20)
	user=models.CharField(max_length=200)
	kittu=models.CharField(max_length=2000)
	

	def __unicode__(self):
		return self.idnum



# Create your models here.
