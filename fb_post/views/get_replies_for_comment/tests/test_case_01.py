"""
# TODO: Handling Comment Id Exception For Get Replies For Comment
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.utils.custom_test_utils_2 import CustomTestUtils

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1234"},
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


class TestCase01GetRepliesForCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetRepliesForCommentAPITestCase, self).setupUser(
            username=username, password=password
        )

    def test_case(self):
        self.default_test_case()