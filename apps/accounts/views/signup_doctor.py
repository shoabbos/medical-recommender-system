from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from apps.main_app.models import doctor
  

def signup_doctor(request):

    if request.method == 'GET':
       return render(request, 'doctor/signup_Form/signup.html')

    if request.method == 'POST':
      if request.POST['username'] and request.POST['email'] and request.POST['name'] \
        and request.POST['dob'] and request.POST['gender'] and request.POST['address'] \
        and request.POST['mobile'] and request.POST['password']and request.POST['password1'] \
        and  request.POST['registration_no'] and  request.POST['year_of_registration'] \
        and request.POST['qualification'] and  request.POST['State_Medical_Council'] and  request.POST['specialization'] :

          username =  request.POST['username']
          email =  request.POST['email']

          name =  request.POST['name']
          dob =  request.POST['dob']
          gender =  request.POST['gender']
          address =  request.POST['address']
          mobile_no = request.POST['mobile']
          registration_no =  request.POST['registration_no']
          year_of_registration =  request.POST['year_of_registration']
          qualification =  request.POST['qualification']
          State_Medical_Council =  request.POST['State_Medical_Council']
          specialization =  request.POST['specialization']
          
          password =  request.POST.get('password')
          password1 =  request.POST.get('password1')

          if password == password1:
              if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('signup_doctor')

              elif User.objects.filter(email = email).exists():
                messages.info(request,'email already taken')
                return redirect('signup_doctor')
                
              else :
                user = User.objects.create_user(username=username,password=password,email=email)   
                user.save()
                
                doctornew = doctor(user=user, name=name, dob=dob, gender=gender, address=address, \
                  mobile_no=mobile_no, registration_no=registration_no, year_of_registration=year_of_registration, \
                  qualification=qualification, State_Medical_Council=State_Medical_Council, specialization=specialization )
                doctornew.save()
                messages.info(request,'user created sucessfully')
                print("doctorcreated")
                
              return redirect('sign_in_doctor')

          else:
            messages.info(request,'password not matching, please try again')
            return redirect('signup_doctor')

      else :
        messages.info(request,'Please make sure all required fields are filled out correctly')
        return redirect('signup_doctor') 
