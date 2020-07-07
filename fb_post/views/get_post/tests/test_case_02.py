"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from freezegun import freeze_time
from fb_post.models.factories import (
    PostFactory, CommentFactory, ReplyFactory,
    PostReactionFactory, CommentReactionFactory
    )
REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1"},
        "query_params": {},
        "header_params": {},
         "securities": {
            "oauth": {
                "tokenUrl": "http://auth.ibtspl.com/oauth2/",
                "flow": "password",
                "scopes": ["read"],
                "type": "oauth2"
            }
        },
        "body": REQUEST_BODY,
    },
}


class TestCase02GetPostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02GetPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.pop_data()

    @freeze_time("2000-10-10")
    def pop_data(self):
        post_obj = PostFactory()
        comment_objs = CommentFactory.create_batch(size=3, post=post_obj)

        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[0])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[1])

        PostReactionFactory.create_batch(size=10, post=post_obj)
        CommentReactionFactory.create_batch(size=5, comment=comment_objs[0])
        CommentReactionFactory.create_batch(size=5, comment=comment_objs[1])

    def test_case(self):
        response = self.default_test_case()

        import json
        response_content = json.loads(response.content)
        self.assert_match_snapshot(name="get_post_details_dict",
                                   value=response_content)

        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.