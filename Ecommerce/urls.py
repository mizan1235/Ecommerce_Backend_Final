from django.urls import path,include
from django.contrib import admin
import Ecommerce.views as views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import FilesViewSet

router = DefaultRouter()
router.register('files', FilesViewSet, basename='files')

urlpatterns = [
path('api/', include(router.urls)),
path('get_user_all',views.get_user_all,name='get_user_all'),
path('create_user',views.create_user,name='create_user'),
path('login_user',views.login_user,name='login_user'),
path('get_product_category',views.get_product_category,name='et_product_category'),
path('get_all_products',views.get_all_products,name='get_all_products'),
path('create_card',views.create_card,name='create_card'),
path('get_card',views.get_card,name='get_card'),
path('get_card_product',views.get_card_product,name='get_card_product'),
path('remove_card',views.remove_card,name='remove_card'),
path('create_order',views.create_order,name='create_order'),
path('get_order',views.get_order,name='get_order'),
path('get_user',views.get_user,name='get_user')

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)