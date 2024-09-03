from django.shortcuts import render, redirect
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegistrationForm
from datetime import datetime
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings

def home(request):
    return render(request,"home.html")

def insert(request):
    if request.method=="POST":
        form=MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registration succesfully completed")
                return redirect("Home")
            except:
                pass
    else:
        form=MyRegisterForm()
    return render(request,"register.html",{"form":form})


def need(request):
     data = RegistrationForm.objects.all()

    # if 'search' in request.POST:
    #     query = request.POST['search']
    #     data = data.filter( bloodgroup__icontains=query)

    # if data:
    #     return render(request, "need.html", {"data": data})
    # else:
    #     message = "Oops, no data available!"
    #     context = {'emoji':'😔'}
    #     return render(request, "need.html", {"messaged": message, "context": context})
     return render(request,"search.html")
def search(request):
    data = RegistrationForm.objects.all()

    if 'search' in request.POST:
        query = request.POST['search']
        native= request.POST['searchs']
        data = data.filter( bloodgroup__icontains=query, native__icontains=native)
        

    if data:
        return render(request, "need.html", {"data": data})
    else:
        message = "Oops, no data available!"
        context = {'emoji':'😔'}
        return render(request, "need.html", {"messaged": message, "context": context})

def login(request):
    if "email" in request.POST and "password" in request.POST:
        logged_email = request.POST['email']
        logged_password = request.POST['password']
        
        # Use get() to retrieve a single object matching both email and password
        user = RegistrationForm.objects.filter(email__iexact=logged_email, password=logged_password).first()

        if user:
            # Pass the user data to the template
            return render(request, "login.html", {"data": [user]})
        else:
            message = "Oops, invalid email or password"
            return render(request, "login.html", {"error": message})
    else:
        # If email or password is not in the request POST data
        message = "Please provide both email and password"
        return render(request, "login.html", {"error": message})
def updatedata(request, id):
    obj = RegistrationForm.objects.get(id=id)
    # if request.method == "POST":
    #     try:
    #         donated_date = request.POST["donated_date"]
    #         calculate = datetime.strptime(donated_date, "%Y-%m-%d")
    #         obj.donated_date = calculate
    #         obj.save()
    #         return render(request, "update.html", {"data": obj})
    #     except KeyError:
    #         error_message = "Error: 'donated_date' key not found in the POST data."
    #      return render(request, "update.html", {"error_message": error_message})
    # else:
    return render(request, "update.html",{'data':obj}) 
def update(request):
    if request.method == "POST":
        try:
            donated_date = request.POST["donated"]
            contact = request.POST["contact"]
            id = request.POST["id"]
            obj = RegistrationForm.objects.get(id=id)
            obj.donated_date = donated_date
            obj.contact = contact  # Assign directly, no need for strptime()
            obj.save()
            return render(request, "update.html", {"data": obj})
        except KeyError:
            error_message = "Error: 'donated_date' key not found in the POST data."
            return render(request, "update.html", {"error_message": error_message})
    else:
         return render(request, "update.html", {"data": obj})
