"""
# TODO: Get Replies For Comment With Valid Details Return List
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from fb_post.utils.custom_test_utils_2 import CustomTestUtils

REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1"},
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

from freezegun import freeze_time

class TestCase02GetRepliesForCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02GetRepliesForCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.pop_data()

    @freeze_time("2000-10-10")
    def pop_data(self):
        from fb_post.models.factories import CommentFactory, ReplyFactory
        comment_obj = CommentFactory()
        ReplyFactory.create_batch(size=2, parent_comment=comment_obj)

    def test_case(self):
        response = self.default_test_case()

        import json
        response_content = json.loads(response.content)
        reply1 = response_content[0]
        reply2 = response_content[1]

        self.assert_match_snapshot(name="dict", value=response_content)

        # self.assert_match_snapshot(name="reply1_id",
        #                           value=reply1["comment_id"])
        # self.assert_match_snapshot(name="reply1_content",
        #                           value=reply1["comment_content"])
        # self.assert_match_snapshot(name="reply1_at",
        #                           value=reply1["commented_at"])
        # self.assert_match_snapshot(name="reply1_commenter",
        #                           value=reply1["commenter"]["name"])
        # self.assert_match_snapshot(name="reply1_commenter_id",
        #                           value=reply1["commenter"]["user_id"])
        # self.assert_match_snapshot(name="reply1_commenter_profile_pic",
        #                           value=reply1["commenter"]["profile_pic"])


#     {
#         'comment_content': 'reply content0',
#         'comment_id': 2,
#         'commented_at': '2020-06-24 21:06:25.520988',
#         'commenter': {
#             'name': 'user2',
#             'profile_pic': 'profile_pic/user2.png',
#             'user_id': 4
#         }
#     },
#     {
#         'comment_content': 'reply content1',
#         'comment_id': 3,
#         'commented_at': '2020-06-24 21:06:25.523579',
#         'commenter': {
#             'name': 'user4',
#             'profile_pic': 'profile_pic/user4.png',
#             'user_id': 6
#         }
#     }
# """