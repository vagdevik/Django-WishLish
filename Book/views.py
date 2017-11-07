# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import form
from .models import Catalog
def index(request):
    if request.method=='POST':
        form1=form(request.POST)
        if form1.is_valid():
            instance = Catalog(Reader_Name=request.POST.get('reader'),Author_Name=request.POST.get('author'),Book_Name=request.POST.get('book'),Category=request.POST.get('category'),Rate=request.POST.get('rate'))
            print instance.Reader_Name
            #, Assignment_File=request.FILES['file'],End_Time=request.POST.get('enddate'))
            instance.save()
            s=1
            form1=form()
            return render(request,'index.html',{'form':form1,'s':s})
            #return HttpResponseRedirect('/Books/')
    else:
        form1 = form()
        s=0
    return render(request,'index.html',{'form':form1,'s':s})
