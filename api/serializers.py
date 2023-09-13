from rest_framework import serializers  
from api.models import Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name']

    
    # def validate_name(self, value):
    #     if not value.isalpha():
    #         raise serializers.ValidationError("Only string values are allowed.")
    #     return value
    
    def validate_name(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("Only string values with spaces are allowed.")
        return value