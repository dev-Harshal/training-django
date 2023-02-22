from rest_framework import serializers
from messenger.models import UserMessages,Users




class UserMessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.first_name',read_only=True)
    class Meta:
        model = UserMessages
        fields = '__all__'
    
          