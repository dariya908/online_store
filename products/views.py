from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .filters import ProductFilter
from .models import *
from .forms import SignupForm
from .forms import OrderForm, ProfileForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from .token import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode



# Create your views here.



def products_page(request):
    products = Product.objects.all()
    filter=ProductFilter(request.GET,queryset=products)
    products=filter.qs
    return render(request, 'products/products.html', {"products": products,'filter':filter})


def order_page(request, product_id):
    try:
        profile=Profile.objects.get(user=request.user)
        product = Product.objects.get(id=product_id)
        total_price = 0
        sale = 0.2
        discount_price = 0

        form = OrderForm(initial={'product': product, 'user':request.user})
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                if product.sale:
                    total_price = product.price * form.cleaned_data['quantity']
                    discount_price = product.price * form.cleaned_data['quantity'] * sale
                    total_price = total_price - discount_price
                else:
                    total_price = product.price * form.cleaned_data['quantity']
                if form.cleaned_data['payment_method']=="wallet":
                    if profile.wallet>=total_price:
                        profile.wallet-=total_price
                        profile.order_count += 1
                        profile.save()
                        return  HttpResponse('спасибо за покупку')
                    else:
                        return HttpResponse('Not enough money!')

                else:
                    profile.order_count+=1
                    profile.save()
                form.save()

        return render(request, 'products/order.html',
                      {"form": form, "total_price": total_price, "discount_price": discount_price, })
    except Product.DoesNotExist:
        return HttpResponse('Not Found!')


def registrasia_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "welcome to our  site!!!"
            body = render_to_string('products/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data['username']
            message = EmailMessage(subject=subject, body=body, to=[to_email, ])
            message.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    return render(request, 'products/registrasia.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    orders = user.order_set.all()
    return render(request, 'products/user.html', {"user": user, "orders": orders})


def aboutus_page(request):
    aboutus = AboutUs.objects.all()
    return render(request, 'products/about_us.html', {"aboutus": aboutus, })


def contakts_page(request):
    contakts = Contakts.objects.all()
    return render(request, 'products/contakts.html', {"contakts": contakts})


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/order.html', {'form': form})


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('products')
    return render(request, 'products/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')


def account_settings(request):
    try:
        user = request.user.profile
        order_user = request.user
        orders = order_user.order_set.all()
        form = ProfileForm(instance=user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
        context = {'form': form, 'orders': orders}
        return render(request, 'products/profile.html', context)
    except AttributeError:
        return redirect('login_page')
