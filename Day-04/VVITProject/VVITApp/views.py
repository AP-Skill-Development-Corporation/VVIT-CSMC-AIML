from django.shortcuts import render,redirect
from .forms import UsregForm
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'CSMA/home.html')

def about(request):
	return render(request,'CSMA/about.html')

def register(request):
	if request.method == "POST":
		p = UsregForm(request.POST)
		if p.is_valid():
			p.save()
			messages.success(request,'Registered Successfully!!')
			return redirect('/')
	p = UsregForm()
	return render(request,'CSMA/registration.html',{'z':p})