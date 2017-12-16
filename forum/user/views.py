# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User

def Users(request):
    if request.method =='GET':
        return render(request,'register.html')

    else:
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,
                                        email=email, password=password)
        user.is_active = True
        user.save()
        return render(request,'user.html')

