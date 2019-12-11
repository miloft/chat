from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
    path('', login_required(views.DialogsView.as_view()), name='dialogs'),
    url(r'^create/(?P<user_id>\d+)/$', login_required(views.CreateDialogView.as_view()), name='create_dialog'),
    url(r'^(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
]