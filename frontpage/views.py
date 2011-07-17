from shoutbox.views import recent_entries as shoutbox_recent_entries, postform as shoutbox_postform
from news.views import recent_entries as news_recent_entries

from djangobb_forum.util import render_to
from django.utils.safestring import mark_safe

from djangobb_forum.models import Topic, PostTracking
from djangobb_forum.templatetags import forum_extras
from trackmaniawars.models import FightUs
@render_to("frontpage/frontpage.html")
def frontpage(request):
    """Render the front page"""

    news_top = mark_safe(news_recent_entries(request, 1, "news/recents_top.html").content)
    news_older = mark_safe(news_recent_entries(request, 3, "news/recents_older.html", 1).content)

    return locals()
@render_to("frontpage/statusbox.html")
def statusbox(request):
    """Render the current status box"""

    # fetch count of unread topics
    if request.user.is_authenticated():
        groups = request.user.groups.all() or []
        topics = Topic.objects.filter(
                   Q(forum__category__groups__in=groups) | \
                   Q(forum__category__groups__isnull=True))
        try:
            last_read = PostTracking.objects.get(user=request.user).last_read
            if last_read:
                topiccount = topics.filter(last_post__updated__gte=last_read).count()
            else:
                topiccount = 0
        except PostTracking.DoesNotExist:
            topiccount = len([topic for topic in topics if forum_extras.has_unreads(topic, request.user)])
    else:
        topiccount = 0

    clanmemberstatus = 'Clanmember' in request.user.groups.all()
    
    fightuscount = FightUs.objects.count()
    return {'unread_topics':topiccount, 'is_clanmember': clanmemberstatus, 'fightus_count': fightuscount}
