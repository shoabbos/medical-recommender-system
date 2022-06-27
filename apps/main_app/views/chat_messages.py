from django.shortcuts import render
from apps.chats.models import Chat


def chat_messages(request):
    if request.method == "GET":

        consultation_id = request.session['consultation_id']

        c = Chat.objects.filter(consultation_id=consultation_id)
        return render(request, 'consultation/chat_body.html', {'chat': c})
