from django.conf.urls import url
from django.contrib import admin
from stock import views as stock_views  # new

urlpatterns = [
    url(r'^$', stock_views.home, name="home"),  # new
    url(r'^admin/', admin.site.urls),
]