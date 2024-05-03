from rest_framework import serializers

from Stadium.models import StadiumImage, Stadium


class StadiumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadiumImage
        fields = ['image']


class StadiumSerializer(serializers.ModelSerializer):
    images = StadiumImageSerializer(many=True, read_only=True)

    class Meta:
        model = Stadium
        fields = ['id', 'images', 'address', 'phone', 'price_per_hour', 'description', 'lat', 'long']
