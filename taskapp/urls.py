from django.urls import path
from taskapp import views

urlpatterns=[
    path('',views.index),
    path('completed/<task_id>',views.complete_task,name="completed"),
    path('pending/<task_id>',views.pending_task,name="pending"),
    path('indexemp', views.indexemp),
    path('create',views.create),
    path('delete/<emp_id>',views.delete,name="delete"), #ไว้ลบข้อมูล
    path('edit/<emp_id>',views.edit,name="edit"), #ไว้แก้ไขข้อมูล
    path('indexmoney',views.indexmoney), #ไว้ระบุพาทหน้าแรกให้เรียกใช้ views index
    path('account',views.account) #ไว้ระบุพาทหน้าแรกให้เรียกใช้ views account
]
