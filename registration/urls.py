from django.urls import path
from .views import SignUpView, ProfileUpdate, ProfileList

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('list/', ProfileList.as_view(), name='list'),
]