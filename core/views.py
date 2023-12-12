from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Item,ConversationMessage,Conversation
from .forms import SignUpForm,LoginForm,ConversationMessageForm
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditForm
from django.db.models import Q

def browse(request):
    query=request.GET.get('query','')
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    context={'items':items,
             'query':query,
             'categories':categories,
             'category_id':int(category_id)
             }

    return render(request,'core/browser.html',context)

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


def new_message(request ,item_pk):
    item=get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('home')
    
    conversations=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation', pk=conversations.first().id)

    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            return redirect('detail',pk=item_pk)
        
    else:
        form=ConversationMessageForm()
    context={'form':form}
    return render(request,'core/new.html',context)

def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user.id])
    context={'conversations':conversations}
    return render(request,'core/inbox.html',context)

def detail_con(request,pk):
    conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    form=ConversationMessageForm()
    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation',pk=pk)
        else:
            form=ConversationMessageForm()
        
    context = {'conversation': conversation,
               'form':form}
    return render(request, 'core/conversation.html', context)