from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse
from .models import StakeHolder,SkillData,Skills

# Create your views here.

# class Manager(APIView):

#     def get(self,request):
#         datalist = {}
#         datalist = request.data
#         employee_id= datalist['employee_id']
#         name = StakeHolder.objects.filter(employee_id=employee_id).values()
#         print('---------------------------------',name)
#         # linked_content = []
#         # namee =[]
#         # for content in name: 
#         #     namee.append(content)
#         #     linked_content.append(content)
#         #     print('-----------------------------',linked_content)
#         res  = {}
#         for line in name:
            
#             res.update(line)
#             res['id']
#         name_id = res['id']
#         leaderUnderManager = StakeHolder.objects.filter(manager = name_id)
#         print('------------------res-------------',res)
#         print('-------------------name--------------',name)
#         # -------------------------------------------------------------------
#         post1=[]
#         for i in leaderUnderManager:
#             i ={'Emp Id':i.employee_id}
#             post1.append(i)
#         return JsonResponse(post1 , safe=False)

#         # return JsonResponse({'dev':'ok'})

#         # courses =  StakeHolder.objects.filter(employee_id='FE02').values()
#         # linked_content = []
#         # for content in courses:
#         #     linked_content.append(content)
#         #     # return linked_content
#         # print('------------------------',linked_content)


#         # leaderUnderManager = StakeHolder.objects.filter(StakeHo)
#         # print('-------------------------------------',leaderUnderManager)
#         # all_entries = StakeHolder.objects.all()
#         # manager_nhmind =StakeHolder.objects.filter(pk__in =[5])
#         # leaderUnderManager = StakeHolder.objects.filter(manager = 5)
#         # head_manager_nhmind = StakeHolder.objects.filter(pk__in =[8])
#         # leaderUnderHeadManager = StakeHolder.objects.filter(manager = 10)

#         # linked_content = []
#         # name =[]
#         # linked_contentt = []
#         # namee =[]
#         # linked_contents = []
#         # names =[]

#         # for content in leaderUnderManager: 
#         #     name.append(content.id)
#         #     linked_content.append(content)
#         # print('--Leader under nh mind-',linked_content)

#         # for content in manager_nhmind: 
#         #     namee.append(content.id)
#         #     linked_contentt.append(content)
#         # print('--manager_nhmind--',linked_contentt)

#         # for content in head_manager_nhmind: 
#         #     names.append(content.id)
#         #     linked_contents.append(content)
#         # print('--Head manager_nhmind--',linked_contents)
#         # return JsonResponse({'dev':'ok'})

class LeaderUndersManager(APIView):

    def get(self,request):
        datalist = {}
        datalist = request.data
        employee_id= datalist['employee_id']
        primary_id_empl= StakeHolder.objects.get(employee_id=employee_id).id
        print('-----------------------------------------------',primary_id_empl)
        leaderUnderManager = StakeHolder.objects.filter(manager = primary_id_empl)
        print('-------------vvvvv--------------------------',leaderUnderManager)
        first_name = StakeHolder.objects.filter(user_id=6)
        print('============================================',first_name)
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

     

