from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

#from xadmin.plugins import xversion
#xversion.register_models()

from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^app/', include('app.urls')),
]
