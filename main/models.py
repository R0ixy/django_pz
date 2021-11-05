from django.db import models
from django.forms import ModelForm
from django.forms.widgets import TextInput, Select, Textarea


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.CharField(max_length=255, verbose_name='Эл. почта')
    message = models.TextField(verbose_name='Сообщение', null=True)
    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message', 'product')
        labels = {'name': 'Имя', 'email': 'Эл. Почта', 'message': 'сообщение', 'product': 'товар'}
        widgets = {'name': TextInput(), 'message': Textarea(), 'product': Select()}
