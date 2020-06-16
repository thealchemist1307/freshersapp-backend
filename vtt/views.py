from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

@api_view(['POST'])
def vtt_response(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
            
        return JsonResponse(data, status=status.HTTP_201_CREATED) 
        
   