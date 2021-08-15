from django.db import models

# Create your models here.

class place(models.Model):
    # id:int
    # name:str
    # img:str
    # desc:str
    # price:int
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='picture')
    desc=models.TextField()
    price= models.IntegerField()
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class newspost(models.Model):
    month= models.CharField(max_length=50)
    day= models.IntegerField()
    headline= models.TextField()
    descr= models.TextField()
    image= models.ImageField(upload_to='pic')
