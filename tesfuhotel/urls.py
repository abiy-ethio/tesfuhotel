from django.conf.urls import include, url
from django.contrib import admin
from booking import views
from booking.views import CreateBooking, UpdateBooking, BookingDetail


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Home/$', views.Home.as_view(), name='Home'),
    url(r'^health/$', views.health, name='health'),
    url(r'^meeting/$', views.meeting, name='meeting'),
    url(r'^reserve/$', views.reserve, name='reserve'),
    url(r'^bookings/(?P<id>\d+)/', views.booking_detail, name='bookings_detail'),
    url(r'^bookings/(?P<pk>[0-9]+)/$', views.BookingDetail.as_view(), name='bookingsdetail'),

    url(r'^bookings/create/$', views.CreateBooking.as_view(), name='create_booking'),
    url(r'^bookings/update/(?P<pk>[0-9]+)/$', views.UpdateBooking.as_view(), name='update_booking'),
    url(r'^admin/', include(admin.site.urls)),
              ]