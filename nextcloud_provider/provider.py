from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class NextcloudAccount(ProviderAccount):
    def to_str(self):
        return self.account.extra_data.get('name',
                                           super(NextcloudAccount, self).to_str())

    def get_avatar_url(self):
        return None


class NextcloudProvider(OAuth2Provider):
    id = 'nextcloud'
    name = 'Nextcloud'
    account_class = NextcloudAccount

    def get_default_scope(self):
        return ['profile', ]

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        # Hackish way of splitting the fullname.
        # Asumes no middlenames.
        name = data.get('display-name', '')
        first_name, last_name = name, ''
        if name and ' ' in name:
            first_name, last_name = name.split(' ', 1)

        special_groups = self.get_settings().get('GROUPS', {})
        is_superuser = 'admin' in special_groups and special_groups['admin'] in data['groups']
        is_staff = 'staff' in special_groups and special_groups['staff'] in data['groups']

        return dict(email=data['email'],
                    last_name=last_name,
                    first_name=first_name,
                    is_staff=is_staff,
                    is_superuser=is_superuser)


provider_classes = [NextcloudProvider]
