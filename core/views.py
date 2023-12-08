from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Item
from .forms import SignUpForm,LoginForm
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm,EditForm

def index(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    context={'items':items,'categories':categories}
    return render(request,'core/index.html',context)

def contactPage(request):
    return render(request,'core/contact.html')


def detail(request,pk):
    item=get_object_or_404(Item, pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    context={'item':item,'related_items':related_items}
    return render(request,'core/detail.html',context)

def signupUser(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            form=SignUpForm()
    context={'form':form}
    return render(request, 'core/signup.html',context)


def loginUser(request):
    form=LoginForm()
    context={'form':form}
    
    return render(request,'core/login.html',context)
"""
def logoutUser(request):
    return redirect('home')
"""
@login_required
def newitem(request):
    form=NewItemForm()
    if request.method == "POST":
        form=NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('detail',pk=item.id)
        else: 
            form=NewItemForm()
    context={
        'form':form
    }
    return render(request,'core/form.html',context)

def dashboardthings(request):
    items=Item.objects.filter(created_by=request.user)
    context={'items':items}
    return render(request,'core/dashboard.html',context)

@login_required
def deleteItem(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard')

@login_required
def editItem(request,pk):
    form=EditForm()
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == "POST":
        form=EditForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            form.save()
            return redirect('detail',pk=item.id)
        else: 
            form=EditForm(instance=item)
    context={
        'form':form
    }
    return render(request,'core/form.html',context)