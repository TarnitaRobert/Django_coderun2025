from django.db import models

# Create your models here.
# demo model class, user info based
class UserInfo(models.Model):
    name= models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.IntegerField()
    mail = models.EmailField(max_length=254)
    job = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class DemoModel(models.Model):
    field1= models.CharField(max_length=32)
    field2= models.FloatField()

    def __str__(self):
        return self.field1

