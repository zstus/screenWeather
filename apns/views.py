from django.shortcuts import render

# Create your views here.
# this is test for git.
# to Server!! go go!

from apns2.client import APNsClient
from apns2.payload import Payload

def send_notification(token_hex, message):
    try:
        client = APNsClient('path/to/cert.pem', use_sandbox=True, use_alternative_port=False)
        payload = Payload(alert=message, sound="default", badge=1)
        response = client.send_notification(token_hex, payload, 'bundle.identifier')
        print(f"Notification sent successfully: {response}")
    except Exception as e:
        print(f"Failed to send notification: {e}")


