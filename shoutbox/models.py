from django.db import models

from django.contrib.auth.models import User

class ShoutboxEntry(models.Model):
    """A single entry in Shoutbox"""

    author_name = models.CharField(max_length=100)
    author = models.ForeignKey(User, blank=True, null=True)
    ip = models.IPAddressField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text