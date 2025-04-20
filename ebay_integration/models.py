# ebay_integration/models.py
from django.db import models

class EbayProduct(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Startprice = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.CharField(max_length=100)
    condition = models.IntegerField()  
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.title
    
class EbayCategory(models.Model):
    category_id = models.CharField(max_length=100, unique=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name 
    