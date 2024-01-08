from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User_Register)
admin.site.register(Artist_Register)
admin.site.register(Login)
admin.site.register(ArtWork)
admin.site.register(AddToCart)
admin.site.register(Payments)
admin.site.register(Reviews)
admin.site.register(My_Order)
admin.site.register(Order_Recieved)