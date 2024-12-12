from django.contrib.auth import login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.utils import timezone 
from django.shortcuts import render, redirect
from .forms import sounakusers
# from .models import UserProfile
from django.contrib import messages
from chattings.models import Department,Replies,Chats
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.models import User
from .utils.gravatar import get_gravatar_url


def count_user_images(user):
    
    chat_images_count = Chats.objects.filter(user=user).exclude(image__isnull=True).exclude(image__exact='').count()
    reply_images_count = Replies.objects.filter(user=user).exclude(image__isnull=True).exclude(image__exact='').count()
    return chat_images_count + reply_images_count

def count_user_pdfs(user):

    chat_images_count = Chats.objects.filter(user=user).exclude(pdf__isnull=True).exclude(pdf__exact='').count()
    
    reply_images_count = Replies.objects.filter(user=user).exclude(pdf__isnull=True).exclude(pdf__exact='').count()
    
    return chat_images_count + reply_images_count

def account(request,user_id):
    user = get_object_or_404(User,id=user_id)
    user_email = user.email  
    gravatar_url = get_gravatar_url(user_email, size=100) 
    chats_count = Chats.objects.filter(user=user).count()
    replies_count = Replies.objects.filter(user=user).count()
    image_count  = Chats.objects.filter(user=user).exclude(image__isnull=True).exclude(image__exact='').count()
    pdf_count = Chats.objects.filter(user=user).exclude(pdf__isnull=True).exclude(pdf__exact='').count()
    return render(request,'myaccount.html',{'user':user,'chats_count':chats_count,'replies_count':replies_count,'gravatar_url':gravatar_url,'image_count':image_count,'pdf_count':pdf_count})

def home(request):
    departments = Department.objects.all()
    return render(request,'home.html',{'departments':departments})

def basenew(request):
    return render(request,'basenew.html')


def signup(request):
    if request.method == 'POST':
        form = sounakusers(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = sounakusers()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request) 
    return redirect('base') 