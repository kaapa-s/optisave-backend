from django.db import models
from bank import Bank
from checklist_item import ChecklistItem

class Promotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    profit = models.DecimalField(max_digits=19, decimal_places=10, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    note = models.TextField()

    checklist = models.ManyToManyField(CheklistItem)