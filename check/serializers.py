# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import BlahModel, TapModel
 
# Create a model serializer
class BlahSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = BlahModel
        fields = ('title', 'description')

class TapSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = TapModel
        fields = ('title', 'description')