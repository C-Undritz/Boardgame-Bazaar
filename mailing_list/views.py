from django.shortcuts import render, redirect, reverse
from .models import MailingList
from django.contrib import messages
from .forms import AddToMailingList


def save_email(request):
    """
    Adds customer entered email to the mailing list database table.
    Function performs check on database to ensure that email address
    entered is not already stored.
    """
    if request.method == 'POST':
        form_data = {
            'email': request.POST['email'],
        }
        email = request.POST['email']
        form = AddToMailingList(form_data)
        mailinglist_status = MailingList.objects.all().filter(email=email).exists()
        if mailinglist_status:
            messages.info(request, 'Email already stored in mailing list')
            return redirect(reverse('home'))
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Email address added to mailing list')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Failed to add email. Please check that you have correctly filled out all required information.')
                return redirect(reverse('home'))
