# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserPostsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUserPostsAPITestCase::test_case body'] = {
    'posts': [
        {
            'comments': [
                {
                    'comment_content': 'comment content0',
                    'comment_id': 1,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
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
                        'name': 'user1',
                        'profile_pic': 'profile_pic/user1.png',
                        'user_id': 3
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
                        'name': 'user2',
                        'profile_pic': 'profile_pic/user2.png',
                        'user_id': 4
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content3',
                    'comment_id': 4,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user3',
                        'profile_pic': 'profile_pic/user3.png',
                        'user_id': 5
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                }
            ],
            'comments_count': 4,
            'post_content': 'post content0',
            'post_id': 1,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
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
        },
        {
            'comments': [
                {
                    'comment_content': 'comment content4',
                    'comment_id': 13,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user70',
                        'profile_pic': 'profile_pic/user70.png',
                        'user_id': 72
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content5',
                    'comment_id': 14,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user71',
                        'profile_pic': 'profile_pic/user71.png',
                        'user_id': 73
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content6',
                    'comment_id': 15,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user72',
                        'profile_pic': 'profile_pic/user72.png',
                        'user_id': 74
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content7',
                    'comment_id': 16,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user73',
                        'profile_pic': 'profile_pic/user73.png',
                        'user_id': 75
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                }
            ],
            'comments_count': 4,
            'post_content': 'post content1',
            'post_id': 2,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
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
        },
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'post content2',
            'post_id': 3,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            }
        }
    ],
    'total_count': 3
}

snapshots['TestCase01GetUserPostsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '3567',
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

snapshots['TestCase01GetUserPostsAPITestCase::test_case user_post_details_in_dict'] = {
    'posts': [
        {
            'comments': [
                {
                    'comment_content': 'comment content0',
                    'comment_id': 1,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
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
                        'name': 'user1',
                        'profile_pic': 'profile_pic/user1.png',
                        'user_id': 3
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
                        'name': 'user2',
                        'profile_pic': 'profile_pic/user2.png',
                        'user_id': 4
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content3',
                    'comment_id': 4,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user3',
                        'profile_pic': 'profile_pic/user3.png',
                        'user_id': 5
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                }
            ],
            'comments_count': 4,
            'post_content': 'post content0',
            'post_id': 1,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
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
        },
        {
            'comments': [
                {
                    'comment_content': 'comment content4',
                    'comment_id': 13,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user70',
                        'profile_pic': 'profile_pic/user70.png',
                        'user_id': 72
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content5',
                    'comment_id': 14,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user71',
                        'profile_pic': 'profile_pic/user71.png',
                        'user_id': 73
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content6',
                    'comment_id': 15,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user72',
                        'profile_pic': 'profile_pic/user72.png',
                        'user_id': 74
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                },
                {
                    'comment_content': 'comment content7',
                    'comment_id': 16,
                    'commented_at': '2000-10-10 00:00:00.000000',
                    'commenter': {
                        'name': 'user73',
                        'profile_pic': 'profile_pic/user73.png',
                        'user_id': 75
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
                    },
                    'replies': [
                    ],
                    'replies_count': 0
                }
            ],
            'comments_count': 4,
            'post_content': 'post content1',
            'post_id': 2,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
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
        },
        {
            'comments': [
            ],
            'comments_count': 0,
            'post_content': 'post content2',
            'post_id': 3,
            'posted_at': '2000-10-10 00:00:00.000000',
            'posted_by': {
                'name': '',
                'profile_pic': '',
                'user_id': 1
            },
            'reactions': {
                'count': 0,
                'type': [
                ]
            }
        }
    ],
    'total_count': 3
}
