from spice import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.qr_redirect, name='spice_qr_redirect'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
