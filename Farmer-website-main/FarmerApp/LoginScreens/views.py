from django.shortcuts import render,redirect
from .models import farmer,scholar
from django.contrib.messages.api import error
from django.contrib import messages
# Create your views here.

def farmerlogin(request):
  return render(request,"farmer/farmerlogin.html",{})

def scholarlogin(request):
  return render(request,"scholar/scholarlogin.html",{})

def add_farmer(request):
  if request.method == "POST":
    farmer_name = request.POST.get("Farmer_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
  f = farmer()
  f.Farmer_name = farmer_name
  f.Contact_num = contact_num
  f.Email_id = email_id
  f.Password = password
  # f.save()
  # checking existing -
  check_existing = farmer.objects.filter(Farmer_name=farmer_name) and farmer.objects.filter(Contact_num = contact_num) and farmer.objects.filter(Email_id = email_id) and farmer.objects.filter(Password = password).exists()
  if check_existing:
    messages.error(request,"user already exists !!! try again...")
    return redirect('/login/login-farmer')
  
  else:
    f.save()
    messages.success(request,'successfully saved...')
    return redirect('/login/login-farmer')
  

# scholar form validation :-
def add_scholar(request):
  if request.method == "POST":
    scholar_name = request.POST.get("Scholar_name")
    contact_num = request.POST.get("Contact_num")
    email_id = request.POST.get("Email_id")
    password = request.POST.get("Password")
  s = scholar()
  s.Scholar_name = scholar_name
  s.Contact_num = contact_num
  s.Email_id = email_id
  s.Password = password
  # checking existing -
  check_existing = scholar.objects.filter(Scholar_name=scholar_name) and scholar.objects.filter(Contact_num = contact_num) and scholar.objects.filter(Email_id = email_id) and scholar.objects.filter(Password = password).exists()
  if check_existing:
    messages.error(request,"user already exists !!! try again...")
    return redirect('/login/login-scholar')

  else:
    s.save()
    messages.success(request,'successfully saved..Please login')
    return redirect('/login/login-scholar')

def loginfarmer(request):
  if request.method == "POST":
    emailid = request.POST.get("EmailId")
    password1 = request.POST.get("Logpassword")
  f = farmer()
  f.Email_id = emailid
  f.Password = password1

  # checking existing -
  check_existing =farmer.objects.filter(Email_id = emailid) and farmer.objects.filter(Password = password1).exists()

  if check_existing:
    return render(request,"home/index.html",{})
  else:
    messages.success(request,"please register yourself first....")
    return redirect('/login/farmerlogin')