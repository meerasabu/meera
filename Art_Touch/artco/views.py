from django.shortcuts import render,redirect,HttpResponse
from .models import *
import razorpay
from django.contrib import messages
# Create your views here.

def index(request):
    if 'admin_id' in request.session:
        x = request.session['admin_id']
        return render(request,'admin_dashboard.html')
    elif 'user_id' in request.session:
        x = request.session['user_id']
        data = ArtWork.objects.all()
        return render(request, 'user1.html', {'r': data})
    elif 'artist_id' in request.session:
        x = request.session['artist_id']
        data = Artist_Register.objects.get(username=x)
        return render(request,'artist_home.html',{'i': data})
    else:
        return redirect(log)

#------------------------------------------ user and artist registration -----------------------------------------------
def u_register(request):
    if request.method == 'POST':
        x1 = request.POST['u1']
        x2 = request.POST['u2']
        x3 = request.FILES['u3']
        x4 = request.POST['u4']
        x5 = request.POST['u5']
        x6 = request.POST['u6']
        x7 = request.POST['u7']
        x8 = request.POST['u8']

        data = User_Register.objects.create(name=x1,email=x2,profilePic=x3,mobileNo=x4,address=x5,pin=x6,username=x7)
        data.save()
        data1 = Login.objects.create(username=x7,password=x8,status=1)
        data1.save()
        return redirect(index)
    else:
        return render(request,'u_register.html')

def a_register(request):
    if request.method == 'POST':
        x2 = request.POST['a2']
        x3 = request.POST['a3']
        x4 = request.POST['a4']
        x5 = request.POST['a5']
        x6 = request.POST['a6']
        x7 = request.FILES['a7']
        x8 = request.POST['a8']
        x9 = request.POST['a9']
        x1 = request.FILES['a1']
        data = Artist_Register.objects.create(a_profilePic=x1,a_name=x2,a_email=x3,a_address=x4,a_mobileNo=x5,qualification=x6,a_identity=x7,username=x8,action='pending')
        data.save()
        data1 = Login.objects.create(username=x8,password=x9,status=2)
        data1.save()
        return redirect(index)
    else:
        return render(request,'a_register.html')

#--------------------------------- login & logout ----------------------------------------------------

def login_page(request):
    return render(request,'login.html')


def log(request):
    if request.method == 'POST':
        u = request.POST['u']
        p = request.POST['p']
        try:
            data = Login.objects.get(username=u)

            if data.password == p and data.status == 0:
                request.session['admin_id'] = u
                return render(request,'admin_dashboard.html')

            elif data.password == p and data.status == 1:
                request.session['user_id'] = u
                data = ArtWork.objects.all()
                return render(request, 'user1.html', {'r': data})

            elif data.password == p and data.status == 2:
                request.session['artist_id'] = u
                data1 = Artist_Register.objects.get(username=request.session['artist_id'])
                return render(request,'artist_home.html',{'i':data1})

            else:
                messages.info(request, "password incorrect")
                return render(request, "login.html")

        except Exception:
            messages.info(request, "Username incorrect")
            return render(request, "login.html")

    else:
        return render(request,'index.html')

def admin_logout(request):
    if 'admin_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)

def user_logout(request):
    if 'user_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)

def artist_logout(request):
    if 'artist_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)


#------------------------------------------------ artist home -------------------------------------------------
def artist_home(request):
    if 'artist_id' in request.session:
        x = request.session['artist_id']
        data = Artist_Register.objects.get(username=x)
        return render(request, 'artist_home.html', {'i': data})
    else:
        return render(request,'artist_home.html')
def artist_profile(request):
    if 'artist_id' in request.session:
        x = request.session['artist_id']
        data = Artist_Register.objects.get(username=x)
        return render(request, 'artist_profile.html', {'i': data,'r':data.action})
    else:
        return render(request,'artist_home.html')

def apro_update(request):
    if request.method == 'POST':
        a = request.FILES['a1']
        b = request.POST['a2']
        c = request.POST['a3']
        d = request.POST['a4']
        e = request.POST['a5']
        f = request.POST['a6']
        g = request.FILES['a7']
        data = Artist_Register.objects.filter(username=request.session['artist_id'])
        data.update(profilePic=a,a_name=b,a_email=c,a_address=d,a_mobileNo=e,qualification=f,a_identity=g)
        return render(request,'artist_home.html')
    else:
        data1 = Artist_Register.objects.filter(username=request.session['artist_id'])
        return render(request, 'a_pro_update.html', {'r': data1})

