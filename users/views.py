from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from users.forms import MessageForm
from .models import Chat, Message


class DialogsView(View):
    def get(self, request):
        users_list = User.objects.all().filter(is_superuser__exact=0).exclude(id__exact=request.user.id)
        chats = Chat.objects.filter(members__in=[request.user.id])
        unreaded = {}
        for chat in chats:
            unreaded[chat.id] = (Message.objects.filter(is_readed__exact=False, chat_id__exact=chat.id).exclude(
                author_id__exact=request.user.id).count())
        context = {
            'user_profile': request.user,
            'chats': chats,
            'unrdms': unreaded,
            'users': users_list
        }

        return render(request, 'users/dialogs.html', context)

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id])
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        id = str(chat.id)
        url = '/dialogs/' + id + '/'
        return HttpResponseRedirect(url)


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None
        context = {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm(),
        }
        return render(request, 'users/messages.html', context)

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
            url = '/dialogs/'+chat_id+'/'
            return HttpResponseRedirect(url)
        context = {'chat_id': chat_id}
        return render(request, 'users/messages.html', context=context)
