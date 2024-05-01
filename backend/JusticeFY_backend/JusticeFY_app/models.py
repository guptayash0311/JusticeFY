from django.db import models
from django.contrib.auth.models import User
# from .models import Cases
# from .models import Lawyer
# from .models import Ph_Judge

class Lawyer(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    CNR = models.CharField(max_length=200)
    ClientName = models.CharField(max_length=100)
    CaseStatus = models.CharField(max_length=50)
    CaseType = models.CharField(max_length=50)
    Doc = models.FileField(upload_to='documents/', null=True, blank=True)
    ApplytoVC = models.CharField(max_length=200)
# # Create your models here.

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


class Cases(models.Model):
    CNR = models.CharField(max_length=100, primary_key=True)
    Case_Type = models.CharField(max_length=255)
    Section_No = models.CharField(max_length=100)
    Filing_Date = models.DateField()
    City = models.CharField(max_length=255)
    Lawyer_Username = models.CharField(max_length=255)
    Judge_Username = models.CharField(max_length=255)
    Description = models.TextField()

    
# class Lawyer(models.Model):
#     Name = models.CharField(max_length=255)
#     Lawyer_ID = models.CharField(max_length=100, primary_key=True)
#     Email = models.EmailField()
#     Phone_No = models.CharField(max_length=20)
#     License_No = models.CharField(max_length=50)
#     Specialization = models.CharField(max_length=255)
#     Bio = models.TextField()

#     def __str__(self):
#         return self.Name
    
# class Ph_Judge(models.Model):
#     Name = models.CharField(max_length=255)
#     Ph_Judge_ID = models.CharField(max_length=100, primary_key=True)
#     Email = models.EmailField()
#     Phone_No = models.CharField(max_length=20)
#     Court = models.CharField(max_length=255)
#     Bio = models.TextField()

#     def __str__(self):
#         return self.Name

# class Vr_Judge(models.Model):
#     Name = models.CharField(max_length=255)
#     Vr_Judge_ID = models.CharField(max_length=100, primary_key=True)
#     Email = models.EmailField()
#     Phone_No = models.CharField(max_length=20)
#     Bio = models.TextField()

#     def __str__(self):
#         return self.Name

# class Lawyer_Cart(models.Model):
#     CNR = models.ForeignKey(Cases, on_delete=models.CASCADE)
#     Plaintiff = models.CharField(max_length=255)
#     Defendant = models.CharField(max_length=255)

#     def __str__(self):
#         return f"Lawyer Cart - {self.CNR}"
    
# class Ph_Judge_Cart(models.Model):
#     CNR = models.ForeignKey(Cases, on_delete=models.CASCADE)
#     Lawyer_ID = models.ForeignKey(Lawyer, related_name='lawyer1', on_delete=models.CASCADE)
#     Lawyer_ID2 = models.ForeignKey(Lawyer, related_name='lawyer2', on_delete=models.CASCADE)
#     Rozname = models.TextField()
#     Application_1 = models.TextField()
#     Application_2 = models.TextField()

#     def __str__(self):
#         return f"Ph Judge Cart - {self.CNR}"
    
# class Vr_Judge_Cart(models.Model):
#     CNR = models.ForeignKey(Cases, on_delete=models.CASCADE)
#     Lawyer_ID = models.ForeignKey(Lawyer, related_name='vr_lawyer1', on_delete=models.CASCADE)
#     Lawyer_ID2 = models.ForeignKey(Lawyer, related_name='vr_lawyer2', on_delete=models.CASCADE)
#     Ph_Judge_ID = models.ForeignKey(Ph_Judge, on_delete=models.CASCADE)
#     Rozname = models.TextField()

#     def __str__(self):
#         return f"Vr Judge Cart - {self.CNR}"