from django.urls import path
from .views import ReservationsView, home
from .views import BookingListView
urlpatterns = [
    path('', home, name='home'),
    path('api/reservations/', ReservationsView.as_view(), name='reservations'),
    path('bookings/', BookingListView.as_view(), name='bookings'),
]
