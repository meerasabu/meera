"""Art_Touch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  django.conf import settings
from django.conf.urls.static import static
from artco import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),

    #registeration
    path('ureg',views.u_register),
    path('areg',views.a_register),

    #approvel&reject #dashboard-admin
    path('artist/<n>',views.artist_table),
    path('approve/<int:n>',views.approval),
    path('reject/<n>',views.reject),

    path('confirm',views.artist_total),

    path('admin',views.admin_page),
    path('artist_vw',views.artist_vw),
    path('user_vw',views.user_vw),
    path('artist_reject',views.artist_rejected),
    path('arti_revw',views.art_review_vw),
    path('arti_fed',views.art_feedback_vw),
    path('arti_com',views.art_compliants_vw),
    #login and logout
    path('logp',views.login_page),
    path('log',views.log),

    path('admin_out',views.admin_logout),
    path('user_out',views.user_logout),
    path('artist_out',views.artist_logout),


    #artist_page
    path('art_hm',views.artist_home),
    path('art_pro',views.artist_profile),
    path('artp_updt',views.apro_update),
    path('art_work',views.art_work),
    path('art_upload',views.art_upload),
    path('work_vw',views.work_vw),
    path('review_vw/<n>',views.review_vw),
    path('a_pend',views.a_pending),

    #user
    path('user',views.shop),
    path('abt',views.user_about),
    path('user1',views.user1),
    path('single/<x>',views.single),
    path('revw',views.user_review),
    path('u_art',views.u_artist),
    path('u_odr',views.u_order_vw),

    #checkout & Cart
    path('add_ads',views.add_address),
    path('add_ads1',views.add_address1),
    path('payment',views.payment),
    path('cart',views.cart),
    path('user_pro',views.user_profile),
    path('checkout',views.checkout),
    path('check/<n>',views.checkout1),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)