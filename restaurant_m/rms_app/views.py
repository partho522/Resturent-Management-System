from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,redirect
from .models import Employee,Bill



# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,"Home.html")


def login_v(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html",{"messege":"Invalid Credentials."})
    else:   
        return render(request, "login.html")



@login_required(login_url='login')
def logout_v(request):
    logout(request)
    return render(request, "login.html", {"messege":"LOGGED OUT"})


@login_required(login_url='login')
def home(request):
    return render(request,"Home.html")



def add_emp(request):
    if request.method == 'POST':
        id = request.POST["ID"]
        name = request.POST["name"]
        post = request.POST["pname"]
        phone = request.POST["phoneNum"]
        salary = request.POST["salary"]

        if id == '' or name =='' or post == '' or phone == '' or salary == '':
            message = "Enter All the field"
            return render(request,"add_emp.html",{"message":message})
        else:
            emp = Employee(ID=id,Name=name,Post=post,Phone=phone,Salary=salary)
            emp.save()
        return HttpResponseRedirect(reverse('display_emp'))
    else:
        return render(request,"add_emp.html")


def display_emp(request):
    emp = Employee.objects.all()
    return render(request,"display_emp.html",{"emp":emp})




def del_emp(request):
    if request.method == 'POST':
        id = request.POST["ID"]
        
        if id == '':
            message = "Enter the field"
            return render(request,"del_emp.html",{"message":message})
        else:
            emp = Employee.objects.get(ID=id)
            emp.delete()  
        return HttpResponseRedirect(reverse('display_emp'))
    else:

        return render(request,"del_emp.html")



def add_bill(request):
    if request.method == 'POST':
        Order_or_Serial = request.POST["OrderSerial"]
        Amount = request.POST["Amount"]
        Bill_or_Status = request.POST["BillStatus"]

        if  Order_or_Serial == '' or Amount == '' or Bill_or_Status == '':
            message = "Enter All the field"
            return render(request,"add_bill.html",{"message":message})
        else:
            

            bill = Bill(Order_or_Serial = Order_or_Serial,Amount = Amount,Bill_or_Status = Bill_or_Status)
            bill.save()   

        return HttpResponseRedirect(reverse('display_bill'))

    else:
        return render(request,"add_bill.html")


def display_bill(request):
    bill = Bill.objects.all()
    return render(request,"display_bill.html",{"bill":bill})
    


        
        

    


