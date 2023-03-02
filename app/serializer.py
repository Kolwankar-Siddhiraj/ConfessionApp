from .models import *
from rest_framework.serializers import ModelSerializer


class ConfessionSerializer(ModelSerializer):

    class Meta:
        model = Confession
        fields = '__all__'


