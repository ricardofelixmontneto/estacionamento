# Generated by Django 4.2.6 on 2023-10-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_movmensalista'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='name',
            new_name='nome',
        ),
    ]