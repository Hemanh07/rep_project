from django.urls import path
from . import views
urlpatterns = [
   path("", views.hod_login,name='hod_login'),
   
]
