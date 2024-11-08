# myproject/urls.py
from django.contrib import admin
from django.urls import path, include  # Import the include function
from myapp.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Include the URLs from your app
    path('', home),  # Add the home view at the root URL
]
