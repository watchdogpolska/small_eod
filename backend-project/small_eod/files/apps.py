from django.apps import AppConfig

from config.minio_app import minio_app


class FilesConfig(AppConfig):
    name = "small_eod.files"

    def ready(self):
        if not minio_app.bucket_exists('files'):
            minio_app.make_bucket('files')
