from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import  User, auth
# from django.shortcuts import render
from . models import place
from . models import newspost
from .form import ModeForm

# Create your views here.
def fun(request):
     # return HttpResponse("jesus save me")
     # return render(request, "home.html", {'name': 'Jesus'})
     # return render(request, "home_post.html", {'name': 'Jesus'})
     # obj= place()
     # obj.name="kerala"
     # obj.price=1000
     # obj.desc="This is kerala"
     obj=place.objects.all()
     da= newspost.objects.all()
     return render(request, "index.html",{'results':obj, 'date':da})

def register(request):
    if request.method=="POST":
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
        else:
            print("Password unmatched")
        return redirect('/')
    else:
        return render(request,'registration.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
     return render(request, "about.html")


def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        img=request.FILES['img']
        p=place(name=name,desc=desc,price=price,img=img)
        p.save()
        print("added")
        return redirect('/')

    return render(request,"add.html")

def updat(request,id):
    ob = place.objects.get(id=id)
    form = ModeForm(request.POST or None, request.FILES,instance=ob)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'obj':ob})

def delete(request,id):
    if request.method=='POST':
       obj=place.objects.get(id=id)
       obj.delete()
       return redirect('/')
    return render(request,'delete.html')

