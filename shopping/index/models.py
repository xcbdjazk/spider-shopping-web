from django.db import models

# Create your models here.
class Product_class(models.Model):
    pcid=models.AutoField(primary_key=True)
    sort=models.CharField(max_length=32)

class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=32)
    img_path=models.CharField(max_length=100)
    price=models.FloatField()
    Stock=models.CharField(max_length=10)
    is_host=models.BooleanField()
    recommend=models.CharField(max_length=500)
    product_class=models.ForeignKey("Product_class",to_field="pcid",default=1,on_delete=models.CASCADE)

class User(models.Model):
    uid=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    gender=models.CharField(max_length=10)
    dtime=models.DateField()
class Cart(models.Model):
    cid=models.AutoField(primary_key=True)
    img_path = models.CharField(max_length=100)
    pname = models.CharField(max_length=32)
    price = models.FloatField()
    count=models.CharField(max_length=5)
    totalprice=models.FloatField()
    ctime = models.DateField()
    user = models.ForeignKey("User", to_field="uid",on_delete=models.CASCADE)
class Order_info(models.Model):
    oid=models.AutoField(primary_key=True)
    img_path = models.CharField(max_length=100)
    pname = models.CharField(max_length=32)
    price = models.FloatField()
    count=models.CharField(max_length=5)
    totalprice=models.FloatField()
    ctime = models.DateField()
    user = models.ForeignKey("User", to_field="uid",on_delete=models.CASCADE)
class Spider_Porduct(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=1000)
    price=models.CharField(max_length=10)
    url_link=models.CharField(max_length=1000)
    img_path=models.CharField(max_length=1000)
    spider = models.ForeignKey("Spider_Porduct_item", to_field="spid",default=1,on_delete=models.CASCADE)
class Spider_Porduct_item(models.Model):
    spid=models.AutoField(primary_key=True)
    option_url=models.CharField(max_length=20)
    option_product=models.CharField(max_length=32)