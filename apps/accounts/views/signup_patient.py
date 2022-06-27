from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from apps.main_app.models import patient


def signup_patient(request):
    if request.method == 'POST':
      if request.POST['username'] and \
        request.POST['email'] and \
        request.POST['name'] and \
        request.POST['dob'] and \
        request.POST['gender'] and \
        request.POST['address'] and \
        request.POST['mobile'] and \
        request.POST['password'] and \
        request.POST['password1']:

          username =  request.POST['username']
          email =  request.POST['email']

          name =  request.POST['name']
          dob =  request.POST['dob']
          gender =  request.POST['gender']
          address =  request.POST['address']
          mobile_no = request.POST['mobile']
          password =  request.POST.get('password')
          password1 =  request.POST.get('password1')

          if password == password1:
              if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('signup_patient')

              elif User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect('signup_patient')
                
              else :
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                
                patientnew = patient(user=user,name=name,dob=dob,gender=gender,address=address,mobile_no=mobile_no)
                patientnew.save()
                messages.info(request,'user created sucessfully')
                
              return redirect('sign_in_patient')

          else:
            messages.info(request,'password not matching, please try again')
            return redirect('signup_patient')

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect('signup_patient') 
    else :
      return render(request,'patient/signup_Form/signup.html')
