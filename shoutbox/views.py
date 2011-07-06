from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from django.shortcuts import redirect, render
from django.db import transaction

from djangobb_forum.util import render_to

from shoutbox.models import ShoutboxEntry
from shoutbox.forms import ShoutboxPostForm

def recent_entries(request, entrycount=5):
    """Render a set of recent entries"""
    entries = ShoutboxEntry.objects.order_by('-created')[:entrycount]
    return render(request, 'shoutbox/recents.html', {'entries':entries})

@transaction.commit_on_success
def postform(request):
    if request.method == 'POST':
        form = ShoutboxPostForm(request.POST)

        if request.user.is_authenticated():
            del form.fields['hint']

        if form.is_valid():
            entry = ShoutboxEntry()
            entry.text = form.cleaned_data['message']
            entry.ip = request.META['REMOTE_ADDR']
            if request.user.is_authenticated():
                entry.author = request.user
                entry.author_name = request.user.username
            else:
                entry.author = None
                entry.author_name = form.cleaned_data['nickname']
            entry.save()
            if request.is_ajax():
                # For ajax store, send a blank, new form afterwards
                form = ShoutboxPostForm()
                if request.user.is_authenticated():
                    del form.fields['hint']
            else:
                next = request.POST['next'] or request.META['HTTP_REFERER']
                if next and next == "/shoutbox/post":
                    next = "/"
                import pdb;pdb.set_trace()
                return redirect(next if next else '/')
    else:
        form = ShoutboxPostForm()
        form.fields['next'].initial=request.get_full_path()
        if request.user.is_authenticated():
            form.fields['nickname'].initial = request.user.username
            del form.fields['hint']
                        
    return render(request, 'shoutbox/postform.html',
                           {'form':form})
