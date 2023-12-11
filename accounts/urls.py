from django.urls import path

from accounts import views

urlpatterns = [

    path('signup',views.Signup.as_view(),name='signup'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.logout_view,name='logout'),
    path('reset_password',views.Forgot_password,name='reset_password')


]