from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
class TodoView(View):
    def get(self,request):
        return render(request,"todoHome.html")

class TodoList(View):
    def get(self,request):
        data=TodoModel.objects.all()
        return render(request,"todoList.html",{"data":data})

class TodoAdd(View):
    def get(self,request):
        form=TodoAddForm()
        return render(request,"todoAdd.html",{"form":form})
    def post(self,request):
        form_data=TodoAddForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Your task has been added!")
            return redirect('tlist')
        messages.error(request,"Please provide valid inputs!!")
        return render(request,"todoAdd.html",{"form":form_data})

class TodoDelete(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid).delete()
        messages.error(request,"Your task has been deleted!")
        return redirect('tlist')

class TodoUpdate(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid)
        form=TodoUpdateForm(instance=todo)
        return render(request,"todoUpdate.html",{"form":form})
    def post(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid)
        form_data=TodoUpdateForm(data=request.POST,files=request.FILES,instance=todo)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Your changes has been updated!")
            return redirect('tlist')
        messages.error(request,"Please provide valid inputs!!")
        return render(request,"todoUpdate.html",{"form":form_data})

def UpdateStatus(request,**kwargs):
    tid=kwargs.get('id')
    todo=TodoModel.objects.get(id=tid)
    todo.Status="Completed"
    todo.save()
    return redirect('tlist')