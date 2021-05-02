from django.urls import path,include
from . import views
from .views import Patient_list

urlpatterns = [

    path('', views.patient_form,name='patient_insert'), # get and post req. for insert operation
    path('patient/list/', Patient_list.as_view(),name='patient_list'),
    path('<int:id>/', views.patient_form,name='patient_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.patient_delete,name='patient_delete'),
    #path('patient/list/',views.patient_list,name='patient_list') # get req. to retrieve and display all records
]