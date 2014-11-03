from django.shortcuts import render_to_response
from django.template import RequestContext

from visualcaptcha_demo.lib.forms import DemoForm
from visualcaptcha_demo.lib.captcha import validate_captcha


def home(request):
    form = DemoForm()
    template_vars = {}
    captcha_check = None

    if request.POST:
        form = DemoForm(request.POST)
        captcha_check = validate_captcha(request)

        if captcha_check['is_valid']:
            # Captcha has passed validation, let's validate the rest of the form
            if form.is_valid():
                # Continue with normal form processing logic
                pass

                # Reset form
                form = DemoForm()

    template_vars['captcha_check'] = captcha_check
    template_vars['form'] = form

    return render_to_response(
        'index.html', template_vars,
        context_instance=RequestContext(request)
    )
