from django.shortcuts import render, redirect

from ..services import get_all_feedbacks


def get_feedback(request):
    if request.method == "GET":
        obj = get_all_feedbacks()
        return redirect(request, 'consultation/chat_body.html',
                        {"obj": obj})
