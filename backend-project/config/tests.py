from django.test.runner import DiscoverRunner


class CustomDiscoverRunner(DiscoverRunner):
    def __init__(self, **kwargs):
        kwargs["pattern"] = "*_test.py"
        super().__init__(**kwargs)
