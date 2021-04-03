from django.shortcuts import render
from nfu.settings import *
from . import fllwng
import os
def home(request):
	hell = "Follwng_final.txt"
	fwng = []
	fwngobj = fllwng.fllwngcls()
	fwng = fwngobj.fllwnglistfunc()
	return render(request,'home.html',{'flwng':fwng})