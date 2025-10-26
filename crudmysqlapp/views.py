from django.shortcuts import render,redirect
from crudmysqlapp.forms import UserForm
from django.http import HttpResponse
from crudmysqlapp.models import User

# Create your views here.

def insert(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
         form.save()
         return HttpResponse("<h2>Data inserted into Database</h2>")
    else:        
        form=UserForm()
    return render(request,'index.html',{'form':form})


def show(request):
    users=User.objects.all()
    return render(request,'show.html',{'users':users})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def edit(request,id):
    user=User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})

def update(request,id):
    user=User.objects.get(id=id)
    form=UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user':user})


