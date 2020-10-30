from django.conf.urls import url 
from managers import views 

urlpatterns = [ 
      url('api/Manager',views.LeaderUndersManager.as_view()),
      url('api/LeaderSkillData',views.LeaderSkillData.as_view()),
      url('api/Leader',views.LeaderUndersManagerFistnameLastname.as_view()),
    
 ]

