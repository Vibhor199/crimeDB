from django.shortcuts import render, HttpResponse
from front.models import *
# Create your views here.
def front(request):
    return render(request, 'front.html')

def entry(request):
    ptypes=Ptype.objects.all()
    pstatus=Pstatus.objects.all()
    persons=Person.objects.all()
    offenders=Offender.objects.all()
    otypes=Otypes.objects.all()
    oo=OffenderOffence.objects.all()
    oe=OffenceEvent.objects.all()
    args={
    'ptypes': ptypes,
    'pstatus': pstatus,
    'persons': persons,
    'offenders': offenders,
    'otypes': otypes,
    'oe': oe,
    'oo':oo 
    }
    return render(request, 'entry.html' , args)

def inptype(request):
    if request.method == 'POST':
        typ=request.POST['ptype']
        p=Ptype(
            description= typ
        )
        p.save()
        return HttpResponse('')
def inotype(request):
    if request.method == 'POST':
        typ=request.POST['otype']
        p=Otypes(
            description= typ
        )
        p.save()
        return HttpResponse('')
