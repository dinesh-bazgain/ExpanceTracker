from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseIncome(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    transcation_choices = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    transcation_type = models.CharField(
        max_length=10,
        choices=transcation_choices
    )

    tax = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    tax_type_choices = [
        ('flat', 'Flat'),
        ('percentage', 'Percentage')
    ]
    tax_type = models.CharField(
        max_length=10,
        choices=tax_type_choices,
        default='flat'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total(self):
        if self.tax_type == 'flat':
            return self.amount + self.tax
        else:
            return self.amount + (self.amount * self.tax / 100)
        
    def __str__(self):
        return f"{self.title} - {self.transcation_type} - Rs. {self.amount}"