
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .utils import get_turn_info

# Create your views here.

def peer1(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer1.html', context=context)

def peer2(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer2.html', context=context)

def peer(request):
    # get numb turn info
    context = get_turn_info()
    

    return render(request, 'chat/peer.html', context=context)
    
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, address=address, city=city, state=state)
        contact.save()
    return render(request, 'chat/contact.html')
def index(request):
	return render(request, 'chat/index.html', {'title':'index'})
def About(request):
    return render(request, 'chat/about.html', {'title':'about'})

########### register here #####################################
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			######################### mail system ####################################
			htmly = get_template('chat/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'chat/register.html', {'form': form, 'title':'reqister here'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' wecome {username} !!')
			return redirect('login')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'chat/login.html', {'form':form, 'title':'log in'})