from django.urls import path, include
from . import views
from .import api 

app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name = 'add_job'),
    path('<str:slug>', views.job_detail, name = 'job_detail'),
    
    # api
    path('api/jobs', api.job_list_api, name = 'job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name = 'job_detail_api'),
    
    #class Based view
    path('api/v2/jobs', api.JobListApi.as_view(), name = 'JobListApi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name = 'JobDetail'),
    
]
