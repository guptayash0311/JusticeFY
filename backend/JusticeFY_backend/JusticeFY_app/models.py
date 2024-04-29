from django.db import models
from django.contrib.auth.models import User

class Lawyer(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    CNR = models.CharField(max_length=200)
    ClientName = models.CharField(max_length=100)
    CaseStatus = models.CharField(max_length=50)
    CaseType = models.CharField(max_length=50)
    Doc = models.FileField(upload_to='documents/', null=True, blank=True)
    ApplytoVC = models.CharField(max_length=200)
# Create your models here.

class PhysicalJudge(models.Model):
    CNR = models.CharField(max_length=16)
    CaseStatus = models.CharField(max_length=50)
    Lawyer_1 = models.CharField(max_length=100)
    Lawyer_2 = models.CharField(max_length=100)
    Lawyer1ASVC = models.BooleanField(default=False)
    Lawyer2ASVC = models.BooleanField(default=False)
    Approve = models.CharField(max_length=200)

class VirtualJudge(models.Model):
    CNR = models.CharField(max_length=16)
    CaseStatus = models.CharField(max_length=50)
    Lawyer_1 = models.CharField(max_length=100)
    Lawyer_2 = models.CharField(max_length=100)
    virtualcourt = models.CharField(max_length=200)
