from django.db import models
from django.utils import timezone

# 지금은 편의를 위해 사용자 계정 연동 항목을 뺌 - 프로젝트할때는 넣으면 좋음
class Sensor(models.Model):
    place = models.CharField(max_length = 50)   # 설치 장소
    category = models.CharField(max_length = 50)  # 센서 종류
    value = models.FloatField()                  # 센서 값
    created_at = models.DateTimeField()          # 측정 날짜-시간


class DHT_temp(models.Model):
    place = models.CharField(max_length = 50)   
    value = models.FloatField()        
    created_at = models.DateTimeField()       

class DHT_humi(models.Model):
    place = models.CharField(max_length = 50)   
    value = models.FloatField()                  
    created_at = models.DateTimeField()   


class CDS(models.Model):
    place = models.CharField(max_length = 50)   
    value = models.FloatField()                  
    created_at = models.DateTimeField()    


class SecFile(models.Model):
    file_name = models.CharField(max_length = 100)
    sec_file = models.FileField(upload_to = "sec_file/%Y_%m_%d/")
    # 라즈베리파이에서 upload하면 django 서버에서
    # media/sec_file/에 월별 일별로 파일이 만들어져서 upload돼


class ImageFile(models.Model):
    file_name = models.CharField(max_length = 100)
    img_file = models.FileField(upload_to = "img_file/%Y_%m_%d/")


# 커튼제어 모델
class ControlCurtain(models.Model):
    curtaincontrol = models.BooleanField(default=False)  


class CurtainTime(models.Model):
    time_day = models.DateTimeField()
    time_night = models.DateTimeField()
    

# 도어락제어 모델
class ControlDoorlock(models.Model):
    doorlockcontrol = models.BooleanField(default=False)  



# 에어컨 제어 모델
class ControlAircon(models.Model):
    airconcontrol = models.BooleanField(default=False)  


# 히터 제어 모델
class ControlHeater(models.Model):
    heatercontrol = models.BooleanField(default=False)   


# 가습기 제어 모델
class ControlHumidifier(models.Model):
    humidifiercontrol = models.BooleanField(default=False)   


# 제습기 제어 모델
class ControlDehumidifier(models.Model):
    dehumidifiercontrol = models.BooleanField(default=False)   


# 기준온도 모델     
class StandardTemperature(models.Model): 
    standard_temp = models.FloatField()         


# 기준습도 모델     
class StandardHumidity(models.Model): 
    standard_humi = models.FloatField() 


class TotalSmartControl(models.Model) : 
    total_control = models.BooleanField(default=False)