from Stadium.models import Stadium
from User.models import User
from django.db import models


class Booking(models.Model):
    status_choice = (
        (1, 'pending'),
        (2, 'confirmed'),
        (3, 'completed'),
        (4, 'cancelled')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.SmallIntegerField(choices=status_choice, null=False, blank=False, default=1)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "%s - %s" % (self.user, self.stadium)
