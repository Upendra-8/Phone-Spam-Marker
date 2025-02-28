from api.models import SpamMark, Contact
from django.db.models import Count


class SpamService:
    @staticmethod
    def mark_as_spam(phone_number, user):
        # Check if the phone number is already marked as spam
        spam_mark, created = SpamMark.objects.get_or_create(phone_number=phone_number)
        
        if user not in spam_mark.marked_by.all():
            spam_mark.marked_by.add(user)
        
            # Update the spam count in the Contact table
            try:
                contact = Contact.objects.get(phone_number=phone_number)
                contact.spam_count += 1  # Increment the spam count
                contact.save()  # Save the updated contact
            except Contact.DoesNotExist:
                # Optionally handle the case where contact does not exist
                pass
        
        return spam_mark
    
    def get_spam_statistics():
        # Get the contacts and annotate them with the count of spam marks for their phone number
        spam_statistics = Contact.objects.annotate(
            num_spam_marks=Count('spammark__marked_by', distinct=True)  # Count the related SpamMark instances for each contact
        ).values(
            'phone_number', 'name', 'spam_count'
        ).order_by('-num_spam_marks')

        return spam_statistics