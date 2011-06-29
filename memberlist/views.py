# Create your views here.
from django.contrib.auth.models import User, Group
from gamesquad.models import Squadmember
from djangobb_forum.util import render_to

@render_to('memberlist.html')
def memberlist(request):
    """show all clanmembers"""

    groups = {}
    for group in Group.objects.order_by('name').all():
        groups[group.name.replace(" ", "_")] = User.objects.filter(groups__in=[group]).filter(is_active=True).all()

    return groups