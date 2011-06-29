from shoutbox.views import recent_entries as shoutbox_recent_entries, postform as shoutbox_postform
from news.views import recent_entries as news_recent_entries

from djangobb_forum.util import render_to
from django.utils.safestring import mark_safe

@render_to("frontpage/frontpage.html")
def frontpage(request):
    """Render the front page"""

    news_top = mark_safe(news_recent_entries(request, 1, "news/recents_top.html").content)
    news_older = mark_safe(news_recent_entries(request, 3, "news/recents_older.html", 1).content)

    return locals()
