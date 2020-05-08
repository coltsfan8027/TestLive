from django.shortcuts import render, redirect
from .forms import *

def index(request):
    return render(request, 'mainpage/index.html')

def registration(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            newUser = form.save(commit=False)
            newUser.user = request.user
            newUser.save()
            return redirect('/admin')
        else:
            form = UserForm()
    

    return render(request, 'mainpage/registration.html', {'form': form})

    






