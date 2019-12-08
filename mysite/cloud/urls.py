from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


app_name = 'cloud'

urlpatterns = [
    path('', views.main,name='main'),
    path('get/',views.check_get,name='search_get'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
