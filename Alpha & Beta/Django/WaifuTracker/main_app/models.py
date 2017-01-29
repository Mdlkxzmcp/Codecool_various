from django.db import models


class Waifu(models.Model):

	name = models.CharField(max_length=120)
	series = models.CharField(max_length=120)
	rating = models.CharField(max_length=25)
	height = models.DecimalField(max_digits=6, decimal_places=0)
	waifu_of_the_month = models.BooleanField()
	img_url = models.CharField(max_length=100)

	def __str__(self):
		return self.name
