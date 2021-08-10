from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_crate, name='view_crate'),
    path('add/<item_id>/', views.add_to_crate, name='add_to_crate'),
    path('modify/<item_id>/', views.modify_crate, name='modify_crate'),
    path('remove/<item_id>/', views.remove_from_crate, name='\
        remove_from_crate'),
    path('coupon_apply/', views.coupon_apply, name='coupon_apply'),
]
