from django.urls import path
from order import views
urlpatterns = [
    path('checkout/', views.checkout,  name='結帳頁面')
]