
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import BlahSerializer, TapSerializer
from .models import BlahModel, TapModel
 
# create a viewset
class BlahViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = BlahModel.objects.all()
     
    # specify serializer to be used
    serializer_class = BlahSerializer

class TapViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = TapModel.objects.all()
     
    # specify serializer to be used
    serializer_class = TapSerializer