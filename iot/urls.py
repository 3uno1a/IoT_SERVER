from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = 'iot'

urlpatterns = [
    path('mqtt/', TemplateView.as_view(template_name = 'iot/mqtt.html'), name = 'mqtt'),
    path('intrusion/', detect_intrusion),       # 카톡으로 메세지 보내기

    path('sec_upload/', sec_upload, name = 'sec_upload'),   # secfile 업로드
    path('sec_file/', SecFileListView.as_view(), name='list'),
    path('sec_file/<int:pk>', SecFileDetailView.as_view(), name = 'detail'),

    path('img_upload/', img_upload, name = 'img_upload'),   # imgfile 업로드

]