import re
from django import forms
from registration.forms import RegistrationFormUniqueEmail
import recaptcha

class RegistrationFormUtfUsername(RegistrationFormUniqueEmail):
    '''
    Allowed UTF8 logins with space
    '''
    recaptcha = recaptcha.ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super(RegistrationFormUtfUsername, self).__init__(*args, **kwargs)
        self.fields['username'].regex = re.compile(r"^[\w\s-]+$", re.UNICODE)

