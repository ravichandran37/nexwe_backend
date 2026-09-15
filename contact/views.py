from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactMessageSerializer
import traceback

class ContactMessageCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact_msg = serializer.save()
            
            # Send Email Notification
            try:
                subject = f"New Contact Request: {contact_msg.subject}"
                body = f"Name: {contact_msg.name}\nEmail: {contact_msg.email}\n\nMessage:\n{contact_msg.message}"
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL], # Send to yourself
                    fail_silently=True, # Prevent crashes if SMTP isn't configured yet
                )
            except Exception as e:
                print(f"Failed to send email: {e}")
                traceback.print_exc()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
