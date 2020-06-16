from rest_framework import serializers 
from clubs.models import Clubs
 
 
class ClubSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Clubs
        fields = ('id',
                  'title',
                  'description',
                  'secretary')