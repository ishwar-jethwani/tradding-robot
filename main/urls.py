from django.urls import path,include
from .views import home,get_symbols
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",login_required(home),name="home"),
    path("symbol/",login_required(get_symbols),name="symbol")

]