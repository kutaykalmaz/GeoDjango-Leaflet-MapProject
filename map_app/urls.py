from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('marked_data/', marked_datasets, name='marked_datasets'),
    path('yer_ekle/', kayit_ekle, name='kayit_ekle'),
    path('kayitlar/', kayitlar, name='kayitlar'),
    path('kayitlar/duzenle/<int:id>',kayitguncelle, name = 'kayitduzenle'),
    path('kayitlar/sil/<int:id>',kayitsil, name = 'kayitsil'),
]
