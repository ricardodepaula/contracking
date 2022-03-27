from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required(login_url='/auth/logar/')
def home(request):
    return render(request, 'home.html')