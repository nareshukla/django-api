# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, home  # Import both PersonViewSet and home view

# Set up the router for the CRUD API
router = DefaultRouter()
router.register(r'persons', PersonViewSet)

# URL patterns
urlpatterns = [
    path('', home, name='home'),  # Map the root URL to the home view
    path('', include(router.urls)),  # Include the CRUD API routes
]