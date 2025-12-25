#!/usr/bin/env python
# Copyright (c) 2014 Mitch Garnaat http://garnaat.org/
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../..'))
from boto.instagram.connection import InstagramConnection


class TestInstagramConnection(unittest.TestCase):
    
    def test_connection_initialization(self):
        conn = InstagramConnection(
            aws_access_key_id='test_key',
            aws_secret_access_key='test_secret'
        )
        self.assertIsNotNone(conn)
        self.assertEqual(conn.region.name, 'us-east-1')
    
    def test_connection_with_region(self):
        from boto.regioninfo import RegionInfo
        region = RegionInfo(
            name='us-west-2',
            endpoint='instagram.us-west-2.amazonaws.com'
        )
        conn = InstagramConnection(
            aws_access_key_id='test_key',
            aws_secret_access_key='test_secret',
            region=region
        )
        self.assertEqual(conn.region.name, 'us-west-2')
    
    def test_required_auth_capability(self):
        conn = InstagramConnection(
            aws_access_key_id='test_key',
            aws_secret_access_key='test_secret'
        )
        capabilities = conn._required_auth_capability()
        self.assertEqual(capabilities, ['hmac-v4'])


if __name__ == '__main__':
    unittest.main()
