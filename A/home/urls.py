from django.urls import path
from . import views
from .views import ProductDetailView

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]