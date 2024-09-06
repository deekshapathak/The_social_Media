from django.shortcuts import render,redirect
from .models import Profile ,Tweet
from django.contrib import messages
from .forms import TweetForm
from django.contrib.auth import authenticate ,login,logout


def login_user(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user=authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         messages.success(request,("start tweeting you have logged in !"))
         return redirect('home')
      else:
         messages.success(request,("pleasse login after some time an error occured !"))
         return redirect('login')
         
         
         

   else: 
     return render(request,'login.html',{})


def logout_user(request):
   logout(request)
   messages.success(request,("you have been logged out "))
   return redirect('home')
   


def home(request):
    if request.user.is_authenticated:
       form =TweetForm(request.POST or None)
       if request.method =="POST":
          if form.is_valid():
             tweet=form.save(commit= False)
             tweet.user = request.user
             tweet.save()
             messages.success(request,("your tweet is created"))
             return redirect('home')


       tweet=Tweet.objects.all().order_by("-created_at")
       return render(request,'home.html',{"tweet":tweet,"form":form})
    else:
        tweet=Tweet.objects.all().order_by("-created_at")
        return render(request,'home.html',{"tweet":tweet})


def profile_list(request):
    if request.user.is_authenticated:
     profiles = Profile.objects.exclude(user=request.user)
     return render(request,'profile_list.html',{"profiles":profiles})
    else:
       messages.success(request,("you must be logged in "))
       return redirect('home.html')



def profile(request,pk):
    if request.user.is_authenticated:
      
      profile = Profile.objects.get(user_id=pk)
      tweet = Tweet.objects.filter(user_id=pk)

    #   post form logic here
      if request.method == 'POST':
        #  get current user id 
        current_user_profile = request.user.profile
        # get the form data
        action = request.POST['follow']
        # follow or infollow
        if action =="unfollow":
           current_user_profile.follows.remove(profile)
        elif action == "follow":
           current_user_profile.follows.add(profile)
        #    save th eprofile noe
        current_user_profile.save()
         
      return render(request,"profile.html",{"profile":profile ,"tweet":tweet})   ##cc
    else:
        messages.success(request,("you must be logged in "))
        return redirect('home.html')
      
      
