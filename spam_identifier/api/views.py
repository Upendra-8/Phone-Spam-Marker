from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers import UserSerializer, ContactSerializer
from api.services.user_service import UserService
from api.services.contact_service import ContactService
from api.services.spam_service import SpamService
from rest_framework.authtoken.views import ObtainAuthToken


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        try:
            user = UserService.register_user(data)
            return Response(UserSerializer(user).data, status=201)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)


class LoginView(ObtainAuthToken):
    pass


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully.'}, status=200)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class MarkSpamView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required.'}, status=400)

        SpamService.mark_as_spam(phone_number, request.user)
        return Response({'message': 'Number marked as spam.'}, status=200)


class SearchView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        query = request.GET.get('query', '')

        # Use the unified search method for both name and phone number
        results = ContactService.search(query)

        # Serialize the results and return them in the response
        serializer = ContactSerializer(results, many=True)
        return Response(serializer.data, status=200)


class ContactDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, contact_id):
        contact = ContactService.get_contact_detail(contact_id)
        if not contact:
            return Response({'error': 'Contact not found.'}, status=404)

        # If the contact belongs to a registered user and the requester is in their contact list
        if contact.user and request.user in contact.user.contacts.all():
            serializer = ContactSerializer(contact, context={'show_email': True})
        else:
            serializer = ContactSerializer(contact, context={'show_email': False})

        return Response(serializer.data, status=200)


class SpamStatisticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        spam_data = SpamService.get_spam_statistics()
        return Response(spam_data, status=200)