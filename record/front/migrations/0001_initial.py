# Generated by Django 2.1.2 on 2018-11-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='OffenceEvent',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('motive', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('l_street', models.CharField(blank=True, max_length=255, null=True)),
                ('l_city', models.CharField(blank=True, max_length=100, null=True)),
                ('l_state', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'offence_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OffenderOffence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'offender_offence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Otypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'otypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=70, null=True)),
                ('mname', models.CharField(blank=True, max_length=70, null=True)),
                ('lname', models.CharField(blank=True, max_length=70, null=True)),
                ('r_street', models.CharField(blank=True, max_length=255, null=True)),
                ('r_city', models.CharField(blank=True, max_length=100, null=True)),
                ('r_state', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'person',
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
            name='Pstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'pstatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ptype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'ptype',
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
        migrations.CreateModel(
            name='Biometrics',
            fields=[
                ('pid', models.OneToOneField(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='front.Person')),
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
            name='Offender',
            fields=[
                ('opid', models.OneToOneField(db_column='opid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='offender', serialize=False, to='front.Person')),
                ('born', models.DateField(blank=True, null=True)),
                ('died', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'offender',
                'managed': False,
            },
        ),
    ]
