# Instagram Metadata Service

## Overview

The Instagram Metadata Service module for boto provides a well-structured interface for interacting with Instagram metadata, including users, posts, and media content.

## Features

- **User Metadata**: Retrieve comprehensive user profile information
- **Post Metadata**: Access post details including captions, timestamps, and engagement metrics
- **Media Metadata**: Get media-specific information for images, videos, and carousel albums
- **List Operations**: Retrieve lists of posts for specific users

## Installation

The Instagram module is included as part of boto. Simply install boto:

```bash
pip install boto
```

## Quick Start

### Connecting to Instagram Metadata Service

```python
import boto

# Connect using AWS credentials
conn = boto.connect_instagram(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# Or connect to a specific region
import boto.instagram
conn = boto.instagram.connect_to_region(
    'us-east-1',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)
```

## Usage Examples

### Retrieving User Metadata

```python
from boto.instagram.metadata import InstagramUser

# Get user metadata
response = conn.get_user_metadata(user_id='instagram_user_123')

# Create user object from response
user = InstagramUser(
    id='instagram_user_123',
    username='example_user',
    full_name='Example User',
    biography='This is my bio',
    followers_count=10000,
    following_count=500,
    media_count=250,
    is_verified=True,
    is_private=False
)
```

### Retrieving Post Metadata

```python
from boto.instagram.metadata import InstagramPost

# Get post metadata
response = conn.get_post_metadata(post_id='post_abc123')

# Create post object
post = InstagramPost(
    id='post_abc123',
    caption='Amazing sunset! #nature #photography',
    timestamp='2024-12-25T12:00:00Z',
    media_type='IMAGE',
    media_url='https://example.com/image.jpg',
    permalink='https://instagram.com/p/abc123',
    like_count=500,
    comment_count=25,
    tags=['nature', 'photography'],
    owner={'id': 'user_123', 'username': 'photographer'}
)
```

### Retrieving Media Metadata

```python
# Get media metadata
response = conn.get_media_metadata(media_id='media_xyz789')
```

### Listing User Posts

```python
# List posts for a user
response = conn.list_user_posts(
    user_id='instagram_user_123',
    max_results=20
)

# With pagination
response = conn.list_user_posts(
    user_id='instagram_user_123',
    max_results=20,
    next_token='pagination_token'
)
```

## Metadata Classes

### InstagramMetadata

Base class for all Instagram metadata objects.

**Attributes:**
- `metadata_type`: Type of metadata (user, post, media)
- `id`: Unique identifier
- `username`: Instagram username
- `caption`: Post caption text
- `timestamp`: ISO 8601 formatted timestamp
- `media_type`: Type of media (IMAGE, VIDEO, CAROUSEL_ALBUM)
- `media_url`: URL to the media content
- `permalink`: Permanent link to the post
- `like_count`: Number of likes
- `comment_count`: Number of comments
- `owner`: Owner information dictionary
- `tags`: List of hashtags
- `location`: Location information dictionary

**Methods:**
- `to_dict()`: Convert metadata to dictionary
- `from_dict(data)`: Create metadata from dictionary

### InstagramUser

Represents Instagram user metadata.

**Additional Attributes:**
- `full_name`: User's full name
- `biography`: User biography
- `followers_count`: Number of followers
- `following_count`: Number of accounts following
- `media_count`: Number of media posts
- `profile_picture_url`: URL to profile picture
- `is_verified`: Whether user is verified
- `is_private`: Whether account is private

### InstagramPost

Represents Instagram post metadata.

**Additional Attributes:**
- `thumbnail_url`: Thumbnail URL for videos
- `children`: Child media for carousel posts

## Error Handling

```python
try:
    response = conn.get_user_metadata(user_id='invalid_user')
except Exception as e:
    print("Error retrieving user metadata:", e)
```

## Best Practices

1. **Use appropriate error handling** for all API calls
2. **Implement pagination** when listing posts to handle large datasets
3. **Cache metadata** when appropriate to reduce API calls
4. **Respect rate limits** when making multiple requests

## Region Support

The Instagram Metadata Service supports the following AWS regions:

- us-east-1 (default)
- us-west-2
- eu-west-1
- ap-southeast-1

## API Reference

### Connection Methods

- `get_user_metadata(user_id)`: Get metadata for a specific user
- `get_post_metadata(post_id)`: Get metadata for a specific post
- `get_media_metadata(media_id)`: Get metadata for a specific media item
- `list_user_posts(user_id, max_results=None, next_token=None)`: List posts for a user

## Contributing

Contributions to the Instagram Metadata Service module are welcome! Please follow the boto contribution guidelines.

## License

This module is part of boto and is licensed under the MIT License. See the LICENSE file for details.
