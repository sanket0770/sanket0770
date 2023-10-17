from datetime import datetime
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, HttpResponse, redirect
from django.template import Context
from portal.models import paymentdetails , message, rentdetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import boto3



# To render index page
def index(request):
    return render(request,"index.html")

# To render about page
def about(request):
    return render(request, 'about.html')

#To render contact page also send SNS notification
def contact(request):
    if request.method=="POST":
        mfname=request.POST.get('mfname')
        mlname=request.POST.get('mlname')
        mcontact=request.POST.get('mcontact')
        memail=request.POST.get('memail')
        mmessage=request.POST.get('mmessage')
        msg=message(mfname=mfname, mlname=mlname, mcontact=mcontact, memail=memail, mmessage=mmessage, mdate=datetime.today())
        msg.save()
        
        #variable to pass to the SNS topic
        msg= "Name: "+mfname+" "+mlname+ "\n\n" + "Email ID: "+memail+"\n\n"+"Contact: "+mcontact+"\n\n"+ "Message: "+"\n\n"+mmessage 
        
        sub= "New Enquiry from "+ mfname + " "+ mlname
        
        #to send notification to admin user using SNS
        topic_arn = 'arn:aws:sns:us-east-1:325026202833:SendNotification'
        smessage = msg
        subject = sub
     
        AWS_REGION = 'us-east-1'
        sns_client = boto3.client('sns', region_name=AWS_REGION)
        response = sns_client.publish(
                TopicArn=topic_arn,
                Message=smessage,
                Subject=subject,
                )['MessageId']
                
        file=request.POST.get('file1')
        
        upload_file(file, "cavyhome")
                
        
    
    return render(request, 'contact.html')

# To display list of message from external user. 
# Required authentication to view
def mmessage (request):
    if request.user.is_authenticated:
        info= message.objects.all()
        return render(request,'message.html', {"info" : info})
    return redirect("/login")

# To display message from external user. 
# Required authentication to view
def msgshow (request):
    if request.method=="POST":
        mfname=request.POST.get('mfname')
        k = message.objects.all().filter(mfname=mfname)
    return render(request, 'msgshow.html',{"k" : k})
    
#To Authenticate Admin user
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('addtenant')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

# To view dishboard
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return redirect("/login")

#To add tenant details
#Required authentication
def addtenant(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        laddress=request.POST.get('laddress')
        pdetails=request.POST.get('pdetails')
        ramt=request.POST.get('ramt')
        damt=request.POST.get('damt')
        sdate=request.POST.get('sdate')
        ldate=request.POST.get('ldate')
        addtenant = rentdetails(fname=fname, lname=lname, contact=contact, email=email, laddress=laddress, pdetails=pdetails, ramt=ramt, damt=damt, sdate=sdate,ldate=ldate)
        addtenant.save()

        addpayment= paymentdetails (fname=fname, lname=lname,ramt=ramt)
        addpayment.save()
    return render(request,'addtenant.html')



        
#To view tenant details
#Required authentication
def details(request):
    if request.user.is_authenticated:
        info= rentdetails.objects.all()
        return render(request,'details.html', {"info" : info})
    return redirect("/login")

#To view tenant details
#Required authentication
def show(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        k = rentdetails.objects.all().filter(fname=fname)
    return render(request, 'show.html',{"k" : k})


#To view details of specific tenant
#Required authentication
def pdetails(request):  
    if request.method == "POST":
        fname=request.POST.get('fname')
        k = paymentdetails.objects.all().filter(fname=fname)
    return render(request,"pdetails.html",{"k" : k})

#to return updated table
def s_pdetails(request):
   
    if request.method=="POST":
        sname=request.POST.get('sname')
        lname=request.POST.get('lname')
        ramt=request.POST.get('ramt')
        rmonth=request.POST.get('rmonth')
        rdate=request.POST.get('rdate')

        
        upd_pay =paymentdetails.objects.all().filter(fname=sname)
        upd_pay.update(fname=sname, lname=lname, ramt=ramt, rmonth=rmonth, rdate=rdate)

        upd_rent = rentdetails.objects.all().filter(fname=sname)
        upd_rent.update(ramt=ramt)
        info= rentdetails.objects.all()
    return render(request,"details.html", {"info" : info})

#To logout user
def logoutuser(request):
    logout(request)
    return redirect("/index")

# Create your views here.
