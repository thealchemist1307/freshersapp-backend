from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from clubs.models import Clubs
from clubs.serializers import ClubSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def club_list(request):
    if request.method == 'GET':
        clubs = Clubs.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            clubs = clubs.filter(title__icontains=title)
        
        clubs_serializer = ClubSerializer(clubs, many=True)
        return JsonResponse(clubs_serializer.data, safe=False)
    elif request.method == 'POST':
        club_data = JSONParser().parse(request)
        club_serializer = ClubSerializer(data=club_data)
        if club_serializer.is_valid():
            club_serializer.save()
            return JsonResponse(club_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(club_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Clubs.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def club_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        clubs = Clubs.objects.get(pk=pk) 
    except Clubs.DoesNotExist: 
        return JsonResponse({'message': 'The Clubs does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        club_serializer = ClubSerializer(clubs) 
        return JsonResponse(club_serializer.data) 
    elif request.method == 'PUT': 
        club_data = JSONParser().parse(request) 
        club_serializer = ClubSerializer(clubs, data=club_data) 
        if club_serializer.is_valid(): 
            club_serializer.save() 
            return JsonResponse(club_serializer.data) 
        return JsonResponse(club_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        clubs.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    # GET / PUT / DELETE tutorial

    