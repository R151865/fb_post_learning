# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03ReplyToCommentAPITestCase::test_case status'] = 201

snapshots['TestCase03ReplyToCommentAPITestCase::test_case body'] = {
    'comment_id': 2
}

snapshots['TestCase03ReplyToCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '17',
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

snapshots['TestCase03ReplyToCommentAPITestCase::test_case reply_content'] = 'string'

snapshots['TestCase03ReplyToCommentAPITestCase::test_case user_id'] = 1

snapshots['TestCase03ReplyToCommentAPITestCase::test_case parent_comment_id'] = 1
