from celery import shared_task
from bucket import bucket

#TODO: Can be Async?
def all_bucket_objects_task():
    result = bucket.get_objects()
    return result


@shared_task
def delete_object_task(key):
    bucket.delete_object(key)

@shared_task
def download_object_task(key):
    bucket.download_object(key)
