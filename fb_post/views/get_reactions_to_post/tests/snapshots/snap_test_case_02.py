# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetReactionsToPostAPITestCase::test_case status'] = 200

snapshots['TestCase02GetReactionsToPostAPITestCase::test_case body'] = [
    {
        'name': 'user1',
        'profile_pic': 'profile_pic/user1.png',
        'reaction': 'WOW',
        'user_id': 3
    },
    {
        'name': 'user2',
        'profile_pic': 'profile_pic/user2.png',
        'reaction': 'LOVE',
        'user_id': 4
    },
    {
        'name': 'user3',
        'profile_pic': 'profile_pic/user3.png',
        'reaction': 'LIT',
        'user_id': 5
    },
    {
        'name': 'user4',
        'profile_pic': 'profile_pic/user4.png',
        'reaction': 'HAHA',
        'user_id': 6
    },
    {
        'name': 'user5',
        'profile_pic': 'profile_pic/user5.png',
        'reaction': 'THUMBS_UP',
        'user_id': 7
    }
]

snapshots['TestCase02GetReactionsToPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '468',
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

snapshots['TestCase02GetReactionsToPostAPITestCase::test_case post_reactions_details'] = [
    {
        'name': 'user1',
        'profile_pic': 'profile_pic/user1.png',
        'reaction': 'WOW',
        'user_id': 3
    },
    {
        'name': 'user2',
        'profile_pic': 'profile_pic/user2.png',
        'reaction': 'LOVE',
        'user_id': 4
    },
    {
        'name': 'user3',
        'profile_pic': 'profile_pic/user3.png',
        'reaction': 'LIT',
        'user_id': 5
    },
    {
        'name': 'user4',
        'profile_pic': 'profile_pic/user4.png',
        'reaction': 'HAHA',
        'user_id': 6
    },
    {
        'name': 'user5',
        'profile_pic': 'profile_pic/user5.png',
        'reaction': 'THUMBS_UP',
        'user_id': 7
    }
]
