from django.db import models

# Create your models here.
class FirstModel(models.Model):
  title = models.CharField(max_length=50)
  name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  isActive = models.BooleanField(default=False)
  results = models.TextField()


class PersonModel(models.Model):
  SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
  )
  id = models.AutoField(primary_key=True)
  email = models.EmailField(max_length=254, unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_joined = models.DateTimeField(auto_now_add=True)
  size = models.CharField(max_length=1, choices=SHIRT_SIZES)
