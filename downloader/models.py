from django.db import models


# Create your models here.

class DownloadReq(models.Model):
    """
    specially for biqle.ru URLs
    """
    url = models.CharField(default='', max_length=512)
    thumbnail = models.FileField(upload_to='download-app')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.url, self.created_at)
