"""
# TODO: Create Reply To Comment With Reply Id
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "2"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase04ReplyToCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase04ReplyToCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        from fb_post.models.factories import ReplyFactory, CommentFactory
        comment_obj = CommentFactory()
        ReplyFactory(parent_comment=comment_obj)

    def test_case(self):
        response = self.default_test_case()

        import json
        response_content = json.loads(response.content)
        reply_id = response_content["comment_id"]

        from fb_post.models import Comment
        comment = Comment.objects.get(id=reply_id)

        self.assert_match_snapshot(name="reply_content",
                                   value=comment.content)
        self.assert_match_snapshot(name="user_id",
                                   value=comment.commented_by.id)
        self.assert_match_snapshot(name="parent_comment_id",
                                   value=comment.parent_comment.id)
