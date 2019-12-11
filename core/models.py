from django.db import models


class AbstractTimeStamp(models.Model):

    """ Abstract Time Stamp """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # meta class abstract definition / not to register database
    class Meta:
        abstract = True
