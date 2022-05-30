from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    uodated = models.DateTimeField(auto_now=True)

    # it wont be saved in the database(just other models can extend it)
    class Meta:
        abstract = True
