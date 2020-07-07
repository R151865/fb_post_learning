"""
Delete Post Given Valid UserId, PostId.
"""

from fb_post_clean_arch.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post_clean_arch.models.factories import PostFactory, UserFactory
from fb_post_clean_arch.models import Post, User

REQUEST_BODY = """
{}
"""
post_id = 1

TEST_CASE = {
    "request": {
        "path_params": {"post_id": post_id},
        "query_params": {},
        "header_params": {},
        "securities": {
            "oauth": {
                "tokenUrl": "http://auth.ibtspl.com/oauth2/",
                "flow": "password",
                "scopes": ["superuser"],
                "type": "oauth2"
            }
        },
        "body": REQUEST_BODY,
    },
}


class TestCase04DeletePostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase04DeletePostAPITestCase, self).setupUser(
            username=username, password=password
        )
        user_obj = User.objects.filter(username=username)[0]
        a = PostFactory(user=user_obj)
        print("post id", a.id)
        print("user id", a.user.id)

    def test_case(self):
        self.default_test_case()