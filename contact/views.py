import os
import json
import logging
import threading
import urllib.request
import urllib.error
from django.conf import settings
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactMessageSerializer

logger = logging.getLogger(__name__)


def send_via_web3forms(access_key, name, email, subject, message):
    """Send notification email via Web3Forms HTTPS API (Port 443 - works on Render Free)."""
    url = "https://api.web3forms.com/submit"
    payload = {
        "access_key": access_key,
        "from_name": f"Nexwe Booking - {name}",
        "name": name,
        "email": email,
        "subject": f"[Nexwe Inquiry] {subject}",
        "message": f"Client Name: {name}\nClient Email: {email}\n\nDetails:\n{message}",
        "replyto": email,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "NexweBackend/1.0",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))
        if res_data.get("success"):
            logger.info(f"Web3Forms notification sent successfully to nexwesolutions@gmail.com for {email}")
            return True
        else:
            logger.error(f"Web3Forms error response: {res_data}")
            return False

def send_via_resend(api_key, name, email, subject, message):
    """Send notification email via Resend HTTPS API (Port 443 - works on Render Free)."""
    url = "https://api.resend.com/emails"
    to_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'nexwesolutions@gmail.com')
    payload = {
        "from": "Nexwe Portfolio <onboarding@resend.dev>",
        "to": [to_email],
        "reply_to": email,
        "subject": f"New Contact Request: {subject}",
        "text": f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "NexweBackend/1.0",
        },
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        logger.info(f"Resend notification sent successfully to {to_email} for {email}")
        return True

def send_via_smtp(name, email, subject, message):
    """Fallback to standard Django SMTP (works locally, blocked on Render Free tier)."""
    password = getattr(settings, 'EMAIL_HOST_PASSWORD', '')
    if not password:
        logger.warning("No email provider configured (WEB3FORMS_ACCESS_KEY, RESEND_API_KEY, or EMAIL_HOST_PASSWORD). Message saved in database only.")
        return False

    email_subject = f"New Contact Request: {subject}"
    email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    send_mail(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
    logger.info(f"Notification email sent via SMTP for contact message from {email}")
    return True

def send_contact_email_async(name, email, subject, message):
    """Dispatches contact notification asynchronously via Web3Forms, Resend, or SMTP."""
    web3forms_key = os.environ.get('WEB3FORMS_ACCESS_KEY') or getattr(settings, 'WEB3FORMS_ACCESS_KEY', '')
    resend_key = os.environ.get('RESEND_API_KEY') or getattr(settings, 'RESEND_API_KEY', '')

    # 1. Primary Cloud Option: Web3Forms (HTTPS port 443 - 100% compatible with Render Free tier)
    if web3forms_key:
        try:
            if send_via_web3forms(web3forms_key, name, email, subject, message):
                return
        except Exception as e:
            logger.error(f"Failed to send email via Web3Forms: {e}")

    # 2. Secondary Cloud Option: Resend (HTTPS port 443)
    if resend_key:
        try:
            if send_via_resend(resend_key, name, email, subject, message):
                return
        except Exception as e:
            logger.error(f"Failed to send email via Resend: {e}")

    # 3. Fallback: SMTP (Runs locally, but fails on Render Free tier due to port 587 block)
    try:
        send_via_smtp(name, email, subject, message)
    except Exception as e:
        logger.error(
            f"SMTP email sending failed: {e}. Note: If running on Render Free tier, "
            "Render blocks SMTP ports 25, 465, and 587. Please configure WEB3FORMS_ACCESS_KEY "
            "in your Render Environment tab to send via HTTPS."
        )

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

