from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
schema_view = get_schema_view(
   openapi.Info(
      title="Project Management API",
      default_version='v1',
      description="API documentation for User Management system",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
api_info = openapi.Info(
    title="Project_Management API",
    default_version="v1",
    description="Core API endpoints for Project_Management",
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('login', include('login.urls')),
        path('users/', include('users.urls')),
        path('roles/', include('roles.urls')),
        path('permissions/', include('permissions.urls')),
        path('projects/', include('projects.urls')),
        path('project_members/', include('project_members.urls')),
    ])),

    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

