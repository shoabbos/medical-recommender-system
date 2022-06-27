from django.shortcuts import render, redirect

from apps.chats.models import Feedback


def admin_ui(request):
    if request.method == 'GET':
        if request.user.is_authenticated:

            auser = request.user
            Feedbackobj = Feedback.objects.all()

            return render(request, 'admin/admin_ui/admin_ui.html', {"auser": auser, "Feedback": Feedbackobj})

        else:
            return redirect('home')

    if request.method == 'POST':
        return render(request, 'patient/patient_ui/profile.html')
