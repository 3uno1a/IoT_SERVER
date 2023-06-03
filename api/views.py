from django.shortcuts import render

from rest_framework import viewsets
from iot.models import *
from .serializers import *


class SensorViewSet(viewsets.ModelViewSet):     # ModelViewSet이 GET, POST, PUT, DELETE 모두 처리
    queryset = Sensor.objects.all().order_by('-id')      # 최신 id순으로 정렬
    # queryset 정의 / 페이지네이션은 config/settings REST_FRAMEWORK에 
    serializer_class = SensorSerializer         # 클래스 배정


class CDSViewSet(viewsets.ModelViewSet):   
    queryset = CDS.objects.all().order_by('-id')     
    serializer_class = CDSSerializer    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = CDS.objects.all().order_by('id')

        if queryset.count() > 20:                      
            queryset.first().delete()                   
        return response
    

class TempViewSet(viewsets.ModelViewSet):   
    queryset = DHT_temp.objects.all().order_by('-id')     
    serializer_class = TempSerializer    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = DHT_temp.objects.all().order_by('id')
        if queryset.count() >= 20:                         # 데이터 생성시, 20개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response


class HumiViewSet(viewsets.ModelViewSet):   
    queryset = DHT_humi.objects.all().order_by('-id')     
    serializer_class = HumiSerializer    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = DHT_humi.objects.all().order_by('id')
        if queryset.count() >= 20:                         # 데이터 생성시, 20개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response


class CurtainViewSet(viewsets.ModelViewSet):
    queryset = ControlCurtain.objects.all()
    serializer_class = CurtainSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlCurtain.objects.all()
        if queryset.count() >= 2:                         # 데이터 생성시, 2개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response


class CurtainTimeViewSet(viewsets.ModelViewSet):
    queryset = CurtainTime.objects.all()
    serializer_class = CurtainTimeSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = CurtainTime.objects.all()

        if queryset.count() >= 2:                      
            queryset.first().delete()                   
        return response



class DoorlockViewSet(viewsets.ModelViewSet):
    queryset = ControlDoorlock.objects.all()
    serializer_class = DoorlockSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlDoorlock.objects.all()

        if queryset.count() >= 2:                        
            queryset.first().delete()                   
        return response
    

class AirconViewSet(viewsets.ModelViewSet):
    queryset = ControlAircon.objects.all()
    serializer_class = AirconSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlAircon.objects.all()

        if queryset.count() >= 2:                        
            queryset.first().delete()                   
        return response
    

class HeaterViewSet(viewsets.ModelViewSet):
    queryset = ControlHeater.objects.all()
    serializer_class = HeaterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlHeater.objects.all()

        if queryset.count() >= 2:                        
            queryset.first().delete()                   
        return response
    

class HumidifierViewSet(viewsets.ModelViewSet):
    queryset = ControlHumidifier.objects.all()
    serializer_class = HumidifierSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlHumidifier.objects.all()

        if queryset.count() >= 2:                        
            queryset.first().delete()                   
        return response
    

class DehumidifierViewSet(viewsets.ModelViewSet):
    queryset = ControlDehumidifier.objects.all()
    serializer_class = DehumidifierSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ControlDehumidifier.objects.all()

        if queryset.count() >= 2:                        
            queryset.first().delete()                   
        return response
    


class StandardTemperatureViewSet(viewsets.ModelViewSet):           # 기준온도
    queryset = StandardTemperature.objects.all().order_by('-id')
    serializer_class = StandardTemperatureSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = StandardTemperature.objects.all()
        if queryset.count() >= 2:                         # 데이터 생성시, 2개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response
    

class StandardHumidityViewSet(viewsets.ModelViewSet):        # 기준습도
    queryset = StandardHumidity.objects.all().order_by('-id')
    serializer_class = StandardHumiditySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = StandardHumidity.objects.all()
        if queryset.count() >= 2:                         # 데이터 생성시, 2개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response


class SecFileViewSet(viewsets.ModelViewSet):
    queryset = SecFile.objects.all().order_by('-id')
    serializer_class = SecFileSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = SecFile.objects.all().order_by('id')

        if queryset.count() > 20:                      
            queryset.first().delete()                   
        return response


class ImgFileViewSet(viewsets.ModelViewSet):
    queryset = ImageFile.objects.all().order_by('-id')
    serializer_class = ImgFileSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = ImageFile.objects.all().order_by('id')

        if queryset.count() > 20:                         # 이미지 데이터 생성시, 20개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response
    

class TotalSmartControlViewSet(viewsets.ModelViewSet):        # 온습도 스마트컨트롤 통합제어
    queryset = TotalSmartControl.objects.all().order_by('-id')
    serializer_class = TotalSmartControlSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        queryset = TotalSmartControl.objects.all()
        if queryset.count() >= 2:                         # 데이터 생성시, 2개 이상이 되면 
            queryset.first().delete()                     # 가장 먼저 만들어진 데이터부터 삭제
        return response