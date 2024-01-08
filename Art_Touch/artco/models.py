from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=10,null=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return str(self.username)

class User_Register(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=30,null=True)
    mobileNo = models.IntegerField(null=True)
    address = models.TextField(null=True)
    profilePic = models.FileField(null=True)
    pin = models.IntegerField(null=True)
    username = models.CharField(max_length=30,null=True)

    def __str__(self) :
        return str(self.name)

class Artist_Register(models.Model):
    a_name = models.CharField(max_length=200,null=True)
    a_email = models.CharField(max_length=30,null=True)
    a_mobileNo = models.CharField(max_length=15,null=True)
    a_address = models.TextField(null=True)
    a_profilePic = models.FileField(null=True)
    a_identity = models.FileField(null=True)
    qualification = models.CharField(max_length=400, null=True)
    action = models.CharField(max_length=15)
    username = models.CharField(max_length=30, null=True)

    def __str__(self) :
        return str(self.a_name)

class ArtWork(models.Model):
    username = models.CharField(max_length=30, null=True)
    artist_name = models.CharField(max_length=200,null=True)
    work = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    quantity = models.IntegerField(null=True)
    price = models.CharField(max_length=30,null=True)
    def __str__(self) :
        return str(self.username)

class AddToCart(models.Model):
    username = models.CharField(max_length=30,null=True)
    item_id = models.IntegerField(null=True)
    item = models.CharField(max_length=30, null=True)
    qnty = models.IntegerField(null=True)
    item_total = models.IntegerField(null=True)
    add_status = models.CharField(max_length=15)
    artist_name = models.CharField(max_length=200,null=True)
    def __str__(self) :
        return str(self.username)

class Payments(models.Model):
    username = models.CharField(max_length=30,null=True)
    name = models.CharField(max_length=30,null=True)
    phn_no = models.CharField(max_length=15,null=True)
    landmark = models.TextField(null=True)
    total = models.IntegerField(null=True)
    p_status = models.CharField(max_length=15)
    def __str__(self) :
        return str(self.username)

# class PaymentMode(models.Model):
#     username = models.CharField(max_length=30,null=True)
#     card_owner = models.CharField(max_length=30,null=True)
#     total_amt = models.IntegerField(null=True)
#     card_no = models.IntegerField(null=True)
#     cvv = models.IntegerField(null=True)
#     expiry = models.DateField()
#     def __str__(self) :
#         return str(self.username)

class Reviews(models.Model):
    username = models.CharField(max_length=30, null=True)
    user_img = models.FileField(null=True)
    email = models.CharField(max_length=30, null=True)
    category = models.CharField(max_length=30, null=True)
    name_artist = models.CharField(max_length=30, null=True)
    quality = models.CharField(max_length=30, null=True)
    comments = models.TextField(null=True)
    def __str__(self) :
        return str(self.username)

class My_Order(models.Model):
    username = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=200, null=True)
    m_item_id = models.IntegerField(null=True)
    m_item = models.CharField(max_length=30, null=True)
    m_qnty = models.IntegerField(null=True)
    m_total = models.IntegerField(null=True)
    m_status = models.CharField(max_length=15)
    def __str__(self) :
        return str(self.username)

class Order_Recieved(models.Model):
    user_name = models.CharField(max_length=30, null=True)
    o_name = models.CharField(max_length=200, null=True)
    o_item_id = models.IntegerField(null=True)
    o_item = models.CharField(max_length=30, null=True)
    o_qnty = models.IntegerField(null=True)
    o_total = models.IntegerField(null=True)
    o_status = models.CharField(max_length=15)
    def __str__(self) :
        return str(self.user_name)


