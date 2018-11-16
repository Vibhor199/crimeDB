# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    type = models.ForeignKey('Ptype', models.DO_NOTHING, db_column='type', blank=True, null=True)
    fame = models.CharField(max_length=70, blank=True, null=True)
    mname = models.CharField(max_length=70, blank=True, null=True)
    lname = models.CharField(max_length=70, blank=True, null=True)
    r_street = models.CharField(max_length=255, blank=True, null=True)
    r_city = models.CharField(max_length=100, blank=True, null=True)
    r_state = models.CharField(max_length=100, blank=True, null=True)
    status = models.ForeignKey('Pstatus', models.DO_NOTHING, db_column='status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'

    def __str__(self):
        return str(self.pid)+". "+self.fame+" "+self.lname


class Pstatus(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pstatus'

    def __str__(self):
        return self.description


class Ptype(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptype'

    def __str__(self):
        return self.description

class OffenceEvent(models.Model):
    oid = models.AutoField(primary_key=True)
    type = models.ForeignKey('Otypes', models.DO_NOTHING, db_column='type', blank=True, null=True)
    victimpid = models.ForeignKey('Person', models.DO_NOTHING, db_column='victimpid', blank=True, null=True, related_name='victimpid')
    motive = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    witnesspid = models.ForeignKey('Person', models.DO_NOTHING, db_column='witnesspid', blank=True, null=True, related_name='witnesspid')
    l_street = models.CharField(max_length=255, blank=True, null=True)
    l_city = models.CharField(max_length=100, blank=True, null=True)
    l_state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offence_event'

    def __str__(self):
        return str(self.oid)


class Offender(models.Model):
    opid = models.OneToOneField('Person', models.DO_NOTHING, db_column='opid', primary_key=True, related_name='offender')
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offender'

    def __str__(self):
        return str(self.opid.pid)+". "+self.opid.fame+" "+self.opid.lname

class OffenderOffence(models.Model):
    oid = models.ForeignKey(OffenceEvent, models.DO_NOTHING, db_column='oid', blank=True, null=True)
    opid = models.ForeignKey(Offender, models.DO_NOTHING, db_column='opid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offender_offence'
        unique_together = (('oid', 'opid'),)

class Otypes(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otypes'

    def __str__(self):
        return self.description

class Aka(models.Model):
    opid = models.ForeignKey('Offender', models.DO_NOTHING, db_column='opid', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aka'
        unique_together = (('opid', 'name'),)

class Biometrics(models.Model):
    opid = models.OneToOneField('Offender', models.DO_NOTHING, db_column='opid', primary_key=True)
    bloodgroup = models.CharField(max_length=5, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    hair = models.CharField(max_length=20, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    eye = models.CharField(max_length=20, blank=True, null=True)
    skin = models.CharField(max_length=20, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'biometrics'

class FamilyMember(models.Model):
    fmpid = models.ForeignKey('Person', models.DO_NOTHING, db_column='fmpid', blank=True, null=True)
    opid = models.ForeignKey('Offender', models.DO_NOTHING, db_column='opid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'family_member'
        unique_together = (('fmpid', 'opid'),)

class Inmate(models.Model):
    opid = models.ForeignKey('Offender', models.DO_NOTHING, db_column='opid', blank=True, null=True)
    ioid = models.ForeignKey('OffenceEvent', models.DO_NOTHING, db_column='ioid', blank=True, null=True)
    prid = models.ForeignKey('Prison', models.DO_NOTHING, db_column='prid', blank=True, null=True)
    cellno = models.IntegerField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    misdemenour = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmate'
        unique_together = (('opid', 'prid', 'ioid', 'startdate'),)

class Prison(models.Model):
    prid = models.AutoField(primary_key=True)
    staffcount = models.IntegerField(blank=True, null=True)
    inchargeid = models.ForeignKey(Person, models.DO_NOTHING, db_column='inchargeid', blank=True, null=True)
    a_street = models.CharField(max_length=255, blank=True, null=True)
    a_city = models.CharField(max_length=100, blank=True, null=True)
    a_state = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prison'

class Trial(models.Model):
    tid = models.AutoField(primary_key=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    verdict = models.CharField(max_length=255, default='NA', editable=True)
    opid = models.ForeignKey(Offender, models.DO_NOTHING, db_column='opid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trial'
