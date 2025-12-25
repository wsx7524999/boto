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


class InstagramMetadata(object):
    """
    Represents Instagram metadata for users, posts, and media.
    """
    
    def __init__(self, metadata_type=None, id=None, username=None,
                 caption=None, timestamp=None, media_type=None,
                 media_url=None, permalink=None, like_count=None,
                 comment_count=None, owner=None, tags=None,
                 location=None):
        """
        Initialize Instagram metadata object.
        
        :type metadata_type: string
        :param metadata_type: Type of metadata (user, post, media)
        
        :type id: string
        :param id: Unique identifier
        
        :type username: string
        :param username: Instagram username
        
        :type caption: string
        :param caption: Post caption text
        
        :type timestamp: string
        :param timestamp: ISO 8601 formatted timestamp
        
        :type media_type: string
        :param media_type: Type of media (IMAGE, VIDEO, CAROUSEL_ALBUM)
        
        :type media_url: string
        :param media_url: URL to the media content
        
        :type permalink: string
        :param permalink: Permanent link to the post
        
        :type like_count: int
        :param like_count: Number of likes
        
        :type comment_count: int
        :param comment_count: Number of comments
        
        :type owner: dict
        :param owner: Owner information dictionary
        
        :type tags: list
        :param tags: List of hashtags
        
        :type location: dict
        :param location: Location information dictionary
        """
        self.metadata_type = metadata_type
        self.id = id
        self.username = username
        self.caption = caption
        self.timestamp = timestamp
        self.media_type = media_type
        self.media_url = media_url
        self.permalink = permalink
        self.like_count = like_count
        self.comment_count = comment_count
        self.owner = owner or {}
        self.tags = tags or []
        self.location = location or {}

    def __repr__(self):
        return 'InstagramMetadata:%s:%s' % (self.metadata_type, self.id)

    def to_dict(self):
        """
        Convert metadata to dictionary format.
        
        :rtype: dict
        :return: Dictionary representation of metadata
        """
        return {
            'metadata_type': self.metadata_type,
            'id': self.id,
            'username': self.username,
            'caption': self.caption,
            'timestamp': self.timestamp,
            'media_type': self.media_type,
            'media_url': self.media_url,
            'permalink': self.permalink,
            'like_count': self.like_count,
            'comment_count': self.comment_count,
            'owner': self.owner,
            'tags': self.tags,
            'location': self.location
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create InstagramMetadata instance from dictionary.
        
        :type data: dict
        :param data: Dictionary containing metadata fields
        
        :rtype: :class:`InstagramMetadata`
        :return: New InstagramMetadata instance
        """
        return cls(
            metadata_type=data.get('metadata_type'),
            id=data.get('id'),
            username=data.get('username'),
            caption=data.get('caption'),
            timestamp=data.get('timestamp'),
            media_type=data.get('media_type'),
            media_url=data.get('media_url'),
            permalink=data.get('permalink'),
            like_count=data.get('like_count'),
            comment_count=data.get('comment_count'),
            owner=data.get('owner', {}),
            tags=data.get('tags', []),
            location=data.get('location', {})
        )


class InstagramUser(InstagramMetadata):
    """
    Represents Instagram user metadata.
    """
    
    def __init__(self, id=None, username=None, full_name=None,
                 biography=None, followers_count=None, following_count=None,
                 media_count=None, profile_picture_url=None, 
                 is_verified=None, is_private=None):
        """
        Initialize Instagram user metadata.
        
        :type id: string
        :param id: User ID
        
        :type username: string
        :param username: Username
        
        :type full_name: string
        :param full_name: User's full name
        
        :type biography: string
        :param biography: User biography
        
        :type followers_count: int
        :param followers_count: Number of followers
        
        :type following_count: int
        :param following_count: Number of accounts following
        
        :type media_count: int
        :param media_count: Number of media posts
        
        :type profile_picture_url: string
        :param profile_picture_url: URL to profile picture
        
        :type is_verified: bool
        :param is_verified: Whether user is verified
        
        :type is_private: bool
        :param is_private: Whether account is private
        """
        super(InstagramUser, self).__init__(
            metadata_type='user',
            id=id,
            username=username
        )
        self.full_name = full_name
        self.biography = biography
        self.followers_count = followers_count
        self.following_count = following_count
        self.media_count = media_count
        self.profile_picture_url = profile_picture_url
        self.is_verified = is_verified
        self.is_private = is_private
    
    def to_dict(self):
        """
        Convert user metadata to dictionary format.
        
        :rtype: dict
        :return: Dictionary representation of user metadata
        """
        data = super(InstagramUser, self).to_dict()
        data.update({
            'full_name': self.full_name,
            'biography': self.biography,
            'followers_count': self.followers_count,
            'following_count': self.following_count,
            'media_count': self.media_count,
            'profile_picture_url': self.profile_picture_url,
            'is_verified': self.is_verified,
            'is_private': self.is_private
        })
        return data
    
    @classmethod
    def from_dict(cls, data):
        """
        Create InstagramUser instance from dictionary.
        
        :type data: dict
        :param data: Dictionary containing user metadata fields
        
        :rtype: :class:`InstagramUser`
        :return: New InstagramUser instance
        """
        return cls(
            id=data.get('id'),
            username=data.get('username'),
            full_name=data.get('full_name'),
            biography=data.get('biography'),
            followers_count=data.get('followers_count'),
            following_count=data.get('following_count'),
            media_count=data.get('media_count'),
            profile_picture_url=data.get('profile_picture_url'),
            is_verified=data.get('is_verified'),
            is_private=data.get('is_private')
        )


class InstagramPost(InstagramMetadata):
    """
    Represents Instagram post metadata.
    """
    
    def __init__(self, id=None, caption=None, timestamp=None,
                 media_type=None, media_url=None, permalink=None,
                 like_count=None, comment_count=None, owner=None,
                 tags=None, location=None, thumbnail_url=None,
                 children=None):
        """
        Initialize Instagram post metadata.
        
        :type id: string
        :param id: Post ID
        
        :type caption: string
        :param caption: Post caption
        
        :type timestamp: string
        :param timestamp: Post creation timestamp
        
        :type media_type: string
        :param media_type: Media type (IMAGE, VIDEO, CAROUSEL_ALBUM)
        
        :type media_url: string
        :param media_url: Media URL
        
        :type permalink: string
        :param permalink: Permanent link
        
        :type like_count: int
        :param like_count: Number of likes
        
        :type comment_count: int
        :param comment_count: Number of comments
        
        :type owner: dict
        :param owner: Post owner information
        
        :type tags: list
        :param tags: List of hashtags
        
        :type location: dict
        :param location: Location information
        
        :type thumbnail_url: string
        :param thumbnail_url: Thumbnail URL for videos
        
        :type children: list
        :param children: Child media for carousel posts
        """
        super(InstagramPost, self).__init__(
            metadata_type='post',
            id=id,
            caption=caption,
            timestamp=timestamp,
            media_type=media_type,
            media_url=media_url,
            permalink=permalink,
            like_count=like_count,
            comment_count=comment_count,
            owner=owner,
            tags=tags,
            location=location
        )
        self.thumbnail_url = thumbnail_url
        self.children = children or []
    
    def to_dict(self):
        """
        Convert post metadata to dictionary format.
        
        :rtype: dict
        :return: Dictionary representation of post metadata
        """
        data = super(InstagramPost, self).to_dict()
        data.update({
            'thumbnail_url': self.thumbnail_url,
            'children': self.children
        })
        return data
    
    @classmethod
    def from_dict(cls, data):
        """
        Create InstagramPost instance from dictionary.
        
        :type data: dict
        :param data: Dictionary containing post metadata fields
        
        :rtype: :class:`InstagramPost`
        :return: New InstagramPost instance
        """
        return cls(
            id=data.get('id'),
            caption=data.get('caption'),
            timestamp=data.get('timestamp'),
            media_type=data.get('media_type'),
            media_url=data.get('media_url'),
            permalink=data.get('permalink'),
            like_count=data.get('like_count'),
            comment_count=data.get('comment_count'),
            owner=data.get('owner', {}),
            tags=data.get('tags', []),
            location=data.get('location', {}),
            thumbnail_url=data.get('thumbnail_url'),
            children=data.get('children', [])
        )
