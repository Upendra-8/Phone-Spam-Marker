from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)


class SpamMark(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    marked_by = models.ManyToManyField(User, related_name="marked_spam")
    
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    spam_count = models.PositiveIntegerField(default=0)
    
    # Ensure there is a relationship from SpamMark to Contact
    spammark = models.ForeignKey(SpamMark, on_delete=models.CASCADE, related_name='contact_spammark', null=True, blank=True)


