from django.urls import  re_path
from products import views

urlpatterns = [
    re_path(r'^api/Product(?:/(?P<id>[0-9]+))?', views.products, name='product_crud'),
]
