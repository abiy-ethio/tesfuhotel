from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . models import Booking
from django.views.generic import DetailView, CreateView, UpdateView


def index(request):
	bookings = Booking.objects.all()
	return render(request, 'booking/index.html',{
		'bookings' : bookings
	})


def health(request):
	booking = Booking.objects.all()
	return render(request, 'booking/health.html', {
		'booking': booking
	})

def meeting(request):
	booking = Booking.objects.all()
	return render(request, 'booking/meeting.html', {
		'booking': booking
	})
class Home(DetailView):
	model = Booking
	template_name = "booking/html"


class BookingDetail(DetailView):
	model = Booking
	template_name = "booking/item_detail.html"


class CreateBooking(CreateView):
	model = Booking
	fields = ['Name', 'checkin', 'checkout', 'email', 'Room_Types']


class UpdateBooking(UpdateView):
	model = Booking
	fields = ['Name', 'checkin', 'checkout', 'email', 'Room_Types']


def booking_detail(request, id):
	booking = get_object_or_404(Booking, id=id)
	context = {
		'booking' :booking
	}
	return render(request, 'booking/item_detail.html', context)

def reserve(request):
	booking = Booking.objects.all()
	return render(request, 'booking/reserve.html', {
		'booking' : booking
	})



