from rest_framework import serializers
from .models import Sensor, Data


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'unit']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'