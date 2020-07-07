# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "reply_to_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/{comment_id}/reply/v1/"

from .test_case_01 import TestCase01ReplyToCommentAPITestCase
from .test_case_02 import TestCase02ReplyToCommentAPITestCase
from .test_case_03 import TestCase03ReplyToCommentAPITestCase
from .test_case_04 import TestCase04ReplyToCommentAPITestCase

__all__ = [
    "TestCase01ReplyToCommentAPITestCase",
    "TestCase02ReplyToCommentAPITestCase",
    "TestCase03ReplyToCommentAPITestCase",
    "TestCase04ReplyToCommentAPITestCase"
]
