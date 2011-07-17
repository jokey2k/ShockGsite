from django.forms import ModelForm

from trackmaniawars.models import FightUs

class FightUsForm(ModelForm):
    class Meta:
        model=FightUs