from django.db import models
from django.contrib.auth.models import User


class Waifu(models.Model):

	user = models.ForeignKey(User, default=0)
	name = models.CharField(max_length=120, unique=True)
	series = models.CharField(max_length=120)
	rating = models.CharField(max_length=25)
	height = models.DecimalField(max_digits=6, decimal_places=0)
	waifu_of_the_month = models.BooleanField(default=False)
	image = models.ImageField(upload_to='waifu_images', default='waifu_images/default.png')
	hearts = models.IntegerField(default=0)

	def __str__(self):
		return self.name
