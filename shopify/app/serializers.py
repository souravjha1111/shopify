from rest_framework import serializers
from .models import inventorymodel


class inventoryserializer(serializers.ModelSerializer):
    class Meta:
        model = inventorymodel
        fields = "__all__"