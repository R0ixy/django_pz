from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def changemode(request, dark):
    colour = dark
    return render(request, 'main/index.html', {"colour": colour})


def index(request):
    product = Product.objects.all()
    return render(request, "main/index.html", {"product": product})



def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')

@login_required(login_url="/accounts/login/")
@csrf_exempt
def addproduct(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request, 'main/addproduct.html', {"category": category})
    if request.method == 'POST':
        category = request.POST["category"]
        name = request.POST["name"]
        price = request.POST["price"]
        description = request.POST["description"]
        image = request.POST["img"]

        if Category.objects.filter(name=category):
            new_product = Product(title=name, price=price, category=Category.objects.get(name=category), image=image,
                                  description=description)
            new_product.save()

        product = Product.objects.all()
        return render(request, 'main/index.html', {"product": product})


def delivery(request):
    return render(request, 'main/delivery.html')


def add_and_save(request):
    if request.method == 'POST':
        fb = FeedbackForm(request.POST)
        if fb.is_valid():
            fb.save()
            # Вывод страницы, отображающей список объявлений, относящихся
            # к категории, заданной при вводе текущего объявления
            return HttpResponseRedirect(reverse('comments', kwargs={'product_id': fb.cleaned_data['product'].pk}))
        else:
            # Данные не корректны
            context = {'form': fb}
            return render(request, 'main/addcomments.html', context)
    else:
        # Обработка get-запроса – отображение формы с полями ввода
        fb = FeedbackForm()
        context = {'form': fb}
        return render(request, 'main/addcomments.html', context)


def comments(request, product_id=0):
    feedbacks = Feedback.objects.filter(product__pk=product_id)
    products = feedbacks[0].product.title
    return render(request, 'main/comments.html', {'feedbacks': feedbacks, 'products': products})
