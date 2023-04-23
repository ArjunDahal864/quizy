from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Quizzy API",
      default_version='v1',
      description="API FOR COMPLETE LMS",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@arjun.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path("course/",include("course.urls")),
    path("quiz/",include("mcq.urls")),
    path("profile/", include("user_profile.urls")),
    path("notes/", include("notes.urls")),
    
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
