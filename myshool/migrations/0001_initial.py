# Generated by Django 5.1.1 on 2024-09-18 13:52

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('school_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trimestres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eleves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Matieres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('coef', models.IntegerField()),
                ('classe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.classes')),
                ('prof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.profs')),
            ],
        ),
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('code', models.CharField(blank=True, max_length=6, null=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Interros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshool.eleves')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshool.matieres')),
                ('prof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.profs')),
                ('trimestre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.trimestres')),
            ],
        ),
        migrations.CreateModel(
            name='Devoirs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshool.eleves')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshool.matieres')),
                ('prof', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.profs')),
                ('trimestre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myshool.trimestres')),
            ],
        ),
    ]