def art_work(request):
    if 'artist_id' in request.session:
        x = request.session['artist_id']
        data = Artist_Register.objects.get(username=x)
        return render(request, 'art_work.html', {'i': data,'r':data.action})
    else:
        return render(request,'artist_home.html')

def art_upload(request):
    if request.method == 'POST':
        a1 = request.POST['w1']
        a2 = request.POST['w2']
        a3 = request.FILES['w3']
        a4 = request.POST['w4']
        a5 = request.POST['w5']
        x = request.session['artist_id']
        data1 = Artist_Register.objects.get(username=x)
        data = ArtWork.objects.create(username=request.session['artist_id'],artist_name=data1.a_name,work=a1,description=a2,image=a3,quantity=a4,price=a5)
        data.save()
        return redirect(index)
    else:
        return render(request, 'art_work.html')

def work_vw(request):
    if 'artist_id' in request.session:
        x = request.session['artist_id']
        d = Artist_Register.objects.get(username=x)
        data = ArtWork.objects.filter(username=x)
        return render(request, 'work_vw.html',{'a':data,'r':d.action})
    else:
        return render(request,'work_vw.html')

def review_vw(request,n):
    if request.method == 'GET':
        d1 = Artist_Register.objects.get(username=request.session['artist_id'])
        data = Reviews.objects.filter(name_artist=n)
        return render(request, 'review_vw.html', {'a': data,'k':d1.action})
    else:
        return render(request, 'review_vw.html')


def a_pending(request):
    if request.method == 'GET':
        x = request.session['artist_id']
        print(x)
        d1 = Artist_Register.objects.get(username=x)
        d2 = My_Order.objects.filter(name=d1.a_name)
        return render(request,'a_pending.html',{'r':d2,'k':d1.action})
    #     # Assuming 'artist_id' is stored in the session
    #     artist_id = request.session.get('artist_id')
    #
    #     if artist_id:
    #         # Retrieve data from Artist_Register model
    #         artist_data = Artist_Register.objects.filter(username=artist_id).first()
    #
    #         if artist_data:
    #             # Check if a_name in Artist_Register matches name in Order_Received
    #             order_data = Order_Recieved.objects.filter(o_name=artist_data.a_name)
    #             print(order_data)
    #
    #             # You can now pass these data to your template
    #             # context = {
    #             #     'artist_data': artist_data,
    #             #     'order_data': order_data,
    #             # }
    #
    #             # Render the template with the context
    #             return render(request, 'a_pending.html', {'artist_data': artist_data,'order_data': order_data,})
    #         else:
    #             # Handle the case when artist_data is not found
    #             return HttpResponse("Artist data not found.")
    #     else:
    #         # Handle the case when 'artist_id' is not in the session
    #         # You may redirect to a login page or do something else
    #         return HttpResponse("Artist ID not found in session. Please log in.")
    #
    # # Handle other HTTP methods if needed
    # return HttpResponse("Invalid HTTP method.")







#--------------------------------------------- admin dashboard---------------------------------------------


def admin_page(request):
    return render(request,'admin_dashboard.html')

def artist_vw(request):
    if request.method == 'GET':
        data= Artist_Register.objects.filter(action='pending')
        return render(request,'artist_table.html',{'r':data})

def artist_table(request,n):
    if request.method == 'GET':
        data = Artist_Register.objects.filter(id=n)
        return render(request, 'artist_vw.html', {'r': data})
    else:
        return render(request,'artist_vw.html')

def approval(request,n):
    if request.method == 'GET':
        data = Artist_Register.objects.filter(id=n)
        data.update(action='confirmed')
        return redirect(artist_vw)
    else:
        return render(request, 'artist_table.html')

def reject(request,n):
    if request.method == 'GET':
        data = Artist_Register.objects.filter(id=n)
        data.update(action='rejected')
        return redirect(artist_vw)
    else:
        return render(request, 'artist_table.html')

def artist_total(request):
    if request.method == 'GET':
        data= Artist_Register.objects.filter(action='confirmed')
        return render(request,'artist_total.html',{'r':data})

def artist_rejected(request):
    if request.method == 'GET':
        data= Artist_Register.objects.filter(action='rejected')
        return render(request,'artist_total.html',{'r':data})

