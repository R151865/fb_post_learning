"""
# TODO: React To Comment With Valid Details
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

comment_id = 1
reaction_type = "WOW"

REQUEST_BODY = """
{
    "reaction_type": "WOW"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": comment_id},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase03ReactToCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase03ReactToCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        from fb_post.models.factories import CommentFactory
        CommentFactory()

    def test_case(self):
        self.default_test_case()

        from fb_post.models import Reaction
        reaction = Reaction.objects.get(comment_id=comment_id,
                                        reaction="WOW")

        self.assert_match_snapshot(name="reaction_type",
                                   value=reaction.reaction)
        self.assert_match_snapshot(name="comment_id",
                                   value=reaction.comment.id)
        self.assert_match_snapshot(name="user_id",
                                   value=reaction.reacted_by.id)
