from api.models import Contact, User

class UserService:
    @staticmethod
    def register_user(data):
        if User.objects.filter(phone_number=data['phone_number']).exists():
            raise ValueError("Phone number already registered.")
        
        # Create the user
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            phone_number=data['phone_number'],
            email=data.get('email', '')
        )
        
        # Create the corresponding contact
        Contact.objects.create(
            user=user,  # Associate the contact with the user
            name=data['username'],  # Or use a separate name field if provided
            phone_number=data['phone_number']
        )
        
        return user
