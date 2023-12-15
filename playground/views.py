import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Cars, Collection, Custoumer
from .forms import CarsForm, OrderForm

# random code for verfication 
code = str(random.randint(1000,9999))

# shows the cars avalible 
def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    cars = Cars.objects.filter(
        Q(collection__name__icontains=q) |

        Q(creator__icontains=q) |
        Q(name__icontains=q) |
        Q(model__icontains=q) |
        Q(description__icontains=q) |
        Q(pricePerDay__icontains=q) |
        Q(pricePerMonth__icontains=q)
        )
    
    car_count = cars.count()

    collections = Collection.objects.all()

    context = {'cars': cars, 'collection': collections, 'car_count': car_count}
    return render(request, 'playground/home_page.html', context)

# shows the full ditaled car 
def car(request, pk):
    cars = Cars.objects.get(id=pk) 
    context = {'cars': cars}
    return render(request, 'playground/car.html', context)


def sendEmail(email, mail_subject, mail_body):

    gmail_user = 'abod.s.200171@gmail.com'
    gmail_password = 'zwea ykdz msmo vpaa'  # Use the App Password you generated
    sent_from = gmail_user
    to = [email]
    subject = mail_subject
    body = mail_body

    email_text = f"Subject: {subject}\n\n{body}"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()


def orderCar(request, pk):
    car = Cars.objects.get(id=pk)
    try:
        instance = Custoumer.objects.get(car=car)
    except Custoumer.DoesNotExist:
        instance = None

    cus = Custoumer.objects.all()
    form = OrderForm(request.POST or None, instance=instance, initial={'car': car})
    if request.method == 'POST':
        if form.is_valid():
            getcode = request.POST.get('code')
            if getcode == str(code):
                form.save()
                car.rentelStatus = True
                car.save()
                return redirect('home')  
            else:
                mail = request.POST.get('mail')
                body = "welcom to driveRent Mr/Ms: " + request.POST.get('name') + " \nthis is the verfication code for the rent " + str(car) + " \n" + code + "\nthank you for useing DriveRent" 
                sendEmail(mail, 'verfication code', body)

    context = {'form': form, 'vc':code}
    return render(request, 'playground/order_car.html', context)


# for get the manager access 
def logInPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('manager-view')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('manager-view')
        else:
            messages.error(request, 'wrong username or password!!')

    except:
        messages.error(request, 'user dose not exist!!')
    context = {'page':page}
    return render(request, 'playground/login_page.html', context)

def intro(request):
    context = {}
    return render(request, 'playground/intro.html', context)



def FAQs(request):
    context = {}
    return render(request, 'playground/FAQs.html', context)

def contact(request):
    context = {}
    
    if request.method == 'POST':
        mail = 'abedalhmeed.business@gmail.com'
        fname = request.POST.get('fname')
        body = request.POST.get('message')
        cuMail = request.POST.get('mail')
        head = f'Mr.Manager the user {fname} send you this message:{body} and this is the replay mail {cuMail}.'
        
        sendEmail(mail, 'user contact gate', head)

    return render(request, 'playground/contact.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def managerPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    cars = Cars.objects.filter(
        Q(collection__name__icontains=q) |
        Q(creator__icontains=q) |
        Q(name__icontains=q) |
        Q(model__icontains=q) |
        Q(description__icontains=q) |
        Q(pricePerDay__icontains=q) |
        Q(pricePerMonth__icontains=q))
    context = {'cars': cars}
    return render(request, 'playground/manager_page.html', context)


@login_required(login_url='login')
def addCar(request):
    form = CarsForm()
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager-view')

    context = {'form':form}
    return render(request, 'playground/add_car_form.html', context)


@login_required(login_url='login')
def deleteCar(request,pk):
    cars = Cars.objects.get(id=pk)
    if request.method == 'POST':
        cars.delete()
        return redirect('manager-view')
    return render(request, 'playground/delete_car.html', {'obj':cars})


@login_required(login_url='login')
def updateCar(request, pk):
    car = Cars.objects.get(id=pk)
    form = CarsForm(instance=car)
    if request.method == 'POST':
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('manager-view')

    context = {'form':form}
    return render(request, 'playground/add_car_form.html', context)

# User in this project is anyone with manager accsess (manager or co-manager )
@login_required(login_url='login')
def registerUser(request):
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
        form.save()
        return redirect('manager-view')
    else:
        messages.error(request, 'wrong username or password!!')
    return render(request, 'playground/login_page.html', {'form':form})


@login_required(login_url='login')
def ordersListView(request):
    cus = Custoumer.objects.all()
    context = {'cus': cus}
    return render(request, 'playground/orders_list_page.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    custoumer = Custoumer.objects.get(id=pk)
    if request.method == 'POST':
        custoumer.delete()
        mail = custoumer.mail
        subject = 'Order status'
        body = "welcom to driveRent Mr/Ms: " + str(custoumer.name) + " \n\nthank you again for your request to us.  we really appreciate that you took the time and effort to order " + str(custoumer.car) + ".\n\nUnfortunately, we have to inform you that we cannout consider your order to the next stage. \n\nti seems that your information was inaccurate. pleas re-order and verify that the information is correct.  \n\nthank you for useing DriveRent." 
        
        sendEmail(mail, subject, body)

        car = Cars.objects.get(id=custoumer.car.id)
        car.rentelStatus = False
        car.save()

        return redirect('order-list-view')
    return render(request, 'playground/delete_order.html', {'obj':custoumer})
