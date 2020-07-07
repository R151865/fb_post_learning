"""
# TODO: Get Post Reactions
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from freezegun import freeze_time
from fb_post.models.factories import PostFactory, PostReactionFactory

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


class TestCase02GetReactionsToPostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02GetReactionsToPostAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.pop_data()

    @freeze_time("2000-10-10")
    def pop_data(self):
        post_obj = PostFactory()
        PostReactionFactory.create_batch(size=5, post=post_obj)
        
    def test_case(self):
        response = self.default_test_case() 

        import json
        response_content = json.loads(response.content)
        self.assert_match_snapshot(name="post_reactions_details",
                                   value=response_content)

