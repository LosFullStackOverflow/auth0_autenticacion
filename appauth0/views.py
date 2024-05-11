from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from autentication.auth0backend import getRole

@login_required
def landing_page(request):
    return render(request, 'index.html')