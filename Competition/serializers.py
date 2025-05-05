from rest_framework.serializers import ModelSerializer
from .models import Competition


class CompetitionsSerializer(ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"