def user_vw(request):
    if request.method == 'GET':
        data= User_Register.objects.all()
        return render(request,'user_table.html',{'r':data})

def art_review_vw(request):
    if request.method == 'GET':
        data = Reviews.objects.all()
        return render(request,'admin_art_reviews.html',{'r':data})

def art_feedback_vw(request):
    if request.method == 'GET':
        data = Reviews.objects.filter(category='feedback')
        return render(request, 'ad_arti_feedback.html', {'r': data})

def art_compliants_vw(request):
    if request.method == 'GET':
        data = Reviews.objects.filter(category='complaint')
        return render(request, 'ad_arti_compliant.html', {'r': data})

# def all_order(request):
#     if request.method == 'GET':
#         data = My_Order.objects.all()
#         return render(request, 'ad_arti_compliant.html', {'r': data})

#----------------------------------------user page--------------------------------------------------------------



def shop(request):
    if request.method == 'GET':
        data= ArtWork.objects.all()
        return render(request,'user1.html',{'r':data})

def user_about(request):
    return render(request,'about.html')

def user1(request):
    if request.method == 'GET':
        data = ArtWork.objects.all()
        return render(request, 'user2.html', {'r': data})
    else:
        return render(request,'user2.html')

def single(request,x):
    if request.method == 'GET':
        data = ArtWork.objects.filter(id=x)
        return render(request,'single.html',{'s':data})
    else:
        data = ArtWork.objects.all()
        return(request,'single.html',{'r':data})

def user_profile(request):
    if 'user_id' in request.session:
        x = request.session['user_id']
        data = User_Register.objects.get(username=x)
        return render(request, 'user_profile.html', {'i': data})
    else:
        return render(request,'user_profile.html')

def user_review(request):
    if request.method == "POST":
        x1 = request.POST['a1']
        x2 = request.POST['a2']
        x3 = request.POST['a3']
        x4 = request.POST['a4']
        x5 = request.POST['a5']
        x6 = request.POST['a6']
        data = Reviews.objects.create(username=x1,email=x2,category=x3,name_artist=x4,quality=x5,comments=x6)
        data.save()
        return render(request,'user1.html')
    else:
        data = Artist_Register.objects.all()
        return render(request,'user_review.html',{'artist':data})

def u_artist(request):
    if request.method == "GET":
        data = Artist_Register.objects.all()
        return render(request, 'u_artist_vw.html', {'artist': data})

def u_order_vw(request):
    if request.method == 'GET':
        data = My_Order.objects.filter(username=request.session['user_id'])
        return render(request,'u_order_vw.html',{'r':data})


# -----------------------------------------cart and payment----------------------------------------------



def cart(request):
    if request.method == 'POST':
        x = request.session['user_id']
        # print(x)
        a1 = request.POST['work']
        # a = request.FILES['img']
        a2 = int(request.POST['item_id'])
        a3 = request.POST['price']
        a6 = request.POST['a_name']
        # print(a2)
        try:
            data = AddToCart.objects.get(item_id=a2)
            # print("sdefsdfdsfdsfdsf")
            # print(type(data.item_id),"dhfgds")
            if data.username == x:
                # print("Matching")
                a4 = data.qnty + 1
                a5 = int(a3)*int(a4)
                AddToCart.objects.filter(username=x,item_id=a2).update(qnty=a4,item_total=a5)
                return redirect(index)
            else:
                AddToCart.objects.create(username=request.session['user_id'], item=a1, item_id=a2, item_total=a3,qnty=1, artist_name=a6, add_status='pending')
                return redirect(index)
        except Exception:
            AddToCart.objects.create(username=request.session['user_id'], item=a1, item_id=a2, item_total=a3, qnty=1, artist_name=a6, add_status='pending')
            return redirect(index)
    else:
        return render(request, 'user1.html')


def checkout(request):
    if request.method == 'GET':
        x = request.session['user_id']
        data = AddToCart.objects.filter(username=x)
        s=0
        for i in data:
           s = i.item_total+s
        d = Payments.objects.filter(username=x)
        if list(d)==[]:
            Payments.objects.create(username=x,name='nill',phn_no='nill',landmark='nill',total=s, p_status='pending')
        else:
            d.update(total=s)
        request.session['am']=s
        total = Payments.objects.get(username=x)
        # print(total.total)
        data1 = User_Register.objects.filter(username=x)
        return render(request,'checkout.html',{'r':data,'k':data1,'q':total.total})

    else:
        return render(request,'checkout.html')


