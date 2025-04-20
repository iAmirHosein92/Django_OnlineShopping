from __future__ import absolute_import, unicode_literals
from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshopping.settings')

celery_app = Celery('onlineshopping')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = 'amqp://myuser:mypassword@rabbitmq:5672//'
celery_app.conf.result_backend = 'rpc://'
celery_app.conf.task_serializer = 'json'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['json', 'pickle']
celery_app.conf.result_expires = timedelta(days=1)
celery_app.conf.task_always_eager = False
celery_app.conf.worker_prefetch_multiplier = 4
celery_app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'home.tasks.add',
        'schedule': 30.0,
        'args': (10, 20)
    },
}
