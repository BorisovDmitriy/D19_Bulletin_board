from django.dispatch import Signal

from bulletin_board.settings import ALLOWED_HOSTS
from django.core.signing import Signer
from django.template.loader import render_to_string


user_registered = Signal(['instance'])


def user_registered_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatcher)


signer = Signer()


def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]

    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('accounts/email/activation_letter_subject.txt', context)
    body_text = render_to_string('accounts/email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)