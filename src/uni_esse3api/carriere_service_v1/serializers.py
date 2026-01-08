from rest_framework import serializers


class CarriereRequestSerializer(serializers.Serializer):
    cf = serializers.CharField(
        required=True, 
        min_length=16, 
        max_length=16,
        help_text="Il codice fiscale dello studente"
    )
