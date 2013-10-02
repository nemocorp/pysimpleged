from django.db import models

from django.contrib.auth.models import User

def scan_doc(instance,filename):
    return filename

class Tag(models.Model):
    tag = models.CharField(max_length=25)

    def __str__(self):
        return self.tag

    def __unicode__(self):
        return self.tag

class Document(models.Model):
    title = models.CharField(max_length=60)
    upload = models.DateField(auto_now_add=True)
    uploader = models.ForeignKey(User)
    official_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    scan = models.FileField(upload_to=scan_doc)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


