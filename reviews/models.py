from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleaniness = models.IntegerField()
    location = models.IntegerField()
    chick_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User",
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        related_name="reviews",
        on_delete=models.CASCADE,
    )

    # by defining a foreign key to a sspecific model, we can access the that specific model's fields
    def __str__(self):
        return f"{self.review} - {self.room}"
