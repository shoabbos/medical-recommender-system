from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User, auth
from ..models import patient, doctor, diseaseinfo, consultation, rating_review
from apps.chats.models import Chat, Feedback


def doctor_ui(request):

    if request.method == 'GET':

      doctorusername = request.session['doctorusername']
      duser = User.objects.get(username=doctorusername)
      doctor_obj = duser.doctor
        
      consultationnew = consultation.objects.filter(doctor = doctor_obj)

      doctorid = request.session['doctorusername']
      duser = User.objects.get(username=doctorid)
    
      return render(request,'doctor/doctor_ui/profile.html',
                    {"duser": duser,
                    "consultation": consultationnew})
