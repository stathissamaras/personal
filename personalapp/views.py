from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import send_mail, EmailMessage
from django.utils.translation import gettext as _

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Έλεγχος email
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'index.html', {
                'error_message': "Μη έγκυρη διεύθυνση email",
                'name': name,
                'subject': subject,
                'message': message
            })
        
        # Αποστολή email
        send_mail(
            f'Νέο Μήνυμα: {subject}',
            f'Από: {name}\nEmail: {email}\n\nΜήνυμα:\n{message}',
            'info@oileco.gr',
            ['info@oileco.gr'],
            fail_silently=False,
        )
        return render(request, 'index.html', {
            'success_message': "Το μήνυμα στάλθηκε επιτυχώς!"
        })

    return render(request, 'index.html')

def innerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Έλεγχος email
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'inner-page.html', {
                'error_message': "Μη έγκυρη διεύθυνση email",
                'name': name,
                'subject': subject,
                'message': message
            })
        
        # Αποστολή email
        send_mail(
            f'Νέο Μήνυμα: {subject}',
            f'Από: {name}\nEmail: {email}\n\nΜήνυμα:\n{message}',
            'info@oileco.gr',
            ['info@oileco.gr'],
            fail_silently=False,
        )
        return render(request, 'inner-page.html', {
            'success_message': "Το μήνυμα στάλθηκε επιτυχώς!"
        })

    return render(request, 'inner-page.html')