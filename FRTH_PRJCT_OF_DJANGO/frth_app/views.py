from django.shortcuts import render
from frth_app.forms import UserForm,User_ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(req):
    return render(req,'frth_app/index.html')

@login_required
def special(req):
    return HttpResponse("You'r Logged In : Nice:) ")

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))

def register(req):
     registered = False

     if req.method == "POST":
         user_form = UserForm(data=req.POST)
         profile_form = User_ProfileForm(data=req.POST)

         if user_form.is_valid() and profile_form.is_valid():
             user = user_form.save()
             user.set_password(user.password)
             user.save()

             profile = profile_form.save(commit=False)
             profile.user = user

             if 'profile_pic' in req.FILES:
                 profile.profile_pic = req.FILES('profile_pic')

             profile.save()

             registered=True
         else:
             print("EROOOORRRR")
     else:
         user_form = UserForm()
         profile_form = User_ProfileForm()

     return render(req,'frth_app/register.html',{'user_form':user_form,
                                                 'profile_form':profile_form,
                                                  'registered':registered,})

def user_login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("NOT AN ACTIVE ACCOUNT")
        else:
            print("INVALID LOGIN CREDENTIALS")
            print("WRONG DATA IS:")
            print("Username : {} Password : {}".format(username,password))
    else:
        return render(req,'frth_app/login.html',{})
