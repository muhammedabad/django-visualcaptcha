from django.http import HttpResponse, Http404
from django.conf import settings

from visualcaptcha import Captcha, Session

import json


def visualcaptcha_start(request, number_of_images):
    assetsPath = "%s/img/visualcaptcha/captcha/" % settings.MEDIA_ROOT
    visualCaptcha = Captcha(Session(request.session), assetsPath=assetsPath)

    visualCaptcha.generate()

    data = visualCaptcha.getFrontendData()

    response = HttpResponse()
    response['Content-type'] = "application/json"
    response.write(json.dumps(data))
    return response


def visualcaptcha_get_image(request, index):
    try:
        index = int(index)
    except TypeError:
        raise Http404

    visualCaptcha = Captcha(Session(request.session))

    headers = {}
    data = visualCaptcha.streamImage(headers=headers, index=index)

    response = HttpResponse(data, content_type=headers['Content-Type'])
    return response


def visualcaptcha_get_audio(request):
    visualCaptcha = Captcha(Session(request.session))

    headers = {}
    data = visualCaptcha.streamAudio(headers=headers)

    response = HttpResponse(data, content_type=headers['Content-Type'])
    return response
