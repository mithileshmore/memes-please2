from django.shortcuts import render, redirect  
from memes.forms import UserLoginForm  
from memes.models import UserLogin  
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import random


def user_login(request):
    if request.method == "POST": 
        form = UserLoginForm(request.POST)
        if form.is_valid():  
            try:
                user = authenticate(
                    username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    if user.is_active:
                        request.session.set_expiry(86400)
                        login(request, user)
                        cookies = request.COOKIES
                        return render(request,'memes_cookies.html', {'cookies':cookies}) 
                    else:
                        form = UserLoginForm()  
                        return render(request,'index.html') 
            except:  
                pass  
    else:
        form = UserLoginForm()  
        return render(request,'index.html')  


@login_required(login_url='/user_login/')
def show(request): 
    if request.method == 'POST':
        if 'cookie_ok' in request.POST:
            UserLogin.objects.filter(username=request.COOKIES['username']).update(cookie_consent=1)
            resp = requests.get('http://alpha-meme-maker.herokuapp.com/').json()
            random_memes = random.sample(resp['data'], 5)
            random_memes_urls = [item['image'] for item in random_memes]
            cookies = request.COOKIES
            return render(request,'display_cookies.html', {'memes':random_memes_urls})  
        elif 'close-cookies' in request.POST:
            UserLogin.objects.filter(username=request.COOKIES['username']).update(cookie_consent=0)
            logout(request) 
            return render(request,'index.html')
