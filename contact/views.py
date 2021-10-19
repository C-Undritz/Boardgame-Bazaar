from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



def contact(request):
    """
    Displays the contact us form and sends email upon post function.
    """
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message_email,
            message,
            [settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, 'Thank you for your message. We will be in \
            contact soon.')
        return redirect(reverse('contact'))
    else:
        return render(request, 'contact/contact.html')
