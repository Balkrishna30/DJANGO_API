from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
'''class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/companyid/employees
    @action(detail = True,methods =['get'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
            
            response_data = {
                'company_name': company.name,  # Include the company name in the response
                'employees': emps_serializer.data,
            }
            
            return Response(response_data)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Company might not exist !! Error'
            })

        pass'''

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def employees(self, request, company_id=None):
        if company_id is not None:
            try:
                company = Company.objects.get(pk=company_id)
                emps = Employee.objects.filter(company=company)
                emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})

                response_data = {
                    'company_name': company.name,
                    'employees': emps_serializer.data,
                }

                return Response(response_data)
            except Company.DoesNotExist:
                return Response({
                    'message': 'Company does not exist.'
                })

        #return Response({'message': 'Company ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

