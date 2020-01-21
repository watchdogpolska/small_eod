from minio import Minio, PostPolicy
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


__all__ = (
    'minio_app',
)


class MinioApp(Minio):
    def presigned_post_form_data(self, bucket, object_path):
        post_policy = PostPolicy()
        post_policy.set_bucket_name(bucket)
        post_policy.set_key(object_path)
        post_policy.set_expires(timezone.now() + timedelta(days=1))

        return self.presigned_post_policy(post_policy)


minio_app = MinioApp(
    settings.MINIO_URL.replace('http://', ''),
    settings.MINIO_ACCESS_KEY,
    settings.MINIO_SECRET_KEY,
    secure='https' in settings.MINIO_URL,
)
