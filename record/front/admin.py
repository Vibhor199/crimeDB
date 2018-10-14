from django.contrib import admin
from front.models import Ptype,Pstatus,Person,OffenceEvent,Offender,OffenderOffence,Otypes,Aka,Biometrics,FamilyMember,Inmate,Prison,Trial
#from front.models import Juice
# Register your models here.
#admin.site.register(Juice)
admin.site.register(Ptype)
admin.site.register(Pstatus)
admin.site.register(Person)
admin.site.register(OffenceEvent)
admin.site.register(Offender)
admin.site.register(OffenderOffence)
admin.site.register(Otypes)
admin.site.register(Aka)
admin.site.register(Biometrics)
admin.site.register(FamilyMember)
admin.site.register(Inmate)
admin.site.register(Prison)
admin.site.register(Trial)
