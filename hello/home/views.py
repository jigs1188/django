from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import contacts
# Create your views here.

def index(request) :
    # context={
        # 'variable1':'i am jignesh',
        # 'variable2':'she is neha'
    # }
    return render(request,'index.html')
    # return render(request,'index.html',context)
    # return HttpResponse("This is Homepage")

def service(request) : 
    return render(request,'service.html')
    
    # return HttpResponse("this is service")

def contact(request) :
    if request.method == "POST":
        name=request.POST.get('name')
        firstname=request.POST.get('firstname') 
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = contacts( name=name,firstname=firstname ,email=email ,phone=phone ,desc=desc ,date=datetime.today())
        contact.save()
    
    return render(request,'contact.html')
    
    # return HttpResponse("this is contact")

