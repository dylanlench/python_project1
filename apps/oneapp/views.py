from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def logandreg(request):
    return render(request, "oneapp/index.html")

def register(request):
    errors = False
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request, 'Email is invalid')
        errors = True
    if(len(request.POST['password']) < 1):
        messages.error(request, 'Password is required')
        errors = True
    if(request.POST['password'] != request.POST['confirm_password']):
        messages.error(request, 'Passwords do not match')
        errors = True

    if(errors):
        return redirect('/')

    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    admin = Admin.objects.create(
        email = request.POST['email'], 
        password = hashed, 
    )

    request.session['admin_id'] = admin.id
    return redirect('/main')

def login(request):
    try:
        admin = Admin.objects.get(email = request.POST['email'])
        if(bcrypt.checkpw(request.POST['password'].encode(), admin.password.encode())):
            request.session['admin_id'] = admin.id
            return redirect('/main')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
    except Admin.DoesNotExist:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def main(request):
    if 'admin_id' not in request.session:
        messages.error(request, 'please log in or register')
        return redirect('/')
    else:
        context = {
            'all_orders' : Order.objects.all()
        }
        return render(request, 'oneapp/main.html', context)

def orderpage(request, order_id):
    if 'admin_id' not in request.session:
        messages.error(request, 'please log in or register')
        return redirect('/')
    else:
        this_order = Order.objects.get(id = order_id )
        context = {
            'all_products' : this_order
        }
        return render(request, "oneapp/order_page.html", context)

def adminproducts(request):
    if 'admin_id' not in request.session:
        messages.error(request, 'please log in or register')
        return redirect('/')
    else:
        context = {
            'all_products' : Product.objects.all()
        }
        return render(request, 'oneapp/admin_products.html', context)