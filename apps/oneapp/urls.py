from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logandreg),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^main$', views.main),
    url(r'^order_show/(?P<order_id>\d+)$', views.orderpage),
    url(r'^admin_products$', views.adminproducts),
    url(r'^edit_prod/(?P<prod_id>\d+)$', views.editproducts),
    url(r'^update_stat/(?P<order_id>\d+)$', views.updatestat),


]