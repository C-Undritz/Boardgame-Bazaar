"""
Boardgame Bazaar: mailing_list App - Views
"""


from django.shortcuts import redirect, reverse
from django.contrib import messages
from .models import MailingList
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
        if MailingList.objects.all().filter(email=email).exists():
            messages.info(request, 'Email already stored in mailing list')
            return redirect(reverse('home'))
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'Email address added to mailing \
                    list')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Failed to add email. Please check \
                    that you have correctly filled out all required \
                        information.')
                return redirect(reverse('home'))
