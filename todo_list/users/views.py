from django.shortcuts import render, redirect
from .forms import UserSigninForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserSigninForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account is created for {username}')
            return redirect('signin')
    else:
        form = UserSigninForm()
        
    return render(request, template_name='users/signup.html', context={"form":form})
