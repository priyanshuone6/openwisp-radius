# Generated by Django 3.0.7 on 2020-07-05 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_radius', '0005_remove_null_uuid_field'),
    ]

    operations = [
        migrations.RenameField(model_name='nas', old_name='uuid', new_name='id',),
        migrations.RenameField(
            model_name='radiuscheck', old_name='uuid', new_name='id',
        ),
        migrations.RenameField(
            model_name='radiusgroupcheck', old_name='uuid', new_name='id',
        ),
        migrations.RenameField(
            model_name='radiusgroupreply', old_name='uuid', new_name='id',
        ),
        migrations.RenameField(
            model_name='radiuspostauth', old_name='uuid', new_name='id',
        ),
        migrations.RenameField(
            model_name='radiusreply', old_name='uuid', new_name='id',
        ),
        migrations.RenameField(
            model_name='radiususergroup', old_name='uuid', new_name='id',
        ),
    ]
