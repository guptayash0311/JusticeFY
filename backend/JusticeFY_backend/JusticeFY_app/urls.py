from JusticeFY_app import views
from django.urls import path
from JusticeFY_app import views

urlpatterns = [
    path('lawyers/',views.getLawyers, name="getLawyers"),
    path('register/',views.createUser, name="createUser"),
    path('login/',views.loginUser, name="loginUser"),
    path('',views.Home, name="Home"),
    # path('login/cart/',views.Cart, name="Cart")
]