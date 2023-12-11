from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
# from django.urls import reverse
from django.views.generic import TemplateView

from accounts.forms import UserRegistrationForm, LoginForm, Reset_Password


class Signup(TemplateView):
    extra_context = {'form':UserRegistrationForm()}
    template_name = 'signup.html'

    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if request.POST['password'] != request.POST['confirm_password']:
                return render(request,'signup.html',context={'form':form,'error':'Password and confirm password does not match'})

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',context={'form':form,'error':'Username already exists'})
            except:
                pass

            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request,'signup.html',context={'form':form,'error':'Email already exists'})
            except:
                pass

            user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            user.save()

            return render(request,'aftersignup.html')
        else:
            return render(request,'signup.html',context={'form':form})


class Login(TemplateView):
    extra_context = {'form': LoginForm()}
    template_name = 'login.html'

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = authenticate(username=request.POST['username'], password=request.POST['password'])

                if user is not None:
                    login(request, user)
                    # Redirect to the homepage URL after successful login
                    return redirect('homepage')  # Replace 'homepage' with the actual URL name of your homepage view
                else:
                    return render(request, 'login.html', context={'form': form, 'error': 'Invalid username or password'})
            except Exception as e:
                # Handle exceptions here, if necessary
                print(e)
        # If the form is not valid or if authentication fails, render the login template with the form and error message
        return render(request, 'login.html', context={'form': form})



def logout_view(request):
    logout(request)
    return redirect('homepage')


def Forgot_password(request):
    form = Reset_Password()

    if request.method == 'POST':
        form = Reset_Password(request.POST)
        if form.is_valid():
            user = User.objects.get(email=request.POST['email'])
            print(user.email)
            user.password = make_password(request.POST['new_password'])
            user.save()





            return redirect('login')
    return render(request, 'password_reset.html', {'form': form})