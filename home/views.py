from django.shortcuts import render, redirect, reverse
# from .models import MailingList
from django.contrib import messages
# from .forms import AddToMailingList


def index(request):
    """
    Displays the home page. Post function adds a customer
    entered email to the mailing list.
    """
    # if request.method == 'POST':
    #     mailing_list = MailingList.objects.all()
    #     print(f'mailing list is: {mailing_list}')
    #     form_data = {
    #         'email': request.POST['email'],
    #     }
    #     print(f'the email sudmitted is: {form_data}')
    #     form = AddToMailingList(form_data)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Email address added to mailing list')
    #         return redirect(reverse('home'))
    #     else:
    #         messages.error(request, 'Failed to add email. Please check that you have correctly filled out all required information.')
    #         return redirect(reverse('home'))

    return render(request, 'home/index.html')
