from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import generics, status

from Booking.models import Booking
from Stadium.models import Stadium, StadiumImage
from .serializers import StadiumSerializer, StadiumImageSerializer
from rest_framework import viewsets, permissions
from api.v1.permissions import IsAdminOrStadiumOwner
from math import radians, sin, cos, asin, sqrt


class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAdminOrStadiumOwner]

        return [i() for i in permission_classes]

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def haversine(self, lat1, long1, lat2, long2):
        lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
        dlong = long2 - long1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r

    def list(self, request, *args, **kwargs):
        start_time_str = request.query_params.get('start_time')
        end_time_str = request.query_params.get('end_time')
        lat = request.query_params.get('lat')
        long = request.query_params.get('long')

        if start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M')

            self.queryset = Stadium.objects.exclude(
                id__in=Booking.objects.filter(
                    Q(start_time__lte=end_time, end_time__gte=start_time) |
                    Q(start_time__gte=start_time, start_time__lte=end_time) |
                    Q(end_time__gte=start_time, end_time__lte=end_time),
                    status=2
                ).values_list('stadium_id', flat=True)
            )

        if lat and long:  # "long" to'g'ri nomlanishi
            user_location = (float(lat), float(long))
            for stadium in self.queryset:
                stadium_location = (stadium.lat, stadium.long)
                distance = self.haversine(*user_location, *stadium_location)
                setattr(stadium, 'distance', distance)

            self.queryset = sorted(self.queryset, key=lambda x: x.distance)

        return super().list(request, *args, **kwargs)
