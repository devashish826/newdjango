# Generated by Django 3.1.2 on 2020-10-28 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managers', '0003_roles_roletypes_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.IntegerField(default=1)),
                ('skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SkillData-Skills+', to='managers.skills')),
            ],
        ),
        migrations.CreateModel(
            name='StakeHolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.CharField(max_length=300, null=True)),
                ('employee_id', models.CharField(max_length=300, null=True)),
                ('profile_img', models.CharField(max_length=300, null=True)),
                ('date_of_joining', models.DateField(null=True)),
                ('leave_balance', models.IntegerField(default=0)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StakeHolder-Entity+', to='managers.entity')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StakeHolder-manager-StakeHolder+', to='managers.stakeholder')),
                ('permission_grp', models.ManyToManyField(related_name='_stakeholder_permission_grp_+', to='managers.PermissionGroups')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StakeHolder-Roles+', to='managers.roles')),
                ('role_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StakeHolder-RoleTypes+', to='managers.roletypes')),
                ('skills', models.ManyToManyField(related_name='_stakeholder_skills_+', through='managers.SkillData', to='managers.Skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='skilldata',
            name='stakeholder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SkillData-StakeHolder+', to='managers.stakeholder'),
        ),
    ]
