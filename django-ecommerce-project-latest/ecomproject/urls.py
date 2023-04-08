"""
    This is the main urls file of the project
    Contains the main paths to the urls
    Coded and maintained by Jotham Prince
    Eshopper ecommerce web application
"""

# the necessary imports
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ecomapp import views
from ecomapp.views import *
# api app routes and authentications
from rest_framework.authtoken.views import obtain_auth_token
# for the notifications in the applications
import notifications.urls

# the main paths of the project
urlpatterns = [
    # default routes
    path('admin/', admin.site.urls),
    path("", include("ecomapp.urls")),
        # the notifications routes
    path('inbox/notifications', include(notifications.urls, namespace='notifications')),
]

# the path to the static files and the media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# customization to the django admin site
admin.site.site_header = "Eshopper"
admin.site.site_title = "Eshopper Admin Portal"
admin.site.index_title = "Welcome to Eshopper Admin Portal"
