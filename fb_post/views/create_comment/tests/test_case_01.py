"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string",
    "post_id": 1
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01CreateCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateCommentAPITestCase, self).setupUser(
            username=username, password=password
        )

        #PostFactory()
    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

    #   import json

    #     response_content = json.loads(response.content)

    #     comment_id = response_content['comment_id']

    #     comment = Comment.objects.get(id=comment_id)

    #     self.assert_match_snapshot(
    #         name='user_id',
    #         value=comment.user.id
    #     )

    #     self.assert_match_snapshot(
    #         name='post_id',
    #         value=comment.post.id
    #     )
    #     self.assert_match_snapshot(
    #         name='comment_text',
    #         value=comment.comment_text
    #     )