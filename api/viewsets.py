from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *

class Index(TemplateView):
    template_name = "index.html"



class ContactAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) # check if valid. if not, custom made error will be displayed(see serializer class)
        self.perform_create(serializer)   # create isntance in db
        return JsonResponse({"successUrl": "http://localhost:5173/", "status": status.HTTP_201_CREATED})

"""
data = request.data
        first_name = data.first_name
        last_name = data.last_name
        email = data.email
        options = data.options
        message = data.message
        contact_data = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            options=options,
            message=message
        )
        contact_data.save()
        """