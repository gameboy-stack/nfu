from django.shortcuts import render
from nfu.settings import *
import os
def home(request):
	hell = "Follwng_final.txt"
	dirf = os.path.join(BASE_DIR,hell)
	fllwng = []

	with open(dirf) as f:
		fllwng = [line.rstrip() for line in f]

	chckng = dirf if dirf!="" else "nthng"

	return render(request,'home.html',{'check':chckng,'flwng':fllwng})