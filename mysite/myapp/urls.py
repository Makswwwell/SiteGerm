from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs/', views.blog_list, name='blog_list'),
    path('menu/', views.menu, name='menu'),
    path('party_services/', views.party_service_list, name='party_service_list'),
    path('gallery/', views.dish_gallery, name='dish_gallery'),
    path('impressum/', views.impressum_view, name='impressum_view'),
    path('privacy_policy/', views.privacy_policy_view, name='privacy_policy_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
