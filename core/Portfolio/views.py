from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    """Contact view that process the form data
    and sends an email to the owner
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')

        subject = f"This email was sent by {name} with email {email}"

        full_msg = request.POST.get('textarea')

        if not name or not email or not full_msg:
            messages.error(request, "Please fill in the fields")
            return redirect('contact')
        try :
            send_mail(
                subject=subject,
                message=full_msg, from_email=email,
                recipient_list=[settings.DEFAULT_FROM_EMAIL]
            )
            messages.success(request, message="You have succesfully sent the message")
            return redirect('contact')
        
        except Exception as e:
            messages.error(request, message=f"An error occured {e}")
            return redirect('contact')

    return render(request, "contact.html")
