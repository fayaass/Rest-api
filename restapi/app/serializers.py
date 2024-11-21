from rest_framework import serializers

class user_serializers(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField ()