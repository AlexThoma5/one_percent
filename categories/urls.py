from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:slug>/edit_log/<int:log_id>/', views.log_edit, name='log_edit'),
    path('<slug:slug>/delete_log/<int:log_id>/', views.log_delete, name='log_delete'),
]
