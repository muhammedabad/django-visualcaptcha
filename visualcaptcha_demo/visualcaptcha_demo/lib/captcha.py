from visualcaptcha import Captcha, Session


def validate_captcha(request):
    visualCaptcha = Captcha(Session(request.session))
    frontendData = visualCaptcha.getFrontendData()

    # If an image field name was submitted, try to validate it
    if frontendData['imageFieldName'] in request.POST:
        if visualCaptcha.validateImage(request.POST[frontendData['imageFieldName']]):
            return {'is_valid': True, 'message': 'Image was valid !'}
        else:
            return {'is_valid': False, 'message': 'Image was not valid !'}

    if frontendData['audioFieldName'] in request.POST:
        # We set lowercase to allow case-insensitivity, but it's actually optional
        if visualCaptcha.validateAudio(request.POST[frontendData['audioFieldName']].lower()):
            return {'is_valid': True, 'message': 'Accessibility answer was valid !'}
        else:
            return {'is_valid': True, 'message': 'Accessibility answer was NOT valid !'}

    return {"is_valid": False, 'message': 'Captcha is required, please try again'}
