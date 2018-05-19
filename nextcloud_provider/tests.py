from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase

from .provider import NextcloudProvider


class NextcloudTests(OAuth2TestsMixin, TestCase):
    provider_id = NextcloudProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
            {
                "ocs": {
                    "data": {
                        "address": "",
                        "display-name": "adobrawy",
                        "email": "naczelnik@jawnosc.tk",
                        "enabled": "true",
                        "groups": [
                            "admin",
                            "zespol"
                        ],
                        "id": "adobrawy",
                        "language": "pl",
                        "phone": "",
                        "quota": {
                            "free": 66055610368,
                            "quota": -3,
                            "relative": 3.43,
                            "total": 68401725358,
                            "used": 2346114990
                        },
                        "twitter": "",
                        "website": ""
                    },
                    "meta": {
                        "message": "OK",
                        "status": "ok",
                        "statuscode": 200
                    }
                }
            }
         """)