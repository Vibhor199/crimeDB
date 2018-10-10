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


class Pstatus(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pstatus'


class Ptype(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptype'
