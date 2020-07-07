# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetPostAPITestCase::test_case status'] = 200

snapshots['TestCase02GetPostAPITestCase::test_case body'] = {
    'comments': [
        {
            'comment_content': 'comment content0',
            'comment_id': 1,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user1',
                'profile_pic': 'profile_pic/user1.png',
                'user_id': 3
            },
            'reactions': {
                'count': 5,
                'type': [
                    'HAHA',
                    'LIT',
                    'LOVE',
                    'THUMBS_UP',
                    'WOW'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        },
        {
            'comment_content': 'comment content1',
            'comment_id': 2,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user2',
                'profile_pic': 'profile_pic/user2.png',
                'user_id': 4
            },
            'reactions': {
                'count': 5,
                'type': [
                    'ANGRY',
                    'LOVE',
                    'SAD',
                    'THUMBS_DOWN',
                    'WOW'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        },
        {
            'comment_content': 'comment content2',
            'comment_id': 3,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user3',
                'profile_pic': 'profile_pic/user3.png',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        }
    ],
    'comments_count': 3,
    'post_content': 'post content0',
    'post_id': 1,
    'posted_at': '2000-10-10 00:00:00.000000',
    'posted_by': {
        'name': 'user0',
        'profile_pic': 'profile_pic/user0.png',
        'user_id': 2
    },
    'reactions': {
        'count': 10,
        'type': [
            'ANGRY',
            'HAHA',
            'LIT',
            'LOVE',
            'SAD',
            'THUMBS_DOWN',
            'THUMBS_UP',
            'WOW'
        ]
    }
}

snapshots['TestCase02GetPostAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '1200',
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

snapshots['TestCase02GetPostAPITestCase::test_case get_post_details_dict'] = {
    'comments': [
        {
            'comment_content': 'comment content0',
            'comment_id': 1,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user1',
                'profile_pic': 'profile_pic/user1.png',
                'user_id': 3
            },
            'reactions': {
                'count': 5,
                'type': [
                    'HAHA',
                    'LIT',
                    'LOVE',
                    'THUMBS_UP',
                    'WOW'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        },
        {
            'comment_content': 'comment content1',
            'comment_id': 2,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user2',
                'profile_pic': 'profile_pic/user2.png',
                'user_id': 4
            },
            'reactions': {
                'count': 5,
                'type': [
                    'ANGRY',
                    'LOVE',
                    'SAD',
                    'THUMBS_DOWN',
                    'WOW'
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        },
        {
            'comment_content': 'comment content2',
            'comment_id': 3,
            'commented_at': '2000-10-10 00:00:00.000000',
            'commenter': {
                'name': 'user3',
                'profile_pic': 'profile_pic/user3.png',
                'user_id': 5
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            },
            'replies': [
            ],
            'replies_count': 0
        }
    ],
    'comments_count': 3,
    'post_content': 'post content0',
    'post_id': 1,
    'posted_at': '2000-10-10 00:00:00.000000',
    'posted_by': {
        'name': 'user0',
        'profile_pic': 'profile_pic/user0.png',
        'user_id': 2
    },
    'reactions': {
        'count': 10,
        'type': [
            'ANGRY',
            'HAHA',
            'LIT',
            'LOVE',
            'SAD',
            'THUMBS_DOWN',
            'THUMBS_UP',
            'WOW'
        ]
    }
}
