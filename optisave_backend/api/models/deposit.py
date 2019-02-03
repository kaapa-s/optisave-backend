from django.db import models
from bank import Bank


PERIODS_CHOICES = (
    ('END', 'End'),
    ('YEAR', 'Yearly'),
    ('MONTH', 'Monthly'),
    ('DAY', 'Daily'),
)

class Deposit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, null=True)

    amount = models.DecimalField(max_digits=19, decimal_places=10, blank=False)
    interest = models.DecimalField(max_digits=19, decimal_places=10, blank=False)
    period = models.CharField(
        max_length=5,
        choices=PERIODS_CHOICES,
        default=PERIODS_CHOICES[0][0],
    )
    tax = models.DecimalField(max_digits=19, decimal_places=10, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    note = models.TextField()