from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User, auth
from ..models import patient, doctor, diseaseinfo, consultation, rating_review
from apps.chats.models import Chat, Feedback

from .home import home
from .admin_ui import admin_ui
from .patient_ui import patient_ui
from .post import post
from .pviewprofile import pviewprofile
from .dconsultation_history import dconsultation_history
from .dviewprofile import dviewprofile
from .consultationview import consultationview
from .doctor_ui import doctor_ui
from .consult_a_doctor import consult_a_doctor
from .chat_messages import chat_messages
from .rate_review import rate_review
from .make_consultation import make_consultation
from .checkdisease import checkdisease
from .pconsultation_history import pconsultation_history
from .close_consultation import close_consultation
