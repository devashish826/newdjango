# Generated by Django 3.1.2 on 2020-10-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0012_modulestack_parent_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulestack',
            name='parent_module',
        ),
    ]