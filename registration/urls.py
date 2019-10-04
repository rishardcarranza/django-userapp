from django.urls import path
from .views import SignUpView, ProfileUpdate, ProfileList, ProfileDelete

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/<slug:username>/', ProfileUpdate.as_view(), name='profile'),
    path('list/', ProfileList.as_view(), name='list'),
    path('delete/<int:pk>/', ProfileDelete.as_view(), name='delete'),
]