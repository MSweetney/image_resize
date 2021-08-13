from django.urls import path
from .views import homepage_view, upload_view, resize_view

urlpatterns = [
    path('', homepage_view, name='home'),
    path('upload/', upload_view, name='upload'),
    path('resize/<int:img_id>/', resize_view, name='resize'),
    ]
