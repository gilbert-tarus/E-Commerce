from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.urls import path, include
# from .views import index as index2
urlpatterns = [
    path('', include('core.urls')),#old and updated part
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Verifying Sentry Installation
# You can easily verify your Sentry installation by creating a route that triggers an error:

# from django.urls import path

# def trigger_error(request):
#     division_by_zero = 1 / 0

# urlpatterns = [
#     path('sentry-debug/', trigger_error),
#     # ...
# ]