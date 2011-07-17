from django.contrib.auth.forms import AuthenticationForm

def frontpage_loginform(context):
    form = AuthenticationForm()
    return {'frontpage_loginform': form}
