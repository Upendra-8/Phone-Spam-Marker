from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('mark-spam/', MarkSpamView.as_view(), name='mark-spam'),
    path('search/', SearchView.as_view(), name='search'),
    path('contacts/<int:contact_id>/', ContactDetailView.as_view(), name='contact-detail'),
    path('spam-statistics/', SpamStatisticsView.as_view(), name='spam-statistics'),
]
