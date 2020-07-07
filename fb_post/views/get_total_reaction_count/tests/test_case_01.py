"""
# TODO: Get Total Reaction Count
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.models.factories import (
    PostReactionFactory, CommentReactionFactory
)

REQUEST_BODY = """
{
    
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
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


class TestCase01GetTotalReactionCountAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetTotalReactionCountAPITestCase, self).setupUser(
            username=username, password=password
        )

        PostReactionFactory.create_batch(5)
        CommentReactionFactory.create_batch(5)

    def test_case(self):
        response = self.default_test_case()

        import json
        response_content = json.loads(response.content)
        print('*'*50)
        print(response_content)
        count = response_content["count"]
        

        self.assert_match_snapshot(name="total_reaction_count",
                                   value=count)
