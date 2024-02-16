from django.urls import path
from VVITApp import views

urlpatterns = [
	path('',views.home,name="hm"),
]