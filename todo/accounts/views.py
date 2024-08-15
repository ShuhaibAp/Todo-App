from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,FormView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm
    def post(self,request):
        form_data=LoginForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                messages.success(request,"Login Successfull!")
                return redirect('tlist')
            else:
                messages.warning(request,"Invalid username or password!!")
                return redirect('log')
        return render(request,"login.html",{"form":form_data})

class RegView(CreateView):
    template_name="registration.html"
    form_class=RegForm
    success_url=reverse_lazy('log')
    
    