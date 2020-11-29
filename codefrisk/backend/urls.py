from django.urls import include, path
from rest_framework import routers
from backend import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users2', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
    path('users/',views.create_user),
    path('add_file/',views.DataUpload.post),
    path('view_files/',views.DataUpload.view_files)
]