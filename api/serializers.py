# 일반 어플리케이션의 form 클래스 역할과 유사
# html 응답 X , json 응답 O
# 모델을 json 문자열로 변환하는 것을 직렬화(serialize)

from rest_framework import serializers
from iot.models import *

class SensorSerializer(serializers.ModelSerializer):   # ModelSerializer는 부모 클래스
    class Meta:
        model = Sensor
        fields = ('id', 'place', 'category', 'value', 'created_at')   # 필드 설정
        # fields: 직렬화에 포함시킬 필드명 - iot/models의 Sensor 클래스에 정의한 필드들


class CDSSerializer(serializers.ModelSerializer):  
    class Meta:
        model = CDS
        fields = ('id', 'place', 'value', 'created_at')

    def get_created_at(self, obj):
        return obj.created_at.strftime('%y_%m_%d_%H_%M') # 날짜를 년월일시분 까지표시, String형태


class CurtainSerializer(serializers.ModelSerializer):      # 커튼 제어 시리얼라이저

    class Meta:
        model = ControlCurtain
        fields = ['curtaincontrol']


class CurtainTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurtainTime
        fields = ['time_day', 'time_night']


class DoorlockSerializer(serializers.ModelSerializer):      # 도어락 제어 시리얼라이저

    class Meta:
        model = ControlDoorlock
        fields = ['doorlockcontrol']


class TempSerializer(serializers.ModelSerializer):  
    class Meta:
        model = DHT_temp
        fields = ('id', 'place', 'value','created_at')

        def get_created_at(self, obj):
            return obj.created_at.strftime('%y_%m_%d_%H_%M')   # 연월일시분


class HumiSerializer(serializers.ModelSerializer):  
    class Meta:
        model = DHT_humi
        fields = ('id', 'place', 'value',  'created_at')

    def get_created_at(self, obj):
        return obj.created_at.strftime('%y_%m_%d_%H_%M') # 날짜를 년월일시분 까지표시, String형태


class AirconSerializer(serializers.ModelSerializer):     

    class Meta:
        model = ControlAircon
        fields = ['airconcontrol']


class HeaterSerializer(serializers.ModelSerializer):     

    class Meta:
        model = ControlHeater
        fields = ['heatercontrol']


class HumidifierSerializer(serializers.ModelSerializer):     

    class Meta:
        model = ControlHumidifier
        fields = ['humidifiercontrol']


class DehumidifierSerializer(serializers.ModelSerializer):     

    class Meta:
        model = ControlDehumidifier
        fields = ['dehumidifiercontrol']


class StandardTemperatureSerializer(serializers.ModelSerializer):      # 가습기 제어 시리얼라이저

    class Meta:
        model = StandardTemperature
        fields = ['standard_temp']


class StandardHumiditySerializer(serializers.ModelSerializer):      # 가습기 제어 시리얼라이저

    class Meta:
        model = StandardHumidity
        fields = ['standard_humi']
    

class SecFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecFile
        fields = ('id', 'file_name', 'sec_file')

        # fields: iot/models의 SecFile 클래스에 정의한 필드들 - rest api에 data 하나당 field가 나와
        '''
        {
            "id": 33,
            "file_name": "img6.jpg",
            "sec_file": "....//.......8000/media/sec_file/2023/05/04/img6.jpg"
        },
        '''

class ImgFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ('id', 'file_name', 'img_file')


class TotalSmartControlSerializer(serializers.ModelSerializer):

    class Meta:
        model = TotalSmartControl
        fields = ['total_control']