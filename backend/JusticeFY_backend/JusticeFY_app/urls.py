from JusticeFY_app import views
from django.urls import path
from JusticeFY_app import views

urlpatterns = [
    path('lawyers/',views.getLawyers, name="getLawyers"),
]