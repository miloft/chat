# -*- coding: utf-8 -*-
from urllib.parse import urlparse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth
from django.template.context_processors import csrf
from django.urls import reverse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.utils.http import is_safe_url, urlunquote
from .forms import RegisterForm
from users import models


def get_next_url(request):
    next = request.META.get('HTTP_REFERER')
    if next:
        next = urlunquote(next)
    if not is_safe_url(url=next, allowed_hosts=request.get_host()):
        next = '/'
    return next


class ELoginView(View):

    def get(self, request):
        if auth.get_user(request).is_authenticated:
            return redirect('/dialogs/')
        else:
            context = create_context_username_csrf(request)
            return render(request, 'accounts/login.html', context=context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            next = urlparse(get_next_url(request)).path
            return redirect(next)
        context = create_context_username_csrf(request)
        context['login_form'] = form
        return render(request, 'accounts/login.html', context=context)


def create_context_username_csrf(request):
    context = {}
    context.update(csrf(request))
    context['login_form'] = AuthenticationForm
    return context


def log_out(request):
    logout(request)
    return redirect('/accounts/login/')


def forward(request):
    return redirect('/accounts/login/')


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            name = form.cleaned_data['username']
        user = models.User.objects.create_user(password=password, username=name)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    else:
        form = RegisterForm()
    return render(request, 'accounts/registration.html', {'form': form})
