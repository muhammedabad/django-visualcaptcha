from django.conf.urls import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings


def direct_to_template(request, template, args={}):
    return render_to_response(template, args, context_instance=RequestContext(request))


urlpatterns = patterns('',
    (r'^$', 'visualcaptcha_demo.lib.views.home'),

    (r'^start/(?P<number_of_images>\d+)/$', 'visualcaptcha_demo.lib.ajax.visualcaptcha_start'),
    (r'^image/(?P<index>\d+)/$', 'visualcaptcha_demo.lib.ajax.visualcaptcha_get_image'),
    (r'^audio/$', 'visualcaptcha_demo.lib.ajax.visualcaptcha_get_audio'),

    # Static directories
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve',  {'document_root': settings.MEDIA_ROOT}),

)
