from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth


def sign_in_doctor(request):

    if request.method == 'GET':
        return render(request, 'doctor/signin_page/index.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                if (user.doctor.is_doctor == True):
                    auth.login(request, user)

                    request.session['doctorusername'] = user.username

                    return redirect('doctor_ui')
            except:
                messages.info(request, 'invalid credentials')
                return redirect('sign_in_doctor')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('sign_in_doctor')
    else:
        return render(request, 'doctor/signin_page/index.html')
