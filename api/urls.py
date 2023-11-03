from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter() 
router.register(r'companies',CompanyViewSet)
router.register(r'employees',EmployeeViewSet)

#we cant get post through companies
urlpatterns = [
    path('',include(router.urls)),
    path('companies/employees/<int:company_id>/', CompanyViewSet.as_view({'get': 'employees'})),

    
]
#companies/companyid/employees 
