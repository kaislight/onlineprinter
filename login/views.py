from django.shortcuts import render,redirect
from login import models
from login.models import UserForm,RegisterForm
import hashlib
import random
import os
import pandas as pd
import numpy as np


def index(request):
    request.session['active'] = 'index'
    return render(request,'login/index.html')


def refresh(request):
    return redirect('/index/')

def dlist(request):
    data = []
    path = "./list/"
    dirs = os.listdir( path )
    for i in dirs:
        p = path + i + '/status.txt'
        f = open(p,"r",encoding='utf-8')
        gets = f.read().split('\n')
        data.append({'name':i,'status':gets[0],'kind':gets[1],'pp':gets[2]})
    request.session['active'] = 'dlist'
    if request.POST:
        n = []
        for i in request.POST.keys():
            n.append(i)
        print(n)
        pf = random.randint(7,10)
        request.session['equip'] = n[1]
        return redirect('/equip/')
    return render(request,'login/dlist.html',{'data':data})

def about(request):
    return render(request,'login/about.html')

def printlist(request):
    return render(request,'login/printlist.html')

def printhistory(request):
    return render(request,'login/printhistory.html')

def printabout(request):
    return render(request,'login/printabout.html')

def equip(request):
    request.session['active'] = 'eqp'
    request.session['status'] = 'bjzt'
    if request.method == "POST":
        print (request)
        myfile = request.FILES.get('myfile')
        file = open('static/get/wait/' + str(myfile),'wb')
        for chunk in myfile.chunks():
            file.write(chunk)
        file.close()
        return redirect('/equip/printlist/')
    return render(request,'login/eqp.html',{'equip':request.session['equip']})

def bjzt(request):
    request.session['status'] = 'bjzt'
    return redirect('/equip/')

def dylb(request):
    request.session['status'] = 'dylb'
    return redirect('/equip/')

def lsjl(request):
    request.session['status'] = 'lsjl'
    return redirect('/equip/')

def login(request):
    print(request.POST)
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = models.User.objects.get(name=username)
            if user.password == hash_code(password):  # ??????????????????????????????????????????
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = "??????????????????"
        except:
            message = "??????????????????"
        return render(request, 'login/login2.html', locals())

    return render(request, 'login/login2.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # ????????????????????????????????????????????????????????????
        return redirect("/index/")
    
    if request.method == "POST":  # ????????????
        message = "???????????????????????????"
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 != password2:  # ??????????????????????????????
            message = "??????????????????????????????"
            return render(request, 'login/register2.html', locals())
        else:
            same_name_user = models.User.objects.filter(name=username)
            if same_name_user:  # ???????????????
                message = '????????????????????????????????????????????????'
                return render(request, 'login/register2.html', locals())
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:  # ??????????????????
                message = '??????????????????????????????????????????????????????'
                return render(request, 'login/register2.html', locals())

            # ????????????OK??????????????????????????????

            new_user = models.User.objects.create()
            new_user.name = username
            new_user.password = hash_code(password1)  # ??????????????????
            new_user.email = email
            new_user.save()
            return redirect('/login/')  # ???????????????????????????
    return render(request, 'login/register2.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()

    return redirect('/index/')

def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update???????????????bytes??????
    return h.hexdigest()