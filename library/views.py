from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from library.models import Library
from library.serializers import LibrarySerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def library_timings(request):
    if request.method == 'GET':
        library = Library.objects.all()
         
        library_serializer = LibrarySerializer(library, many=True)
        return JsonResponse(library_serializer.data, safe=False)
    elif request.method == 'POST':
        library_data = JSONParser().parse(request)
        library_serializer = LibrarySerializer(data=library_data)
        if library_serializer.is_valid():
            library_serializer.save()
            return JsonResponse(library_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(library_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 


    