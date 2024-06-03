from email.message import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from dangnhap import settings
from .form import AddCoffeeForm, OrderCoffeeForm # type: ignore
from django.contrib.auth.decorators import login_required
from authentication.models import Coffee
from authentication.models import Order
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

# import openai
import os


# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
# from . tokens import generate_token
# from django.urls.http import urlsafe_base64_decode, urlsafe_base664_encode

# Create your views here.
def home(request): # Nhan yeu cau
    return render(request, "authentication/index.html") # Tra ve phan hoi 

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        ## Lay gia tri cua tu POST

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username")
            return redirect('home')
        
        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already registered!")
        #     return redirect('home')
        
        # if len(username) > 10:
        #     messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")

        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!")
        #     return redirect('home')

        myuser = User.objects.create_user(username, email, pass1) # tạo một đối tượng User mới trong Django.
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False # Vô hiệu hóa tài khoản người dùng không cho đăng nhập vào hệ thống

        myuser.save() # Luu thay doi vao co so du lieu

        messages.success(request, "Your Account has been successfully created.") # Tạo một tin nhắn thành công trong Django

        # Welcome Email

        # subject = "Welcome to Analyst"
        # message = "Hello " + myuser.first_name + "!! \n" + " Welcome to Analyst"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=False)


        # # Email Address
        # current_site = get_current_site(request)
        # email_subject = "Confirm your email @ Analyst - Login!"
        # message2 = render_to_string('email_confirmation.html', {
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()



        return redirect('signin')


    return render(request, "authentication/signup.html")


def send_test_email(request):
    subject = "Test Email"
    message = "This is a test email."
    from_email = settings.EMAIL_HOST_USER
    to_list = ['truongnqfx@gmail.com']
    try:
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1) # goi phuong thuc xac thuc co khop mat khau trong co so du lieu hay khong
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {"fname": fname})
        else:
            messages.error(request, "Dang Nhap that bai")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Dang xuat thanh cong")
    return redirect('home')

# def activate(request, uidb64, token):
#     try: 
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pd=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         myuser.save()
#         login(request, myuser)
#         return redirect('home')
#     else:
#         return render(request, 'activation_failed.html')




def coffee(request):
    coffee_list = Coffee.objects.all()
    return render(request, "coffee.html", {'coffees': coffee_list})
    # return render(request, "base_coffee.html")

def list_coffee(request, pk):
    list_coffee = Coffee.objects.get(id=pk)
    return render(request, "list_coffee.html", {'list_coffee': list_coffee})

def delete_coffee(request, pk):
    delete_coffee = Coffee.objects.get(id=pk)
    delete_coffee.delete()
    messages.success(request, "Bạn vừa xóa 1 bản ghi")
    return redirect('coffee')

def add_coffee(request):
    form = AddCoffeeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_coffee = form.save()
            messages.success(request, "Đã thêm bản ghi")
            return redirect('coffee')
    return render(request, 'add_coffee.html', {'form': form})

def update_coffee(request, pk):
    current_coffee = Coffee.objects.get(id=pk)
    form = AddCoffeeForm(request.POST or None, instance=current_coffee)
    if form.is_valid():
        form.save()
        messages.success(request, "Bản ghi đã cập nhật")
        return redirect('coffee')
    return render(request, 'update_coffee.html', {'form':form})

def quantity_coffee(request, pk):
    select_coffee = Coffee.objects.get(id=pk)
    form = OrderCoffeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Bản ghi đã cập nhật")
        return redirect('coffee')
    return render(request, 'quantity_coffee.html', {'form':form})

def order_coffee(request):
    if request.method == "POST":
        coffee_id = request.POST.get('coffee_id')
        quantity = request.POST.get('quantity')

        # Kiểm tra xem coffee_id có hợp lệ không
        if coffee_id is None or not coffee_id.isdigit():
            messages.error(request, "ID của cà phê không hợp lệ.")
            return redirect('order_coffee')

        coffee_id = int(coffee_id)

        # Kiểm tra xem quantity có được cung cấp và có hợp lệ không
        if not quantity:
            messages.error(request, "Vui lòng nhập số lượng.")
            return redirect('order_coffee')

        try:
            quantity = int(quantity)
        except ValueError:
            messages.error(request, "Số lượng không hợp lệ.")
            return redirect('order_coffee')

        coffee = get_object_or_404(Coffee, id=coffee_id)

        order, created = Order.objects.get_or_create(
            coffee=coffee,
            defaults={'quantity': quantity, 'total': coffee.price * quantity}
        )

        if not created:
            order.quantity += quantity
            order.total += coffee.price * quantity
            order.save()

    coffees = Coffee.objects.all()
    total_price = sum(coffee.price * coffee.quantity for coffee in coffees if coffee.price is not None and coffee.quantity is not None)

    return render(request, 'order_coffee.html', {'coffees': coffees, 'total_price': total_price})

@login_required
def reset_cart(request):
    coffees = Coffee.objects.all()
    for coffee in coffees:
        Order.objects.create(
            coffee=coffee,
            quantity=coffee.quantity,
            total=coffee.price * (coffee.quantity or 1)  # Sử dụng 1 làm mặc định nếu quantity là None
        )
    
    # Xóa tất cả các bản ghi trong bảng Order
    Order.objects.all().delete()
    
    messages.success(request, "Bạn vừa lưu và xóa hết bản ghi")
    return redirect('order_coffee')