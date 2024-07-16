from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.AutoField
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Shop/Images",default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    description = models.TextField(default='')
    phone = models.CharField(max_length=20,default='')

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json = models.TextField(null=True, blank=True)
    name=models.CharField(max_length=90)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    country=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestap=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.update_desc[:50]}..."