from django.shortcuts import render
from nfu.settings import *
from . import fllwng
import os
def home(request):	#,acc
	hell = "Follwng_final.txt"
	fwng = []
	fwngobj = fllwng.fllwngcls()
	fwng = fwngobj.fllwnglistfunc() # pre prepared following list
	profile = fwngobj.logi("_._.venki._._") # acc 
	"""	if(profile.is_private):
	if(profile.followed_by_viewer == False):"""

	usrnfu = fwngobj.ntffunc(profile)

	ntfufinallist = list(set(usrnfu) - set(fwng))
	ntfufinallist.sort()

	return render(request,'home.html',{'flwng':ntfufinallist})