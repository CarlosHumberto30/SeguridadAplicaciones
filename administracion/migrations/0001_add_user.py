# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-24 15:30
from __future__ import unicode_literals

from django.db import migrations
import datetime
from  django.contrib.auth.models import User,Group


def create_superuser(apps, schema_editor):
    rol = Group.objects.all()
    if not rol:
        grupoadministracion = Group.objects.create(name='Administrador')


    username = 'Admin'
    email = 'admin@sisap.com'
    password = 'Admin123'
    first_name = 'Admin'
    last_name = 'Admin'
    last_login = datetime.datetime.now()
    user = User.objects.create_user(username=username, email=email, password=password,last_login=last_login)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.first_name = first_name
    user.last_name = last_name
    user.groups.add(grupoadministracion.id)
    user.save()





class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_superuser)
    ]