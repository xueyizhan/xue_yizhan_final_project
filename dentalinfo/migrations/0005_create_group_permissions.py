# Generated by Django 4.1 on 2023-05-03 21:22

from __future__ import unicode_literals
from itertools import chain
from django.db import migrations

def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')
    service_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='service')
    patient_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='patient')
    dentist_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='dentist')
    year_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='year')
    month_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='month')
    day_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='day')
    hour_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='hour')
    time_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='time')
    appointment_permissions = permission_class.objects.filter(content_type__app_label = 'dentalinfo', content_type__model='appointment')
    perm_view_service = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='service', codename='view_service')
    perm_view_patient = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='patient', codename='view_patient')
    perm_view_dentist = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='dentist', codename='view_dentist')
    perm_view_year = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='year', codename='view_year')
    perm_view_month = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='month', codename='view_month')
    perm_view_day = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='day', codename='view_day')
    perm_view_hour = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='hour', codename='view_hour')
    perm_view_time = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='time', codename='view_time')
    perm_view_appointment = permission_class.objects.filter(content_type__app_label='dentalinfo', content_type__model='appointment', codename='view_appointment')
    g_client_permissions = chain(perm_view_service, patient_permissions, perm_view_dentist, perm_view_year, perm_view_month,
                                 perm_view_day, perm_view_hour, perm_view_time, perm_view_appointment)
    g_doctor_permissions = chain(perm_view_service, perm_view_patient, dentist_permissions, perm_view_year, perm_view_month,
                                 perm_view_day, perm_view_hour, perm_view_time, perm_view_appointment)
    g_scheduler_permissions = chain(perm_view_service, patient_permissions, dentist_permissions, perm_view_year, perm_view_month,
                                    perm_view_day, perm_view_hour, time_permissions, appointment_permissions)
    g_admin_permissions = chain(service_permissions, patient_permissions, dentist_permissions, year_permissions, month_permissions,
                                day_permissions, hour_permissions, time_permissions, appointment_permissions)

    my_groups_initialization_list = [
        {'name': 'g_client', 'permissions_list': g_client_permissions,},
        {'name': 'g_doctor', 'permissions_list': g_doctor_permissions,},
        {'name': 'g_scheduler', 'permissions_list': g_scheduler_permissions,},
        {'name': 'g_admin', 'permissions_list': g_admin_permissions,},
    ]

    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):

    dependencies = [
        ('dentalinfo', '0004_create_groups'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions_data, remove_group_permissions_data)
    ]
