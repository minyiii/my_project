from django.db import models
from django.conf import settings
from django.utils import timezone
# from django.contrib.auth.models import User

class Mindmap(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    describe = models.CharField(max_length=60)
    md_file = models.FileField(upload_to='uploads_md/') # md檔
    json_file = models.FileField(upload_to='uploads_json/') # json檔
    # edit_time = models.DateTimeField(default=timezone.now)
    edit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}".format(self.author, str(self.id))