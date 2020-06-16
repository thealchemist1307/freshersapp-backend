from rest_framework import serializers 
from library.models import Library
 
 
class LibrarySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Library
        fields = ('id',
                  'day',
                  'timings')