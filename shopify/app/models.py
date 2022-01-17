from django.db import models
import random, string

class inventorymodel(models.Model):
    identifier = models.CharField(max_length = 500, default=str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))))
    itemname = models.CharField(max_length = 500, null = False, blank = False)
    descriptiom = models.CharField(max_length = 5000, null = True, blank = True)
    unitprice = models.IntegerField(blank=True, null=True)
    instockquantity = models.IntegerField(blank=True, null=True)
    reorderlevel = models.IntegerField(blank=True, null=True)
    reorderdays = models.IntegerField(blank=True, null=True)
    ordered = models.IntegerField(blank=True, null=True)
    discontinued = models.BooleanField(default= False)


    def __str__(self):
        return str(self.itemname)

