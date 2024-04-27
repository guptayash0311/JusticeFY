from django.contrib import admin
# Register your models here.
from django.contrib.admin.sites import site 
from .models import Lawyer
from .models import PhysicalJudge
from .models import VirtualJudge
from django.contrib import admin
from JusticeFY_app.models import Lawyer 
from JusticeFY_app.models import PhysicalJudge;
from JusticeFY_app.models import VirtualJudge;


# @admin.register(Lawyer)
# class LawyerAdmin(admin.ModelAdmin):
#     list_display = ('CNR', 'ClientName', 'CaseStatus', 'CaseType', 'Doc', 'ApplytoVC')
admin.site.register(Lawyer)


# @admin.register(PhysicalJudge)
# class PhysicalJudgeAdmin(admin.ModelAdmin):
#     list_display = ('CNR', 'CaseStatus', 'Lawyer_1', 'Lawyer_2', 'Lawyer1ASVC', 'Lawyer2ASVC', 'Approve')
admin.site.register(PhysicalJudge)


# @admin.register(VirtualJudge)
# class VirtualJudgeAdmin(admin.ModelAdmin):
#     list_display = ('CNR', 'CaseStatus', 'Lawyer_1', 'Lawyer_2', 'virtualcourt')
admin.site.register(VirtualJudge)

