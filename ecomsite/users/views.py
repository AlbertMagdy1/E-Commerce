from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account was created successfully')
            return redirect('main')

    else:
        form = RegisterForm()
    
    return render(request,'user/register.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.warning(request,'Logged Out Successfully')
    return redirect('main')


def profilepage(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please login first")
        return redirect('/login/')
    return render (request, 'user/profile.html')


class CustomLoginView(LoginView):
    def form_valid(self,form):
        username = form.get_user().username.capitalize()
        messages.success(self.request, f'Welcome back {username}')
        return super().form_valid(form)
    
    


