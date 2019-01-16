from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Notifications, Profile


def send_priority_email(name, receiver, title, message, author, neighbourhood):
    #Creating message subject and sender
    subject = "Welcome Email"
    sender = 'clintonsoftwares@gmail.com'

    text_content = render_to_string('email/message.txt', {"name": name})
    html_content = render_to_string('email/messaqe.html', {"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
