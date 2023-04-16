from django.urls import path

from . import views

urlpatterns = [
    path('stable_diffusion', views.generate_image_from_stable_diffusion, name='stable_diffusion'),
    path('midjourney', views.generate_image_from_midjourney, name='midjourney'),
    path('DALLE', views.generate_image_from_DALLE, name='DALLE')
]