from datetime import datetime

from django.shortcuts import redirect
from django.contrib.auth.models import User

from apps.main_app.models import doctor


def saveddata(request, doctorusername):
    if request.method == 'POST':

        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']
        registration_no = request.POST['registration_no']
        year_of_registration = request.POST['year_of_registration']
        qualification = request.POST['qualification']
        State_Medical_Council = request.POST['State_Medical_Council']
        specialization = request.POST['specialization']

        dobdate = datetime.strptime(dob, '%Y-%m-%d')
        yor = datetime.strptime(year_of_registration, '%Y-%m-%d')

        duser = User.objects.get(username=doctorusername)

        doctor.objects.filter(pk=duser.doctor).update(name=name, dob=dob, gender=gender, address=address,
                                                      mobile_no=mobile_no, registration_no=registration_no,
                                                      year_of_registration=yor, qualification=qualification,
                                                      State_Medical_Council=State_Medical_Council, specialization=specialization)

        return redirect('dviewprofile', doctorusername)
