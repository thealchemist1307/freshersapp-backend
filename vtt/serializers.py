from rest_framework import serializers 
from vtt.models import config , audio 
 
 
class ConfigSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = config
        fields = ( "encoding"
      "sampleRateHertz"
      "languageCode"
      "enableWordTimeOffsets")
class AudioSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = audio
        fields = "__all__"