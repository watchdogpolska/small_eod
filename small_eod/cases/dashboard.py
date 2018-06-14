"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'small_eod.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from github_revision.utils import get_backend, get_url

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

version = get_backend()()

SYSTEM_APP = ('django.contrib.*', 'allauth.*')

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        # append a group for "Administration" & "Applications"
        self.children.append(modules.AppList(
            _('System'),
            column=1,
            css_classes=('grp-closed',),
            models=SYSTEM_APP,
        ))
        self.children.append(
            modules.AppList(
                _('Application'),
                column=1,
                # css_classes=('collapse closed',),
                exclude=SYSTEM_APP,
            )
        )

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Support'),
            column=2,
            children=[
                {
                    'title': "GitHub - {}".format(version),
                    'url': get_url(version),
                    'external': False,
                },
            ]
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=3,
        ))
