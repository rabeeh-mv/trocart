from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer
def sign_out(request):
    logout(request)
    return redirect('home')
def show_account(request):
    context={}
    if request.method == 'POST' and 'register' in request.POST:
      context['register']=True
      try:
           username = request.POST.get('username')
           email = request.POST.get('email')
           password = request.POST.get('password')
           address = request.POST.get('address')
           phone = request.POST.get('phone')

           # Create user account
           user = User.objects.create_user(
               username=username,
               email=email,
               password=password
           )

           # Create customer account
           customer = Customer.objects.create(
               user=user,
               phone=phone,
               address=address
           )
           success_massage="you are account created successfully"
           messages.success(request,success_massage)
           return redirect('home')
      except Exception as e:
          error_massae="duplicete username or invalide user"
          messages.error(request,error_massae)
    if request.POST and 'login' in request.POST:
        context['register']=False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"you are login successfully")
            return redirect('home')
        else:
            messages.error(request,"invalid user name or passsword ")
    return render(request, 'account.html',context)
