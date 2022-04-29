from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Response


@receiver(post_save, sender=Response)
def reply_added(sender, instance, created, **kwargs):
    if created:
        msg = EmailMultiAlternatives(
            subject='У вас новое сообщение c bulletin_board',
            from_email='D9newspaper@yandex.ru',
            to=[f'{instance.ads.author.user.email}']
        )

        html_content = render_to_string(
            'email/response_added_letter.html',
            {'response': instance})

        msg.attach_alternative(html_content, "text/html")
        msg.send()

    else:
        user = instance.user
        subject = f"Ваш отклик был одобрен и размещен на доске объявлений"
        message = f'Ваш комментарий: "{instance.text_response}" к объявлению "{instance.ads}" был одобрен и размещен на форуме.'
        user.email_user(subject, message)
