from django.http import JsonResponse
from .models import Sensor, Data
from .serializers import SensorSerializer, DataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET','POST'])
def sensor_list(request):
    #Get request 
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response({'sensors':serializer.data})

    #Post request
    if request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)        

@api_view(['GET','PUT','DELETE'])
def sensor_detail(request,id):
    #Catch error for invalid sensor id
    try:
        sensor = Sensor.objects.get(pk=id)
    except Sensor.DoesNotExist:
        return Response(status=status.HTTP_404_NOTFound)

    #Condition for different HTTP methods
    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 

class DataListView(generics.ListCreateAPIView):
    serializer_class = DataSerializer
    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['date','sensor']

    def get_queryset(self):
        return Data.objects.filter()

    def perform_create(self,serializer):
        return serializer.save()




