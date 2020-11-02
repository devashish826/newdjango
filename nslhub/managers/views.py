from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from .models import StakeHolder,SkillData,Skills,User,ModuleStack,ModuleLeaders,ModuleType

# Create your views here.

class LeaderUndersManager(APIView):

    def get(self,request):
        datalist = {}
        datalist = request.data
        employee_id= datalist['employee_id']
        primary_id_empl= StakeHolder.objects.get(employee_id=employee_id).id
        print('-----------------------------------------------',primary_id_empl)
        leaderUnderManager = StakeHolder.objects.filter(manager = primary_id_empl)
        print('-------------vvvvv--------------------------',leaderUnderManager)
        leaders=[]
        for leader in leaderUnderManager:
            leader ={'Emp Id':leader.employee_id}
            leaders.append(leader)
        return JsonResponse(leaders , safe=False)
        # return JsonResponse({'dev':'ok'})
        
class LeaderSkillData(APIView):
    def get(self,request):
        res = {}
        res = request.data 
        Skill=[]
        employee_id= res['employee_id']
        primary_id_empl= StakeHolder.objects.get(employee_id=employee_id).id
        QuerySetSkillData = SkillData.objects.filter(stakeholder_id=primary_id_empl)
        for  i in QuerySetSkillData:  
            a=i.skill_id
            b=Skills.objects.get(id=a)
            skill ={'Skill':b.name,'proficiency_level':i.proficiency}
            Skill.append(skill)
        return JsonResponse(Skill , safe=False)

class LeaderUndersManagerFistnameLastname(APIView):

    def get(self,request):
        datalist = {}
        datalist = request.data
        employee_id= datalist['employee_id']
        primary_id_empl= StakeHolder.objects.get(employee_id=employee_id).id
        leaderUnderManager = StakeHolder.objects.filter(manager = primary_id_empl)
        Skill=[]
        for i in leaderUnderManager:
            a=i.user_id
            b = User.objects.get(id = a)
            skill ={'Emp id':i.employee_id,'first name':b.first_name,'last name':b.last_name}
            Skill.append(skill)
        return JsonResponse(Skill , safe=False)
       
       
class ModuleStackk(APIView):

    def get(self,request):
        datalist = {}
        datalist = request.data
        employee_id= datalist['employee_id']
        primary_id_empl= StakeHolder.objects.get(employee_id=employee_id).id
        moduleleaders_object = ModuleLeaders.objects.filter(stakeholder_id = primary_id_empl)
        Skill=[]
        for  i in moduleleaders_object:  
            skill ={'name':i.module.name,'active':i.module.active,'module_type_id':i.module.module_type_id,"parent_module_id":i.module.parent_module_id}
            Skill.append(skill)
        return JsonResponse(Skill , safe=False)
            
class Stakeholderlist(APIView):
    def get(self,request):
        datalist = {}
        leader = []
        datalist = request.data
        name= datalist['name']
        # moduleStack
        modulestackObject = ModuleStack.objects.get(name = name)
        ModuleLeadersObject = ModuleLeaders.objects.filter(module_id = modulestackObject)
        # for i in ModuleLeadersObject:
        #     leader.append(i.stakeholder_id)
        # moduleleaders_object = ModuleLeaders.objects.filter(stakeholder_id__in = leader)
        # print('--------------------xxxx---------------------------',leader)
        leader = []

        Skill=[]
        for  i in ModuleLeadersObject: 
            leader.append(i.stakeholder_id)   
            print('--------------------------------------------------',leader)
            skill ={'Emp ID':i.stakeholder.employee_id,'Full Name ':i.stakeholder.user.first_name +' '+ i.stakeholder.user.last_name ,'first_name':i.stakeholder.user.first_name,'last name':i.stakeholder.user.last_name}
            Skill.append(skill)
        print('--------------------------------------------------',leader)
        return JsonResponse(Skill , safe=False)
       
       

        # return JsonResponse({'dev':'ok'})