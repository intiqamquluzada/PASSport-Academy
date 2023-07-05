from django.urls import path
from .views import *


app_name = "pac"
urlpatterns = [
    path("home/", home_view, name='home')

]
