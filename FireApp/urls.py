from django.urls import path
from django.urls.conf import include
from .views import *


urlpatterns = [
    path('accounts/login/',LoginRedirect.as_view(), name = 'login_redirect'),
    path('accounts/signup/',Signup.as_view(), name = 'signup_redirect'),
    path('accounts/', include("allauth.urls")),
    path('',Home.as_view(), name = 'home'),
    path('check/',Check.as_view(), name = 'check'),
    path('dashboard/',DashBoard.as_view(), name = 'dashboard'),
    path('signup/',Signup.as_view() , name = 'signup'),
    path('login/',Login.as_view(), name = 'login'),
    path('logout/',Logout.as_view(), name = 'logout'),

]
