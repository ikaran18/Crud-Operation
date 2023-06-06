from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .forms import StudentRegistration,SignupForm
from .models import Student
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
#This Function is for ADD AND SHOW DATA
def addandshow(request):
    if  request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = StudentRegistration()    
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'addandshow.html',{"form":fm, "stu":stud})

#This Function is for UPDATE DATA
def update(request,id):
    if request.method=="POST":
        pi = Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'update.html',{"form":fm})

#This Function is for DELETE DATA
def delete(request,id):
    if request.method=="POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
    
def signup(request):
    if request.method=="POST":
        gm = SignupForm(request.POST)
        if gm.is_valid():
            gm.save()
    else:
        gm=SignupForm()
    return render(request,'signup.html',{"gm":gm})

def user_login(request):
    if request.method =="POST":
        gm=AuthenticationForm(request=request,data=request.POST)
        if gm.is_valid():
            ename=gm.cleaned_data['username']
            upass=gm.cleaned_data['password']
            user = authenticate(username=ename,passowrd=upass)
            if user is not None:
                 login(request,user)
                 return HttpResponseRedirect('/addandshow/')
    else:
        gm=AuthenticationForm()
    return render(request,'login.html',{"gm":gm})