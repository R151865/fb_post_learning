"""
# TODO: React To Comment, Handling InvalidCommentException
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "reaction_type": "WOW"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01ReactToCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01ReactToCommentAPITestCase, self).setupUser(
            username=username, password=password
        )

    def test_case(self):
        self.default_test_case()
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.