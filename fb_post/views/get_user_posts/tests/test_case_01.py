"""
# TODO: Get User Posts
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.utils.custom_test_utils_2 import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from freezegun import freeze_time
from fb_post.models.factories import (
    PostFactory, CommentFactory, PostReactionFactory,
    CommentReactionFactory, ReplyFactory
    )


REQUEST_BODY = """
{}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"offset": 0, "limit": 100},
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


class TestCase01GetUserPostsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetUserPostsAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.pop_data(username)

    @freeze_time("2000-10-10")
    def pop_data(self, username):
        from fb_post.models import User
        user_obj = User.objects.get(username=username)
        post_objs = PostFactory.create_batch(size=3, posted_by=user_obj)

        # post_obj 1 data
        comment_objs = []
        comment_objs.extend(
            CommentFactory.create_batch(size=2, post=post_objs[0])
            )
        comment_objs.extend(
            CommentFactory.create_batch(size=2, post=post_objs[0])
            )

        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[0])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[1])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[2])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[3])
        
        
        PostReactionFactory.create_batch(size=10, post=post_objs[00])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[0])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[1])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[2])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[3])

        # post_obj 2 data
        comment_objs = []
        comment_objs.extend(
            CommentFactory.create_batch(size=2, post=post_objs[1])
            )
        comment_objs.extend(
            CommentFactory.create_batch(size=2, post=post_objs[1])
            )

        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[0])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[1])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[2])
        ReplyFactory.create_batch(size=2, parent_comment=comment_objs[3])

        PostReactionFactory.create_batch(size=10, post=post_objs[1])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[0])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[1])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[2])
        CommentReactionFactory.create_batch(size=10, comment=comment_objs[3])


    def test_case(self):
        response = self.default_test_case()

        import json
        response_content = json.loads(response.content)
        print(response_content)
        self.assert_match_snapshot(name="user_post_details_in_dict",
                                   value=response_content)

        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        
        # get users Post
    # description 3 min
    #  post 3  comments 2 replies 4 post reaction 10 comments reaction 10 3 min
    # 1 min