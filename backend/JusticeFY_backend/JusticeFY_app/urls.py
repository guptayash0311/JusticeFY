from JusticeFY_app import views
from django.urls import path
from JusticeFY_app import views

urlpatterns = [
    path('lawyers/',views.getLawyers, name="getLawyers"),
    path('register/',views.createUser, name="createUser"),
    path('login/',views.loginUser, name="loginUser"),
    path('case_details/',views.cnr_search, name="cnr_search"),
    path('',views.Home, name="Home"),
    path('approve/',views.approve,name="approve"),
    path('platform/',views.platform,name="platform")
    # path('login/cart/',views.Cart, name="Cart")
]