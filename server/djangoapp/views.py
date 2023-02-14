
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
import logging
import json

from .form import RegistrationForm

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
def login_request(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                messages.warning(request, 'Both username and password are required.')
                return HttpResponseRedirect(reverse('djangoapp:login'))

            user_obj = User.objects.filter(username=username).first()

            if user_obj is None:
                messages.warning(request, 'User not found')
                return HttpResponseRedirect(reverse('djangoapp:login'))

            user = authenticate(request, username=username, password=password)

            if user is None:
                messages.warning(request, 'Worng password.')
                return HttpResponseRedirect(reverse('djangoapp:login'))

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('djangoapp:login'))
    except Exception as e:
        print(e)
    return render(request, 'djangoapp/login.html')

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    messages.success(request, 'You have just logout of your account')
    return render(request, 'djangoapp/login.html')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get('username')
            messages.success(request, 'Account for ' + username + ' was created.')
            return HttpResponseRedirect(reverse('djangoapp:login'))
    else:
        form = RegistrationForm()
        context = {"form": form}
        return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

