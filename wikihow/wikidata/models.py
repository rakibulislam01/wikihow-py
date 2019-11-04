# TODO: Check whether guarding this code with this ` if ` is really necessary.
from django.db import models
from django.db.models.signals import pre_delete  # Receive the pre_delete signal and delete the file associated with the model instance.
from django.dispatch import receiver


class Content(models.Model):
    """
    Save file which crawl from website.
    """
    url_text = models.CharField(max_length=200, default=None)
    user_text = models.CharField(max_length=200, default=None)
    scrape_time = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200, default=None)
    json_file = models.FileField(upload_to='')

    def __str__(self):
        return self.url_text


@receiver(pre_delete, sender=Content)
def json_file_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.json_file.delete(False)
