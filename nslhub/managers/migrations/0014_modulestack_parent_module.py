# Generated by Django 3.1.2 on 2020-10-30 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0013_remove_modulestack_parent_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulestack',
            name='parent_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ModuleStack-Module+', to='managers.modulestack'),
        ),
    ]