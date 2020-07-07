from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from fb_post_v2.models import *
from fb_post_v2.models.factories import *



class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )
        UserFactory.reset_sequence()
        PostFactory.reset_sequence()
