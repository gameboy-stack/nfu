from django.shortcuts import render
from nfu.settings import *
from . import fllwng
import os
def home(request):
	hell = "Follwng_final.txt"
	fwng = []
	fwng = fllwngcls.fllwnglistfunc()
	return render(request,'home.html',{'flwng':fwng})