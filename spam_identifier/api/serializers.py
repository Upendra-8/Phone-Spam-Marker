from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email']

class ContactSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'spam_likelihood']

    def get_spam_likelihood(self, obj):
        spam_marks = obj.spam_count
        return f"{spam_marks} spam marks"
