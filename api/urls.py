from rest_framework import routers
from api.views import *

from django.urls import path, include

router = routers.DefaultRouter()   # 인스턴스 생성

# SensorViewSet이 ./api/sensor/와 ./api/sensor/<int:id>/ 2개를 등록해 (id 있는거 없는거)
router.register('sensor', SensorViewSet, basename='sensor')    # sensor를 기본 url로 등록 / View 클래스 등록
router.register('cds', CDSViewSet, basename = 'cds')
router.register('temp', TempViewSet, basename = 'temp')
router.register('humid', HumiViewSet, basename = 'humid')

router.register('curtain', CurtainViewSet)
router.register('curtain_time', CurtainTimeViewSet)
router.register('doorlock', DoorlockViewSet)

router.register('aircon', AirconViewSet)
router.register('heater', HeaterViewSet)
router.register('humidifier', HumidifierViewSet)
router.register('dehumidifier', DehumidifierViewSet)

router.register('standard_temp', StandardTemperatureViewSet) #
router.register('standard_humi', StandardHumidityViewSet) 
router.register('total_control', TotalSmartControlViewSet) 

router.register('secfile', SecFileViewSet, basename='secfile')
router.register('imgfile', ImgFileViewSet, basename = 'imgfile')


urlpatterns = [
    path('', include(router.urls)),
]
