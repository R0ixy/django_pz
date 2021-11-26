from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/', views.index, name='index'),
    # path('<args>', views.index_with_par, name='index'),
    path('<dark>', views.changemode),

    path('about/', views.about, name='about'),
    # path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('comments/', views.add_and_save),
    path('comments/<int:product_id>', views.comments, name='comments')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
