from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
import re
import random

# Create your views here.
def index(request):

    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        invalid_input = ['', ' ']
        if name in invalid_input or email in invalid_input or phone in invalid_input or message in invalid_input:
            messages.error(request, 'One or more fields are empty!')
        else:
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_pattern = re.compile(r'^[0-9]{10}$')

            if email_pattern.match(email) and phone_pattern.match(phone):
                form_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'message': message,
                }
                message_body = '''
                From:\n\t\t{}\n
                Message:\n\t\t{}\n
                Email:\n\t\t{}\n
                Phone:\n\t\t{}\n
                '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['phone'])
                send_mail('You got a mail!', message_body, '', ['dev.ash.py@gmail.com'])
                messages.success(request, 'Your message was sent.')
            else:
                messages.error(request, 'Email or Phone is Invalid!')
    return render(request, 'contact.html', {})


