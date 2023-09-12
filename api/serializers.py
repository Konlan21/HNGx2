from rest_framework import serializers  
from api.models import Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']

    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Only string values are allowed.")
        return value