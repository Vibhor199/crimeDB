# Generated by Django 2.1.2 on 2018-10-12 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_offenceevent_offender_offenderoffence_otypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'aka',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Biometrics',
            fields=[
                ('opid', models.OneToOneField(db_column='opid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='front.Offender')),
                ('bloodgroup', models.CharField(blank=True, max_length=5, null=True)),
                ('sex', models.CharField(blank=True, max_length=1, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('hair', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('eye', models.CharField(blank=True, max_length=20, null=True)),
                ('skin', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'biometrics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'family_member',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inmate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellno', models.IntegerField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('misdemenour', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inmate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prison',
            fields=[
                ('prid', models.AutoField(primary_key=True, serialize=False)),
                ('staffcount', models.IntegerField(blank=True, null=True)),
                ('a_street', models.CharField(blank=True, max_length=255, null=True)),
                ('a_city', models.CharField(blank=True, max_length=100, null=True)),
                ('a_state', models.CharField(blank=True, max_length=100, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'prison',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('verdict', models.CharField(default='NA', max_length=255)),
            ],
            options={
                'db_table': 'trial',
                'managed': False,
            },
        ),
    ]
