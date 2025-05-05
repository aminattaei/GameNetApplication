from rest_framework.serializers import ModelSerializer

from .models import Game


class GameModelSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"
