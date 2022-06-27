from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth


def sign_in_patient(request):
    if request.method == 'POST':
          username, password =  request.POST.get('username'), request.POST.get('password')
          user = auth.authenticate(username=username,password=password)

          if user:
              try:
                 if ( user.patient.is_patient == True ) :
                     auth.login(request,user)

                     request.session['patientusername'] = user.username

                     return redirect('patient_ui')
               
              except :
                  messages.info(request,'invalid credentials')
                  return redirect('sign_in_patient')

          else :
             messages.info(request,'invalid credentials')
             return redirect('sign_in_patient')

    else :
      return render(request, 'patient/signin_page/index.html')
