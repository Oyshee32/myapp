from rest_framework import serializers

class CodeRunSerializer(serializers.Serializer):
    value = serializers.CharField(max_length=255)