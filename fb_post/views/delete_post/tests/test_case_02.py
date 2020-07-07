"""
# TODO: Delete Post, With Valid Details Delete Post
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
post_id = 1
REQUEST_BODY = """
{
}
"""


TEST_CASE = {
    "request": {
        "path_params": {"post_id": post_id},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02DeletePostAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02DeletePostAPITestCase, self).setupUser(
            username=username, password=password
        )

        from fb_post.models import User
        user_obj = User.objects.get(id=self.foo_user.id)

        from fb_post.models.factories import PostFactory, UserFactory
        PostFactory(posted_by=user_obj)

    def test_case(self):
        self.default_test_case()

        from fb_post.models import Post
        is_post_exists = not Post.objects.filter(id=post_id).exists()
        self.assert_match_snapshot(name="is_post_deleted",
                                   value=is_post_exists)