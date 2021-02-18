from django.urls import path,include
from .views import home
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",login_required(home),name="home")

]