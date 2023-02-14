from django.db import models

# Create your models here.
class agencyregmodel(models.Model):
    agency=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    password=models.CharField(max_length=10)

class userregmodel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=20)


class packageuploadmodel(models.Model):
    catchoice=[
        ('food','food'),
        ('yes','yes'),
        ('no','no'),
    ]
    choice=[
        ('pet','pet'),
        ('yes','yes'),
        ('no','no'),
    ]
    cchoice=[
        ('0-0','0-0'),
        ('0-1','0-1'),
        ('1-2','1-2'),
        ('2-3','2-3'),
        ('3-4','3-4'),
        ('4-5','4-5'),
        ('5-6','5-6'),
        ('6-7','6-7'),
        ('7-8','7-8'),
        ('8-9','8-9'),
        ('9-10','9-10')
    ]
    agency=models.CharField(max_length=20)
    email=models.EmailField()
    destina=models.CharField(max_length=300)
    food=models.CharField(max_length=20,choices=catchoice)
    pet=models.CharField(max_length=20,choices=choice)
    duration=models.CharField(max_length=20,choices=cchoice)
    stay=models.CharField(max_length=20)
    rate = models.CharField(max_length=20)

class bookmodel(models.Model):
    agency=models.CharField(max_length=20)
    destina=models.CharField(max_length=300)
    rate=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.EmailField()


class wishmodel(models.Model):
    agency = models.CharField(max_length=20)
    email = models.EmailField()
    destina = models.CharField(max_length=300,null=True)
    food = models.CharField(max_length=20)
    pet = models.CharField(max_length=20)
    duration = models.CharField(max_length=20,null=True)
    stay = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)

class placemodel(models.Model):
    state=models.CharField(max_length=20)
    details=models.CharField(max_length=500)