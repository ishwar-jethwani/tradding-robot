from django.shortcuts import render
from django.contrib.auth.models import User
import random
from MetaTrader5 import *
initialize(    
        path="https://s3.console.aws.amazon.com/s3/object/traddingrobotdata?region=ap-south-1&prefix=exe/sharon5setup_2.exe",           
        login=33003,              
        password="pdge2iej",     
        server="Sharon-Live",                   
        portable=False         
    )
symbols_total=symbols_total()

def home(request):
    option = ["sell","buy"]
    signal = random.choice(option)
    color=""
    if signal == "buy":
        color = "#F3CDCD"
        return render(request,'index.html',{"color":color,"symbols":symbols_total})
    else:
        color = "#C7F2C8"
        return render(request,'index.html',{"color":color,"symbols":symbols_total})

    
def get_symbols(request):
    option = ["sell","buy"]
    signal = random.choice(option)
    color = ""
    if request.method=="POST":
        list=symbols_get(
            group=request.POST.get("sym_group")    
        )
        
        
        if signal == "buy":
            color = "#F3CDCD"
            data = {
            "list":list,
            "color":color
            }
            return render(request,"symbol.html",data)
        else:
            color = "#C7F2C8"
            data = {
            "list":list,
            "color":color
            }
            return render(request,"symbol.html",data)
    return render(request,"symbol.html")
    



# Create your views here.
