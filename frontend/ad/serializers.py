from rest_framework import serializers

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)