from django.shortcuts import render
from.models import Student_details
# Create your views here.
def form(request):
    return render (request,'index.html')
def result(request):
    name=request.POST['name'].upper()
    year =request.POST['class']
    degree=request.POST['degree']
    responsibilities=request.POST['responsibilities'].split(',')
    
    if 'rep' in  request.POST :
        rep_before=request.POST['rep']
    else :rep_before=False
    if 'have_responsibilties' in  request.POST :
        have_responsibilities=request.POST['have_responsibilties']
    else :have_responsibilities=False
    user=Student_details()
    user.name=name
    user.Class=degree
    user.year=year
    user.rep_before=rep_before
    user.responsibilities=responsibilities
    user.have_responsibilities=have_responsibilities
    print(name,degree,year,rep_before,responsibilities,have_responsibilities)
    
    user.save()
    return render (request,'result.html',{'name':name})
    