def checkout1(request,n):
    if request.method == 'GET':
        data = AddToCart.objects.filter(id=n)
        data.delete()
        return redirect(checkout)
    else:
        return render(request, 'checkout.html')


def add_address(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['phn_no']
        c = request.POST['landmark']
        data = Payments.objects.filter(username=request.session['user_id'])
        data.update(name=a,phn_no=b,landmark=c)
        d = Payments.objects.get(username=request.session['user_id'])
        return render(request,'add_address.html',{'r':d})
    else:
        return render(request,'add_address.html')

def add_address1(request):
    if request.method == 'GET':
        data = Payments.objects.filter(username=request.session['user_id'])
        return render(request, 'add_address.html',{'r':data})

def payment(request):
    x = request.session['am']

    user_id = request.session.get('user_id')
    if not user_id:
        # Handle the case when 'user_id' is not present in the session
        return HttpResponse("User ID not found in session.")

    # Get necessary data in a single query
    user_data = User_Register.objects.filter(username=user_id).first()
    payment_data = Payments.objects.filter(username=user_id).first()
    cart_items = AddToCart.objects.filter(username=user_id)

    if not user_data or not payment_data:
        # Handle the case when user data or payment data is not found
        return HttpResponse("User data or payment data not found.")

    # Update all instances in d1 and d2
    Payments.objects.filter(username=user_id).update(p_status='payed')
    AddToCart.objects.filter(username=user_id).update(add_status='payed')

    # Create instances in My_Order based on AddToCart and Payments, save them, and then delete AddToCart
    for cart_item in cart_items:
        my_order_instance = My_Order.objects.create(
            username=user_id,
            name=cart_item.artist_name,
            m_item_id=cart_item.item_id,
            m_item=cart_item.item,
            m_qnty=cart_item.qnty,
            m_total=payment_data.total,
            m_status=payment_data.p_status
        )
        my_order_instance.save()

        # Add values to Order_Recieved
        order_received_instance = Order_Recieved.objects.create(
            user_name=user_data.username,
            o_name=cart_item.artist_name,
            o_item_id=cart_item.item_id,
            o_item=cart_item.item,
            o_qnty=cart_item.qnty,
            o_total=payment_data.total,
            o_status=payment_data.p_status
        )
        order_received_instance.save()

        # Delete the corresponding AddToCart instance
        cart_item.delete()

    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    # cursor = connection.cursor()
    # cursor.execute("update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(id) + "' ")

    # payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    return render(request, "payment.html", {'n': x})

# def payment(request):
#     x = request.session['am']
#     if request.method == 'GET':
#         z = request.session['user_id']
#         d1 = Payments.objects.filter(username=z)
#         d2 = AddToCart.objects.filter(username=z)
#         d1.update(p_status='payed')
#         d2.update(add_status='payed')
#         if request.method == 'GET':
#             z = request.session['user_id']
#             d = User_Register.object.filter(username=z)
#             d1 = Payments.objects.filter(username=z)
#             d2 = AddToCart.objects.filter(username=z)
#
#
#             # Update all instances in d1 and d2
#             d1.update(p_status='payed')
#             d2.update(add_status='payed')
#
#             # Get the Payments instance
#             payment_instance = d1.first()  # Assuming there is only one Payments instance per user
#
#             # Create instances in My_Order based on AddToCart and Payments, save them, and then delete AddToCart
#             for cart_item in d2:
#                 d3 = My_Order.objects.create(
#                     username=z,
#                     name=cart_item.artist_name,
#                     m_item_id=cart_item.item_id,
#                     m_item=cart_item.item,
#                     m_qnty=cart_item.qnty,
#                     m_total=payment_instance.total,  # Use value from Payments
#                     m_status=payment_instance.p_status  # Use value from Payments
#                 )
#                 d3.save()
#
#                 # Delete the corresponding AddToCart instance
#                 cart_item.delete()
#
#     order_currency = 'INR'
#     client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
#     # cursor = connection.cursor()
#     # cursor.execute("update inspection_details set status='completed', fine_paid_date = curdate() where insp_id='" + str(id) + "' ")
#
#     # payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
#     return render(request, "payment.html",{'n':x})



# def art_work(request):
#     return render(request,'art_work.html')

