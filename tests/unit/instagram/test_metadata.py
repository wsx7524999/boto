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
from boto.instagram.metadata import InstagramMetadata, InstagramUser, InstagramPost


class TestInstagramMetadata(unittest.TestCase):
    
    def test_metadata_initialization(self):
        metadata = InstagramMetadata(
            metadata_type='post',
            id='12345',
            username='testuser',
            caption='Test caption'
        )
        self.assertEqual(metadata.metadata_type, 'post')
        self.assertEqual(metadata.id, '12345')
        self.assertEqual(metadata.username, 'testuser')
        self.assertEqual(metadata.caption, 'Test caption')
    
    def test_metadata_repr(self):
        metadata = InstagramMetadata(metadata_type='post', id='12345')
        self.assertEqual(repr(metadata), 'InstagramMetadata:post:12345')
    
    def test_metadata_to_dict(self):
        metadata = InstagramMetadata(
            metadata_type='post',
            id='12345',
            username='testuser',
            caption='Test caption',
            like_count=100,
            tags=['tag1', 'tag2']
        )
        result = metadata.to_dict()
        self.assertEqual(result['metadata_type'], 'post')
        self.assertEqual(result['id'], '12345')
        self.assertEqual(result['username'], 'testuser')
        self.assertEqual(result['like_count'], 100)
        self.assertEqual(result['tags'], ['tag1', 'tag2'])
    
    def test_metadata_from_dict(self):
        data = {
            'metadata_type': 'post',
            'id': '12345',
            'username': 'testuser',
            'caption': 'Test caption',
            'like_count': 100,
            'tags': ['tag1', 'tag2']
        }
        metadata = InstagramMetadata.from_dict(data)
        self.assertEqual(metadata.metadata_type, 'post')
        self.assertEqual(metadata.id, '12345')
        self.assertEqual(metadata.username, 'testuser')
        self.assertEqual(metadata.like_count, 100)
        self.assertEqual(metadata.tags, ['tag1', 'tag2'])


class TestInstagramUser(unittest.TestCase):
    
    def test_user_initialization(self):
        user = InstagramUser(
            id='user123',
            username='testuser',
            full_name='Test User',
            followers_count=1000,
            is_verified=True
        )
        self.assertEqual(user.metadata_type, 'user')
        self.assertEqual(user.id, 'user123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.full_name, 'Test User')
        self.assertEqual(user.followers_count, 1000)
        self.assertTrue(user.is_verified)
    
    def test_user_to_dict(self):
        user = InstagramUser(
            id='user123',
            username='testuser',
            full_name='Test User',
            biography='Test bio',
            followers_count=1000,
            following_count=500,
            is_verified=True
        )
        result = user.to_dict()
        self.assertEqual(result['id'], 'user123')
        self.assertEqual(result['full_name'], 'Test User')
        self.assertEqual(result['biography'], 'Test bio')
        self.assertEqual(result['followers_count'], 1000)
        self.assertEqual(result['following_count'], 500)
        self.assertTrue(result['is_verified'])
    
    def test_user_from_dict(self):
        data = {
            'id': 'user123',
            'username': 'testuser',
            'full_name': 'Test User',
            'biography': 'Test bio',
            'followers_count': 1000,
            'is_verified': True
        }
        user = InstagramUser.from_dict(data)
        self.assertEqual(user.id, 'user123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.full_name, 'Test User')
        self.assertEqual(user.biography, 'Test bio')
        self.assertEqual(user.followers_count, 1000)
        self.assertTrue(user.is_verified)


class TestInstagramPost(unittest.TestCase):
    
    def test_post_initialization(self):
        post = InstagramPost(
            id='post123',
            caption='Test post',
            media_type='IMAGE',
            like_count=50,
            comment_count=10,
            tags=['instagram', 'test']
        )
        self.assertEqual(post.metadata_type, 'post')
        self.assertEqual(post.id, 'post123')
        self.assertEqual(post.caption, 'Test post')
        self.assertEqual(post.media_type, 'IMAGE')
        self.assertEqual(post.like_count, 50)
        self.assertEqual(post.comment_count, 10)
        self.assertEqual(len(post.tags), 2)
    
    def test_post_with_children(self):
        children = [
            {'id': 'child1', 'media_url': 'http://example.com/1.jpg'},
            {'id': 'child2', 'media_url': 'http://example.com/2.jpg'}
        ]
        post = InstagramPost(
            id='carousel123',
            media_type='CAROUSEL_ALBUM',
            children=children
        )
        self.assertEqual(post.media_type, 'CAROUSEL_ALBUM')
        self.assertEqual(len(post.children), 2)
    
    def test_post_to_dict(self):
        post = InstagramPost(
            id='post123',
            caption='Test post',
            media_type='IMAGE',
            like_count=50,
            thumbnail_url='http://example.com/thumb.jpg',
            children=[{'id': 'child1'}]
        )
        result = post.to_dict()
        self.assertEqual(result['id'], 'post123')
        self.assertEqual(result['caption'], 'Test post')
        self.assertEqual(result['thumbnail_url'], 'http://example.com/thumb.jpg')
        self.assertEqual(len(result['children']), 1)
    
    def test_post_from_dict(self):
        data = {
            'id': 'post123',
            'caption': 'Test post',
            'media_type': 'IMAGE',
            'like_count': 50,
            'thumbnail_url': 'http://example.com/thumb.jpg',
            'children': [{'id': 'child1'}]
        }
        post = InstagramPost.from_dict(data)
        self.assertEqual(post.id, 'post123')
        self.assertEqual(post.caption, 'Test post')
        self.assertEqual(post.thumbnail_url, 'http://example.com/thumb.jpg')
        self.assertEqual(len(post.children), 1)


if __name__ == '__main__':
    unittest.main()
