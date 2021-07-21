from django.db import models

# Create your models here.


class product(models.Model):
    category_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=200, default="")
    product_spice = models.IntegerField(default=0, null=True)
    product_desception = models.CharField(max_length=2000, default="")
    product_image = models.ImageField()

    def __str__(self):
        return self.product_name


class category(models.Model):
    category_name = models.CharField(max_length=100, default="")
    id_mom = models.IntegerField(default=None)

    def __str__(self):
        return self.category_name


class customer(models.Model):
    customer_name = models.CharField(max_length=100, default="")
    customer_address = models.CharField(max_length=500, default="")
    customer_phone = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.customer_name


class order(models.Model):
    product_id = models.IntegerField(default=0, null=True)
    customer_id = models.IntegerField(default=0, null=True)
    fee_and_ship = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.product_id


class info(models.Model):
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100)

