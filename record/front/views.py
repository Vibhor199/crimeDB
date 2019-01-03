from django.shortcuts import render, HttpResponse
from front.models import *
from django.db.models import Count
from django.db import connection
import json
# Create your views here.
def getcdat(request):
    if request.method == 'POST':
        city=request.POST['city']
        #OffenceEvent.objects.filter(l_city=city).count()
        cursor = connection.cursor()
        cursor.execute('SELECT YEAR(date), COUNT(YEAR(date)) FROM offence_event where l_city="'+city+'" GROUP BY YEAR(date)')
        row=cursor.fetchall()
        ans={}
        for r in row:
            ans[r[0]]=r[1]
        print(ans)
    return HttpResponse(json.dumps(ans))
def front(request):
    s=OffenceEvent.objects.values('l_state').distinct()
    sc={}
    for i in s:
        ci={}
        for a in OffenceEvent.objects.filter(l_state=i['l_state']).values('l_city').distinct():
            ci[str(a['l_city'])]=0
        sc[str(i['l_state'])]=ci
    print(sc)
    args={
        'states':s,
        'sc':sc
    }
    return render(request, 'front.html', args)

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
def inperson(request):
    if request.method == 'POST':
        print(ok)
