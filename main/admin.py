from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ['category']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(Feedback, FeedbackAdmin)





# admin.site.register(CartProduct)
# admin.site.register(Cart)
# admin.site.register(Customer)