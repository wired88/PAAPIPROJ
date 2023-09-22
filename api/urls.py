from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.viewsets import ContactAPIView


app_name = "api"
urlpatterns = [
    path("contact/", ContactAPIView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



"""


from api.views import ContactAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contact.jsx', ContactAPIView)


"""