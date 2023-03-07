from django.db import models

# Create your models here.
# for district
class District(models.Model):
    name=models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.name

# for branches
class Branches(models.Model):
    bname=models.CharField(max_length=250,unique=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.bname

#for user details
class User_details(models.Model):
    username=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phno=models.IntegerField()
    mailid=models.CharField(max_length=250)
    addres=models.CharField(max_length=250)
    district=models.ForeignKey(District,db_column='district', on_delete=models.CASCADE)
    branch=models.ForeignKey(Branches,db_column='branch', on_delete=models.CASCADE)
    account_type=models.CharField(max_length=250)
    materials=models.CharField(max_length=250)
    def __str__(self):
        return self.name


