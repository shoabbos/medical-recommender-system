from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth


def sign_in_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            try:
                if (user.is_superuser == True):
                    auth.login(request, user)

                    return redirect('admin_ui')
            except:
                messages.info(request, 'Please enter the correct username and password for a admin account.')
                return redirect('sign_in_admin')

        else:
            messages.info(request, 'Please enter the correct username and password for a admin account.')
            return redirect('sign_in_admin')

    else:
        return render(request, 'admin/signin/signin.html')
