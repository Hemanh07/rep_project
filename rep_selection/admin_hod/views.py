from django.shortcuts import render
from selection_form.models import Student_details
from .select import print_message
# Create your views here.
def hod_login(request):
    return render (request,'admin_login.html')
def hod_login_authendication(request):
    pass
def process_the_result(request):
    student_details_list=Student_details.objects.all()
    print_message(student_details_list)

    