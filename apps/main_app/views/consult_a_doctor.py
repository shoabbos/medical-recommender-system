from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User, auth
from ..models import patient, doctor, diseaseinfo, consultation, rating_review
from apps.chats.models import Chat, Feedback


def consult_a_doctor(request):
    if request.method == 'GET':
   
        doctortype = request.session['doctortype']
        print(doctortype)
        dobj = doctor.objects.all()

        return render(request,'patient/consult_a_doctor/consult_a_doctor.html',
                      {"dobj": dobj})
