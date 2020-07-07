# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "get_resources"
REQUEST_METHOD = "get"
URL_SUFFIX = "resources/v2/"

from .test_case_01 import TestCase01GetResourcesAPITestCase

__all__ = [
    "TestCase01GetResourcesAPITestCase"
]
