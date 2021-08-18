from django.db import models
class Contact(models.Model):
    name = models.TextField(max_length=122)
    email = models.TextField(max_length=122)
    phone = models.TextField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

# Create your models here.
