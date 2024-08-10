from django.shortcuts import render
from django.http import HttpResponse

# Home.
def home(request):
    '''View for the home page.'''
    return HttpResponse('Welcome to Auto Hub!')