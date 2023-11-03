from django.http import HttpResponse
import os
def home_page(request):
    with open('hello.txt', 'r') as file:
        content = file.read()
    return HttpResponse(content)