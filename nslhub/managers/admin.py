from django.contrib import admin
from . models import Entity,PermissionGroups,Skills,Roles,RoleTypes,StakeHolder,SkillData,ModuleType
from .models import ModuleStack,ModuleLeaders,LeaderModuleChangeHistory,LeaderManagerChangeHistory
# Register your models here.
admin.site.register(Entity)
admin.site.register(PermissionGroups)
admin.site.register(Skills)
admin.site.register(Roles)
admin.site.register(RoleTypes)
admin.site.register(StakeHolder)
admin.site.register(SkillData)
admin.site.register(ModuleType)
admin.site.register(ModuleStack)
admin.site.register(ModuleLeaders)
admin.site.register(LeaderModuleChangeHistory)
admin.site.register(LeaderManagerChangeHistory)