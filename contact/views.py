from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactMessageSerializer
import threading
import logging

logger = logging.getLogger(__name__)

def send_contact_email_async(name, email, subject, message):
    password = getattr(settings, 'EMAIL_HOST_PASSWORD', '')
    if not password:
        logger.info("EMAIL_HOST_PASSWORD is not set. Saved to database only.")
        return
    try:
        email_subject = f"New Contact Request: {subject}"
        email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
        logger.info(f"Notification email sent for contact message from {email}")
    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")

class ContactMessageCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            contact_msg = serializer.save()
            
            # Send Email in background thread so HTTP response returns instantly
            threading.Thread(
                target=send_contact_email_async,
                args=(contact_msg.name, contact_msg.email, contact_msg.subject, contact_msg.message),
                daemon=True
            ).start()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

