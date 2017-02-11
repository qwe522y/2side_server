from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    class Status:
        IN_PROCESS = 1
        ACCEPTED = 0
        REJECTED = 100

    author = models.ForeignKey(User)
    status = models.IntegerField(
        choices=((Status.IN_PROCESS, "В обработке"), (Status.ACCEPTED, "Принятый"), (Status.REJECTED, "Отклоненный")),
        default=Status.IN_PROCESS
    )
    prms = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

