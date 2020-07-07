from django_swagger_utils.utils.test import CustomAPITestCase
from freezegun import freeze_time

from fb_post.models import *
from fb_post.models.factories import *


class CustomTestUtils(CustomAPITestCase):

    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )
        UserFactory.reset_sequence()
        PostFactory.reset_sequence()
        CommentFactory.reset_sequence()
        ReplyFactory.reset_sequence()
        PostReactionFactory.reset_sequence()
        CommentReactionFactory.reset_sequence()
    
