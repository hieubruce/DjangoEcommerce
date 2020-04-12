from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, get_user_model

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
    content={
        'title':'Hello World!',
        'content':'Wellcome to the home page.'
    }
    if request.user.is_authenticated:
        content['premium_content'] = 'YEAHHHH'
    return render(request, 'home_page.html', content)

def about_page(request):
    content={
        'title':'About page',
        'content':'Wellcome to the about page'
    }
    return render(request, 'home_page.html', content)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    content={
        'title':'Contact',
        'content':'Wellcome to the contact page.',
        'form': contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    return render(request, 'contact/view.html', content)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form':form}
    print('User logged in')
    if form.is_valid():

        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            context['form'] = LoginForm()
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            print('Error')

    return render(request,'auth/login.html', context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request,'auth/register.html', context)
