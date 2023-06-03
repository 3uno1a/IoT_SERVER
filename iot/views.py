from django.shortcuts import render
from . import sub
from django.views.generic import TemplateView
from django.http import JsonResponse   # Json으로 응답
from django.views.decorators.csrf import csrf_exempt
from .models import SecFile, ImageFile
from django.views import generic

@csrf_exempt   # csrf token 없이
def sec_upload(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        sec_file = request.FILES['sec_file']
        model = SecFile(file_name = file_name, sec_file = sec_file)
        model.save()
        print('upload file', file_name, sec_file)
        msg = {'result' : 'success'}

    else:                                # GET 요청
        msg = {'result' : 'fail'}
    return JsonResponse(msg)


@csrf_exempt   # smartCam - 20cm이내로 오면 2초동안 사진 5번 촬영하는 기능용
def img_upload(request):
    if request.method == 'POST':
        file_name = request.POST['file_name']
        img_file = request.FILES['img_file']
        model = ImageFile(file_name = file_name, img_file = img_file)
        model.save()
        print('upload file', file_name, img_file)
        msg = {'result' : 'success'}

    else:                                # GET 요청
        msg = {'result' : 'fail'}
    return JsonResponse(msg)


def send_talk(text, url):
    talk_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    with open("access_token.txt", "r") as f:
        token = f.read()
    header = {"Authorization": f"Bearer {token}"}

    # 문자열 하나, 링크 하나로 구성되는 카톡 메시지 구성
    text_template = {
        'object_type': 'text',
        'text': text,
        'link': {
                'web_url': url,
                'mobile_web_url' : url
        }
    }

def detect_intrusion(request):
    # 카톡으로 메세지 보내기
    text = request.GET.get('text')
    url = request.GET.get('url')

    res = send_talk(text, url)
    if res.get('result_code') == 0:
        msg = {'result' : 'success'}
    else:
        msg = {
            'result' : 'fail',
            'reason' : str(res),
        }
    return JsonResponse(msg)


# 녹화 파일 목록 보기
class SecFileListView(generic.ListView):
    model = SecFile
    template_name = 'iot/sec_file_list.html'
    context_object_name = 'sec_files'


# 녹화 파일 상세 보기
class SecFileDetailView(generic.DetailView):
    model = SecFile
    template_name = 'iot/sec_file_detail.html'
    context_object_name = 'vfile'

