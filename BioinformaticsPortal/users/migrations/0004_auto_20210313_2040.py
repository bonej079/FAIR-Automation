# Generated by Django 3.0.3 on 2021-03-13 08:58

from django.db import migrations, models
from django.core.management.sql import emit_post_migrate_signal

def add_permission(apps, group, name):
    Permission = apps.get_model('auth', 'Permission')
    perm = Permission.objects.get(codename=name)
    group.permissions.add(perm)

def add_permissions(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, db_alias)

    Group = apps.get_model('auth', 'Group')
    group, created = Group.objects.get_or_create(name='contributor')

    if created:
        add_permission(apps, group, 'add_tool')
        add_permission(apps, group, 'change_tool')
        add_permission(apps, group, 'add_pipeline')
        add_permission(apps, group, 'change_pipeline')
        add_permission(apps, group, 'view_pipeline')
        add_permission(apps, group, 'delete_pipeline')

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210313_0958'),
    ]

    operations = [
        migrations.RunPython(add_permissions)
    ]
