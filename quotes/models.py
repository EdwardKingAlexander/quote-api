from django.db import models

# Create your models here.
class Quote(models.Model):
    title = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.customer_name}" 
