from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hek(k):
	return HttpResponse("Welcome User")

def gy(y):
	return HttpResponse("<h2>Welcome User</h2>")

def hk(request,n):
	return HttpResponse(f"Hi User {n}")

def byh(request,a,g):
	return HttpResponse(f"Hi user username: {g} Age: {a}")

def kn(request,cn,sn,rn):
	return HttpResponse(f"Name: <span style='color:green'>{cn}</span> Roll number: <span style='color:red'>{sn}</span> Age: <span style='color:blue'>{rn}</span>")

def km(request):
	return render(request,'demo.html')

def vh(request,k):
	return render(request,'sample.html',{"h":k})

def wh(request):
	if request.method == "POST":
		a = request.POST['sn']
		b = request.POST['sr']
		c = request.POST['sb']
		return render(request,'stdata.html',{'p':a,'q':b,'r':c})
	return render(request,'streg.html')

def emp(request):
	return render(request,'employee.html')

