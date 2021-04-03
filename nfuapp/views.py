from django.shortcuts import render
from nfu.settings import *
from . import fllwng
import os
def home(request):	#,acc,acctype
	hell = "Follwng_final.txt"
	fwng = []
	fwngobj = fllwng.fllwngcls()
	fwng = fwngobj.fllwnglistfunc()
	profile = fwngobj.logi("_._.venki._._")
	print("prof priv")
	print(profile.is_private)
	print("follow by view")
	print(profile.followed_by_viewer)
	usrnfu = fwngobj.ntffunc(profile)

	ntfufinallist = list(set(usrnfu) - set(fwng))
	ntfufinallist.sort()

	return render(request,'home.html',{'no':len(ntfufinallist),'flwng':ntfufinallist})