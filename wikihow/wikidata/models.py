# TODO: Check whether guarding this code with this ` if ` is really necessary.
from django.db import models


class Content(models.Model):
    url_text = models.CharField(max_length=100)
    content = models.TextField()
    scrape_time = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.url_text
