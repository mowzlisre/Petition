from django.shortcuts import render, redirect
from .models import User, Petition
from django.contrib import messages

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.designation == "Public":
            context = {
                "petitions": Petition.objects.filter(petitioner=request.user)
            }
            return render(request, 'app/home.html', context)
        else:
            context = {
                "petitions": Petition.objects.filter(petition_for=request.user)
            }
            return render(request, 'app/dashboard.html', context)

def newPetition(request):
    if request.method == "POST":
        petition = Petition()
        petition.petitioner = request.POST.get("petitioner")
        petition.petition_for = request.POST.get("petitionfor")
        petition.petition = request.POST.get("petition")
        petition.attachments = request.POST.get("attachment")
        petition.save()
        return redirect('home')
        messages.success(request, 'Your petition has been filed and is awaited for review.')



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