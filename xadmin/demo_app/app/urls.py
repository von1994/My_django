from django.conf.urls import url

from app import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^overview$',views.overview, name='overview'),
    url(r'^batch_config$',views.configure, name='configure'),
    url(r'^sendemail$', views.sendemail, name='sendemail'),
    url(r'^ipinfo$', views.ipinfo, name='ipinfo'),
    url(r'^batch_config/step1.html$', views.step1, name='step1'),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
