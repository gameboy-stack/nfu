from django.shortcuts import render
from nfu.settings import *
from . import fllwng
import os
def home(request):
	hell = "Follwng_final.txt"
	dirf = os.path.join(BASE_DIR,hell)
	fwng = []
	fwng = fllwngcls.fllwnglistfunc()



	chckng = dirf if dirf!="" else "nthng"

	return render(request,'home.html',{'check':chckng,'flwng':fwng})