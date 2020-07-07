# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetRepliesForCommentAPITestCase::test_case status'] = 200

snapshots['TestCase02GetRepliesForCommentAPITestCase::test_case body'] = [
    {
        'comment_content': 'reply content0',
        'comment_id': 2,
        'commented_at': '2000-10-10 00:00:00.000000',
        'commenter': {
            'name': 'user2',
            'profile_pic': 'profile_pic/user2.png',
            'user_id': 4
        }
    },
    {
        'comment_content': 'reply content1',
        'comment_id': 3,
        'commented_at': '2000-10-10 00:00:00.000000',
        'commenter': {
            'name': 'user4',
            'profile_pic': 'profile_pic/user4.png',
            'user_id': 6
        }
    }
]

snapshots['TestCase02GetRepliesForCommentAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '376',
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

snapshots['TestCase02GetRepliesForCommentAPITestCase::test_case dict'] = [
    {
        'comment_content': 'reply content0',
        'comment_id': 2,
        'commented_at': '2000-10-10 00:00:00.000000',
        'commenter': {
            'name': 'user2',
            'profile_pic': 'profile_pic/user2.png',
            'user_id': 4
        }
    },
    {
        'comment_content': 'reply content1',
        'comment_id': 3,
        'commented_at': '2000-10-10 00:00:00.000000',
        'commenter': {
            'name': 'user4',
            'profile_pic': 'profile_pic/user4.png',
            'user_id': 6
        }
    }
]
