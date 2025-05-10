from django.urls import path
from .views import *

urlpatterns = [
    path('', NobelListView.as_view(), name='nobel-list'),
    path('create/', NobelCreateView.as_view(), name='nobel-create'),
    path('<int:pk>/', NobelDetailView.as_view(), name='nobel-detail'),
    path('<int:pk>/edit/', NobelUpdateView.as_view(), name='nobel-update'),
    path('<int:pk>/delete/', NobelDeleteView.as_view(), name='nobel-delete'),
]