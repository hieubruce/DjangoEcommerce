from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, get_user_model

from .forms import ContactForm

def home_page(request):
    content={
        'content':'Wellcome to the home page.'
    }
    if request.user.is_authenticated:
        content['premium_content'] = 'User LOGIN'
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
        'title':'Liên hệ',
        'form': contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({'message':'Thank you for your submission'})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return JsonResponse(errors, status=400, content_type = 'application/json')

    return render(request, 'contact/view.html', content)
