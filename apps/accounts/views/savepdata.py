from django.shortcuts import redirect

from apps.main_app.models import patient
from datetime import datetime

from ..services import get_user_by_username


def savepdata(request, patientusername):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        mobile_no = request.POST['mobile_no']
        print(dob)
        dobdate = datetime.strptime(dob, '%Y-%m-%d')

        puser = get_user_by_username(patientusername)

        patient.objects.filter(pk=puser.patient).update(name=name, dob=dobdate, gender=gender,
                                                        address=address, mobile_no=mobile_no)

        return redirect('pviewprofile', patientusername)
