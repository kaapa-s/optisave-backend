from django.db import models

class ChceklistItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(blank=False)
    deadline = models.DateField(blank=False)
