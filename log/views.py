from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth

def login(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            args['err'] = "Неверный логин или пароль! Если забыли данные, напишите на support@opros.ru "
            return render(request, 'log/index.html', args)
    else:
        return render(request, 'log/index.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')
