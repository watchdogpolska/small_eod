"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'small_eod.dashboard.CustomIndexDashboard'
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from github_revision.utils import get_backend, get_url

from grappelli.dashboard import modules, Dashboard
from django.apps import apps as django_apps

version = get_backend()()

SYSTEM_APP = ("django.contrib.*", "allauth.*")


class CustomAppList(modules.AppList):
    # Keep it there until
    # merge following pull request
    # https://github.com/sehmaschine/django-grappelli/pull/867
    def init_with_context(self, context):
        if self._initialized:
            return
        items = self._visible_models(context["request"])
        apps = {}
        for model, perms in items:
            app_label = model._meta.app_label
            if app_label not in apps:
                apps[app_label] = {
                    "name": django_apps.get_app_config(app_label).verbose_name,
                    "title": capfirst(app_label.title()),
                    "url": self._get_admin_app_list_url(model, context),
                    "models": [],
                }
            model_dict = {}
            model_dict["title"] = capfirst(model._meta.verbose_name_plural)
            if perms["change"] or perms["view"]:
                model_dict["admin_url"] = self._get_admin_change_url(model, context)
            if perms["add"]:
                model_dict["add_url"] = self._get_admin_add_url(model, context)
            apps[app_label]["models"].append(model_dict)

        apps_sorted = list(apps.keys())
        apps_sorted.sort()
        for app in apps_sorted:
            # sort model list alphabetically
            apps[app]["models"].sort(key=lambda i: i["title"])
            self.children.append(apps[app])
        self._initialized = True


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        # append a group for "Administration" & "Applications"
        self.children.append(
            CustomAppList(
                _("System"),
                column=1,
                css_classes=("grp-closed",),
                models=SYSTEM_APP,
            )
        )
        self.children.append(
            CustomAppList(
                _("Application"),
                column=1,
                # css_classes=('collapse closed',),
                exclude=SYSTEM_APP,
            )
        )

        # append another link list module for "support".
        self.children.append(
            modules.LinkList(
                _("Support"),
                column=2,
                children=[
                    {
                        "title": "GitHub - {}".format(version),
                        "url": get_url(version),
                        "external": False,
                    },
                ],
            )
        )

        # append a recent actions module
        self.children.append(
            modules.RecentActions(
                _("Recent Actions"),
                limit=5,
                collapsible=False,
                column=3,
            )
        )
