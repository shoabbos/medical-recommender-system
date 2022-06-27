from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User, auth
from ..models import patient, doctor, diseaseinfo, consultation, rating_review
from apps.chats.models import Chat, Feedback


def rate_review(request,consultation_id):
   if request.method == "POST":
         consultation_obj = consultation.objects.get(id=consultation_id)
         patient = consultation_obj.patient
         doctor1 = consultation_obj.doctor
         rating = request.POST.get('rating')
         review = request.POST.get('review')

         rating_obj = rating_review(patient=patient,
                                    doctor=doctor1,
                                    rating=rating,
                                    review=review)
         rating_obj.save()

         rate = int(rating_obj.rating_is)
         doctor.objects.filter(pk=doctor1).update(rating=rate)
         
         return redirect('consultationview', consultation_id)
