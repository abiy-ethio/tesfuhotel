from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.core.urlresolvers import reverse


class Booking(models.Model):
	Name = models.CharField(max_length=200)
	checkin = models.DateTimeField(default=timezone.now())
	checkout = models.DateTimeField(default=timezone.now() )
	email = models.EmailField()
	Room = models.IntegerField(default=0)


	Standared = 'Standared'
	Twin = 'Twin'
	Deluxe = 'Deluxe'
	Suit = 'Suit'
	Room_Type = (
		(Standared, 'Standared'),
		(Twin, 'Twin'),
		(Deluxe, 'Deluxe'),
		(Suit, 'Suit'),
	)
	Room_Types = models.CharField(
		max_length=200,
		choices=Room_Type,
		default=Standared,
	)

	def get_absolute_url(self):
		return reverse('bookingsdetail', kwargs={'pk': self.pk})



