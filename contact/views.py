from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def contact(request):
    """
    Displays the contact us form and sends email to company email address upon
    POST function.
    """
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        subject = render_to_string(
            'contact/contact_emails/contact_email_subject.txt',
            {'message_name': message_name,
             'message_subject': message_subject})

        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt',
            {'message_email': message_email,
             'message': message,
             'message_name': message_name})

        send_mail(
            subject,
            body,
            message_email,
            [settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(
            request, 'Thank you for your message. We will be in contact soon.')
        return redirect(reverse('contact'))
    else:
        return render(request, 'contact/contact.html')
