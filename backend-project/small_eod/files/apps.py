from minio import Minio, PostPolicy
from django.conf import settings
from django.utils.timezone import timedelta
from django.utils import timezone
from django.apps import AppConfig


class MinioApp(Minio):
    def presigned_post_form_data(self, bucket, object_path):
        post_policy = PostPolicy()
        post_policy.set_bucket_name(bucket)
        post_policy.set_key(object_path)
        post_policy.set_expires(timezone.now() + timedelta(days=1))

        return self.presigned_post_policy(post_policy)


minio_app = MinioApp(
    settings.MINIO_URL.replace("http://", "").replace("https://", ""),
    settings.MINIO_ACCESS_KEY,
    settings.MINIO_SECRET_KEY,
    secure="https" in settings.MINIO_URL,
)


class FilesConfig(AppConfig):
    name = "small_eod.files"

    def ready(self):
        if not minio_app.bucket_exists(settings.MINIO_BUCKET):
            minio_app.make_bucket(settings.MINIO_BUCKET)
