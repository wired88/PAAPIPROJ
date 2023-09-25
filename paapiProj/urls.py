from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from api.viewsets import ContactAPIView

router = routers.DefaultRouter(trailing_slash=False)  # training_slash remove the end /
router.register(r'contact', ContactAPIView.as_view(), basename="contact")

# router.register(r'master', views.MasterViewSet)

# This wrapper turns your list into a regex URL matcher
react_views_regex = r'\/|\b'.join([
    # List all your react routes here
    '/',
    '/contact',
    '/offers',
    '/imprint',

]) + r'\/'

from django.views.generic import TemplateView

urlpatterns = [
  path('admin/', admin.site.urls),
  path("", TemplateView.as_view(template_name="index.html")),
  path("api/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
