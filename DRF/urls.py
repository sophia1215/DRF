from django.contrib import admin
from django.urls import path, include

# For Django-REST-framework
from rest_framework.routers import DefaultRouter
# For Django REST Swagger
from rest_framework_swagger.views import get_swagger_view

from musics import views

# For Django REST Swagger
schema_view = get_swagger_view(title='API')


router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # For Django REST Swagger
    path('docs/', schema_view),
    
    # For Authentications
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
