from django.shortcuts import render, redirect

def home(request):
    """Sends the user to the home page"""
    return render(request, 'home.html', {})
