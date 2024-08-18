from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('download-cv/<int:user_id>/', views.download_cv, name='download_cv'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)