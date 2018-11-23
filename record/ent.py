from front.models import *
import sys,random
import datetime as dt
#insertion in PERSON
'''
ldi=[]
file=open("name.txt","r")
for line in file:
    s=line.split()
    if(len(s)==2):
        ldi.append({"fname":s[0],"mname":"","lname":s[1]})
    if(len(s)==3):
        ldi.append({"fname":s[0],"mname":s[1],"lname":s[2]})
#print(ldi)
file=open("city.txt","r")
c=[]
for line in file:
    c.append(line.strip())
for d in ldi:
    d["city"]=c[random.randint(0,(len(c)-1))]
    d["state"]="Karnataka"
    d["ptype"]=random.randint(1,7)

for d in ldi:
    v=Person.objects.create(type=Ptype.objects.get(id=d["ptype"]),fname=d["fname"],mname=d["mname"],lname=d["lname"],r_city=d["city"],r_state=d["state"])
'''
#insertion in offender
'''
for i in Person.objects.filter(type=Ptype.objects.get(description='OFFENDER')):
    yearb = random.randint(1950, 2001)
    monthb = random.randint(1, 12)
    dayb = random.randint(1, 28)
    bdate = datetime(yearb, monthb, dayb)
    Offender.objects.create(opid=i,born=bdate)
'''
'''
file=open("crim.txt","r")
c=[]
for line in file:
    c.append(line.strip())
for cr in c:
    Otypes.objects.create(description=cr)
'''
#insertion in oevent
'''
o=Offender.objects.all()
lo=len(o)-1
v=Person.objects.filter(type=Ptype.objects.get(description='VICTIM'))
lv=len(v)-1
print(v)
t=Otypes.objects.all()
lt=len(t)-1

for i in range(2000):
        ty=t[random.randint(0,lt)]
        vi=v[random.randint(0,lv)]

        year = random.randint(1990, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

        da = dt.datetime(year, month, day)
        ti=dt.time(random.randint(0, 23),random.randint(0, 59),0)
        OffenceEvent.objects.create(type=ty,victimpid=vi, date=da,time=ti,l_city=vi.r_city,l_state=vi.r_state)
'''
