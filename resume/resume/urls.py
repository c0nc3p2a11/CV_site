from django.contrib import admin
from django.urls import path
from main import views as main_views
from contact_form import views as cf_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', cf_views.form, name='form'),
    path('', main_views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
