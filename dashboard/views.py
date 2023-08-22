from django.shortcuts import render
from .models import Data
from django.db.models import Q
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        #data = Data.objects.filter(first_name__icontains=q) #it will give the double name in single search in same first_name
        #data = Data.objects.filter(last_name__icontains=q) #it will give the double name in single search in same last_name
        multiple_q= Q(Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(age__icontains=q)) #it will give the all the values first_name and last_name and age also 
        data=Data.objects.filter(multiple_q)
    else:
        data = Data.objects.all()
    contest = {'data':data}
    return render(request,'dashboard/index.html',contest)
