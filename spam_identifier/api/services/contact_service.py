from api.models import Contact
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class ContactService:
    @staticmethod
    def search(query):
        results = Contact.objects.filter(
            models.Q(name__icontains=query) | models.Q(phone_number__icontains=query)
        ).order_by('name')
        return results
    
     # Get a contact detail by ID or phone number
    @staticmethod
    def get_contact_detail(contact_id=None, phone_number=None):
        try:
            if contact_id:
                contact = Contact.objects.get(id=contact_id)
            elif phone_number:
                contact = Contact.objects.get(phone_number=phone_number)
            else:
                return None  # Return None if no identifier is provided
            return contact
        except ObjectDoesNotExist:
            return None  # Return None if contact is not found

