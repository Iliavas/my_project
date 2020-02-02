from django.db import models

class text_image(models.Model):
	image = models.ImageField(upload_to='images/')
