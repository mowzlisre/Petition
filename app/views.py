from django.shortcuts import render, redirect
from .models import User, Petition
from django.contrib import messages
from datetime import datetime, timedelta

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.designation == "Public":
            context = {
                "petitions": Petition.objects.filter(petitioner=request.user),
                "users": User.objects.exclude(designation='Public')
            }
            return render(request, 'app/home.html', context)
        else:
            context = {
                "petitions": Petition.objects.filter(petition_for=request.user, approved='False'),
                "approved": Petition.objects.filter(petition_for=request.user, approved='True')
            }
            return render(request, 'app/dashboard.html', context)

def newPetition(request):
    if request.method == "POST":
        petition = Petition()
        petition.petitioner = request.user
        key = request.POST.get("petitionfor")
        petition.petition_for = User.objects.get(id=key)
        petition.subject = request.POST.get("subject")
        petition.petition = request.POST.get("petition")
        petition.attachments = request.POST.get("attachment")
        petition.due = datetime.today() + timedelta(int(request.POST.get("due")))
        petition.approved = "False"
        petition.save()
        return redirect('home')
        messages.success(request, 'Your petition has been filed and is awaited for review.')

def addName(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.name = request.POST.get("username")
        user.save()
        return redirect('home')

def approve(request, pk):
    if request.method == "POST":
        petition = Petition.objects.get(id=pk)
        petition.approved = "True"
        petition.save()
        return redirect("home")

def public_register(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('username')
        user.designation = 'Public'
        password = request.POST.get('pwd1')
        user.set_password(password)
        user.save()
        return  redirect('login')
        messages.success(request, 'Your account have been registered succesfully. Now you can login and file a petition.')

    return render(request, 'app/public-register.html')