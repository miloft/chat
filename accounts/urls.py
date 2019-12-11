# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', views.ELoginView.as_view(), name='login'),
    path('', views.forward),
    url(r'^logout/$', views.log_out),
    url(r'^dialogs/', include('users.urls')),
    url(r'^registration/$', views.registration), # пока не работает
]