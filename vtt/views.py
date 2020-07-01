from django.shortcuts import render
import json
from collections import namedtuple
from json import JSONEncoder
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from rest_framework.parsers import FileUploadParser
import io
from vtt.serializers import ConfigSerializer , AudioSerializer
from vtt.models import config,audio
@api_view(['POST'])
def vtt_response(request):
    parser_classes = [FileUploadParser]
    print("This is the changed requets \n")
    if request.method == 'POST':  
        client = speech_v1.SpeechClient()
        response = client.recognize({
    "encoding":"FLAC",
    "language_code": "en-US"
}, {"content":request.FILES["audio"].read()})
        print(response.results[0].alternatives[0].transcript)
        return Response(response.results[0].alternatives[0].transcript)        

    return JsonResponse("Failed", status=status.HTTP_201_CREATED) 
        
   