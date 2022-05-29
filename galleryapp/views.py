from django.shortcuts import render, redirect
from galleryapp import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your views here.

def login(request):  #登入
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['passwd']  #取得輸入密碼
		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/photo/')  #開啟相片頁面
			else:  #帳號無效
				message = '帳號尚未啟用！'
		else:  #驗證未通過
			message = '登入失敗！'
	return render(request, "login.html", locals())
    
def logout(request):  #登出
	auth.logout(request)
	return redirect('')

def signin(request):  #註冊

	return render(request, "signin.html", locals())

def photoshow(request):  #顯示相片

	return render(request, "index.html", locals())

def albumshow(request):  #顯示相簿

	return render(request, "album.html", locals())

def trashshow(request):  #顯示垃圾桶

	return render(request, "trash.html", locals())