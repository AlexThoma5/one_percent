from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('test/', views.test_view, name='categories-test'),
]
