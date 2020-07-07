# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTotalReactionCountAPITestCase::test_case status'] = 200

snapshots['TestCase01GetTotalReactionCountAPITestCase::test_case body'] = {
    'count': 10
}

snapshots['TestCase01GetTotalReactionCountAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '13',
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

snapshots['TestCase01GetTotalReactionCountAPITestCase::test_case total_reaction_count'] = 10
