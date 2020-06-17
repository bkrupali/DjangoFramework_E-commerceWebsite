from django.shortcuts import render,redirect
from django.db import models
from .models import *
# Create your views here.
def index(request):
    return render(request,'login.html')
def reg(request):
    return render(request, 'reg.html')

class Registration(models.Model):
    Name=models.CharField(max_length=200,blank=True)
    Email = models.CharField(max_length=200, blank=True)
    Password= models.CharField(max_length=200, blank=True)

def registration(request):
    if request.method=='POST':
        member=Registration(Name=request.POST['username'],Email=request.POST['email'],Password=request.POST['password'])
        member.save()
        return render(request,'login.html')
    
def login_query(request):
    if request.method == 'POST':
        global email
        email=request.POST['email']
        password=request.POST['password']
        test=Registration.objects.filter(Email=email).filter(Password=password)
        
        if test.count()>0:
            s={'msg':"login is successful"}
            return redirect('/mysite')
        else:
            return redirect('/login')

def show_entry(request):
    context={'s_name':Product.objects.all().order_by('?'[:6])}
    return render(request,'index.html',context)
def Addcart(request):
     if request.method== 'POST':
         order_1=Order(Product_fk=request.POST['p_fk'],user_fk=email,order_total=request.POST['p_price'],order_del='pending',order_status='0')
         order_1.save()
         return redirect('/mysite')