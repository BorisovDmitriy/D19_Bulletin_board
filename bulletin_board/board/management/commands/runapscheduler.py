import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from datetime import datetime, timedelta
from django.utils import timezone
from board.models import Ad
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def weekly_mail():
    ads = Ad.objects.filter(create_time__gte=datetime.now(tz=timezone.utc) - timedelta(days=7))
    if ads.exists():
        recipients = [user.email for user in User.objects.all()]
        msg = EmailMultiAlternatives(
            subject=f'Все объявления за прошедшую неделю на bulletin_board',
            from_email='D9newspaper@yandex.ru',
            to=recipients
        )

        html_content = render_to_string(
            'weekly_mail.html',
            {'ads': ads})

        msg.attach_alternative(html_content, "text/html")

        msg.send()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            weekly_mail,
            trigger=CronTrigger(day_of_week="mon", hour="15", minute="00"),
            id="weekly_mail",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'weekly_mail'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(minute="*/5"),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'delete_old_job_executions'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
