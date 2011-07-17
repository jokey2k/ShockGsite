from django.db import transaction
from django.shortcuts import redirect, render

from trackmaniawars.forms import FightUsForm

@transaction.commit_on_success
def fightusform(request):
    if request.method == 'POST':
        form = FightUsForm(request.POST)

        if form.is_valid():
            entry = form.save()
            return render(request, 'trackmaniawars/fightus_success.html')
    else:
        form = FightUsForm()
                        
    return render(request, 'trackmaniawars/fightus_form.html',
                           {'form':form})

