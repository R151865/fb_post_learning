# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03ReactToCommentAPITestCase::test_case status'] = 200

snapshots['TestCase03ReactToCommentAPITestCase::test_case body'] = b''

snapshots['TestCase03ReactToCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase03ReactToCommentAPITestCase::test_case reaction_type'] = 'WOW'

snapshots['TestCase03ReactToCommentAPITestCase::test_case comment_id'] = 1

snapshots['TestCase03ReactToCommentAPITestCase::test_case user_id'] = 1
