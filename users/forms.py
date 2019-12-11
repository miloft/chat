from django.forms import ModelForm
import django.forms as forms
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
