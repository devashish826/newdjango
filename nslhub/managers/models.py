from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from enum import IntEnum


class Entity(models.Model):
    """Permission Groups"""
    name = models.CharField(max_length=240, unique=True)
    # enum = models.IntegerField(choices=[(item.value, item.name) for item in EntityEnum], default=EntityEnum.BEPL)
    def __str__(self):
        return self.name

class PermissionGroups(models.Model):
    """Permission Groups"""
    name = models.CharField(max_length=240, unique=True)
    description = models.TextField(null=True)
    # permissions = JSONField()
    entity = models.ForeignKey(Entity,  on_delete=models.SET_NULL, related_name="PermissionGroups-Entity+", null=True)
    # parent = models.ForeignKey('self',  on_delete=models.SET_NULL, related_name="PermissionGroups-manager-PermissionGroups+", null=True)

    def __str__(self):
        return self.name

class Skills(models.Model):
    """Skills model."""
    name = models.CharField(max_length=240, unique=True)
    def __str__(self):
        return self.name



class Roles(models.Model):
    """Role model."""
    name = models.CharField(max_length=240, unique=True)
    def __str__(self):
        return self.name
    


class RoleTypes(models.Model):
    """Role Type model."""
    name = models.CharField(max_length=240, unique=True)
    def __str__(self):
        return self.name


class StakeHolder(models.Model):
    """StakeHolder model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission_grp = models.ManyToManyField(PermissionGroups, related_name="Stack-Leaders+")
    cv = models.CharField(max_length=300, null=True)
    employee_id = models.CharField(max_length=300, null=True)
    # designation = models.IntegerField(choices=[(desg.value, desg.name) for desg in Designations], default=Designations.Associate_Solution_Leader)
    manager = models.ForeignKey("self",  on_delete=models.SET_NULL, related_name="StakeHolder-manager-StakeHolder+", null=True)
    # extra_data = JSONField(default=dict)
    skills = models.ManyToManyField(Skills, through='SkillData', related_name="StakeHolder-SkillData+")
    leave_balance = models.DecimalField(max_digits=10, decimal_places=5, default=0.0, null=False)
    profile_img = models.CharField(max_length=300, null=True)
    role = models.ForeignKey(Roles,  on_delete=models.SET_NULL, related_name="StakeHolder-Roles+", null=True)
    role_type = models.ForeignKey(RoleTypes,  on_delete=models.SET_NULL, related_name="StakeHolder-RoleTypes+", null=True)
    entity = models.ForeignKey(Entity,  on_delete=models.SET_NULL, related_name="StakeHolder-Entity+", null=True)
    # user_type = models.IntegerField(choices=[(item.value, item.name) for item in UserTypeEnum], default=UserTypeEnum.SEMANTIC)
    date_of_joining = models.DateField(null=True)
    leave_balance = models.IntegerField(default=0, null=False)
    @property
    def full_name(self):
        middle_name = "" if self.extra_data.get("middle_name", None) is None else self.extra_data["middle_name"]
        return self.user.first_name + " " + middle_name + " " +self.user.last_name
    
    @property
    def email(self):
        return self.user.email

    def __str__(self):
        return self.user.username

class SkillData(models.Model):
    """Skill Stakeholder Relationship table."""
    skill = models.ForeignKey(Skills,  on_delete=models.CASCADE, related_name="SkillData-Skills+", null=True)
    stakeholder = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="SkillData-StakeHolder+", null=True)
    proficiency = models.IntegerField(default=1, null=False)
    # skill_preference = models.IntegerField(choices=[(val.value, val.name) for val in SkillPreference], null=True)
    # extra_data = JSONField(default=dict)
  
    


class ModuleType(models.Model):
    name = models.CharField(max_length=300, null=True)
    # enum = models.IntegerField(choices=[(val.value, val.name) for val in ModuleTypeEnum], null=True)
    def __str__(self):
        return self.name

class ModuleStack(models.Model):
    name = models.CharField(max_length=300, null=True)
    module_type = models.ForeignKey(ModuleType,  on_delete=models.CASCADE, related_name="ModuleStack-ModuleType+", null=True)
    parent_module = models.ForeignKey('self',  on_delete=models.CASCADE, related_name="ModuleStack-Module+", null=True)
    leaders = models.ManyToManyField(StakeHolder, through='ModuleLeaders', related_name="Module-Leaders+")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class ModuleLeaders(models.Model):
    module = models.ForeignKey(ModuleStack,  on_delete=models.CASCADE, related_name="Leaders-Module+", null=True)
    stakeholder = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="Leader-StakeHolder+", null=True)
    spoc = models.BooleanField(default=False)
    leader = models.BooleanField(default=False)


class LeaderModuleChangeHistory(models.Model):
    old_module = models.ForeignKey(ModuleStack,  on_delete=models.CASCADE, related_name="LeaderModuleChangeHistory-Module-old_module+", null=True)
    new_module = models.ForeignKey(ModuleStack,  on_delete=models.CASCADE, related_name="LeaderModuleChangeHistory-Module-new_module+", null=True)
    stakeholder = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="LeaderModuleChangeHistory-StakeHolder+", null=True)
    created_on = models.DateTimeField(auto_now_add=True)


class LeaderManagerChangeHistory(models.Model):
    old_manager = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="LeaderManagerChangeHistory-StakeHolder-old_manger+", null=True)
    new_manager = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="LeaderManagerChangeHistory-StakeHolder-new_manager+", null=True)
    stakeholder = models.ForeignKey(StakeHolder,  on_delete=models.CASCADE, related_name="LeaderManagerChangeHistory-StakeHolder-stakeholder+", null=True)
    created_on = models.DateTimeField(auto_now_add=True)
