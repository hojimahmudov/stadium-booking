from django.urls import path, include
from api.v1.user import urls as user_urls
from api.v1.stadium import urls as stadium_urls
from api.v1.booking import urls as booking_urls

urlpatterns = [
    path('user/', include(user_urls)),
    path('stadium/', include(stadium_urls)),
    path('booking/', include(booking_urls))
]
