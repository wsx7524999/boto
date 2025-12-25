#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Instagram Metadata Service Example

This example demonstrates how to use the Instagram Metadata Service
module in boto to interact with Instagram data.

Note: This is a conceptual implementation demonstrating the structure
for a hypothetical Instagram metadata service integration. The actual
endpoints and API would need to be configured based on the real service
being wrapped (e.g., Facebook Graph API, Instagram Basic Display API).

For production use, ensure you have:
1. Valid API credentials from Instagram/Facebook
2. Proper endpoint configuration
3. Appropriate rate limiting and error handling
"""

# Example 1: Basic Connection
def example_basic_connection():
    """Show how to establish a basic connection"""
    import boto
    
    # Connect using default region
    conn = boto.connect_instagram(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    return conn


# Example 2: Working with User Metadata
def example_user_metadata():
    """Show how to work with user metadata"""
    from boto.instagram.metadata import InstagramUser
    
    # Create a user metadata object
    user = InstagramUser(
        id='17841405822304914',
        username='example_user',
        full_name='Example User',
        biography='Living life one photo at a time 📸',
        followers_count=15000,
        following_count=500,
        media_count=350,
        profile_picture_url='https://example.com/profile.jpg',
        is_verified=True,
        is_private=False
    )
    
    # Convert to dictionary
    user_dict = user.to_dict()
    print("User as dict:", user_dict)
    
    # Create from dictionary
    new_user = InstagramUser.from_dict(user_dict)
    print("Recreated user:", new_user)
    
    return user


# Example 3: Working with Post Metadata
def example_post_metadata():
    """Show how to work with post metadata"""
    from boto.instagram.metadata import InstagramPost
    
    # Create a post metadata object
    post = InstagramPost(
        id='17895695668004550',
        caption='Beautiful sunset at the beach! 🌅 #sunset #beach #nature',
        timestamp='2024-12-25T18:30:00Z',
        media_type='IMAGE',
        media_url='https://example.com/sunset.jpg',
        permalink='https://www.instagram.com/p/ABC123/',
        like_count=1250,
        comment_count=48,
        owner={
            'id': '17841405822304914',
            'username': 'example_user'
        },
        tags=['sunset', 'beach', 'nature'],
        location={
            'id': '213385402',
            'name': 'Santa Monica Beach',
            'latitude': 34.0195,
            'longitude': -118.4912
        }
    )
    
    print("Post ID:", post.id)
    print("Caption:", post.caption)
    print("Likes:", post.like_count)
    print("Tags:", post.tags)
    
    return post


# Example 4: Working with Carousel Posts
def example_carousel_post():
    """Show how to work with carousel album posts"""
    from boto.instagram.metadata import InstagramPost
    
    # Create a carousel post with multiple media items
    carousel = InstagramPost(
        id='17912345678901234',
        caption='Amazing vacation photos! Swipe to see more 👉',
        timestamp='2024-12-24T12:00:00Z',
        media_type='CAROUSEL_ALBUM',
        permalink='https://www.instagram.com/p/XYZ789/',
        like_count=2100,
        comment_count=95,
        children=[
            {
                'id': 'child_1',
                'media_type': 'IMAGE',
                'media_url': 'https://example.com/photo1.jpg'
            },
            {
                'id': 'child_2',
                'media_type': 'IMAGE',
                'media_url': 'https://example.com/photo2.jpg'
            },
            {
                'id': 'child_3',
                'media_type': 'VIDEO',
                'media_url': 'https://example.com/video1.mp4',
                'thumbnail_url': 'https://example.com/thumb1.jpg'
            }
        ]
    )
    
    print("Carousel has", len(carousel.children), "items")
    return carousel


# Example 5: Fetching Data from API
def example_fetch_user_data():
    """Show how to fetch user data from the API"""
    import boto
    
    # Establish connection
    conn = boto.connect_instagram(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    
    # Get user metadata
    try:
        response = conn.get_user_metadata(user_id='17841405822304914')
        print("User metadata retrieved:", response)
    except Exception as e:
        print("Error:", e)


# Example 6: Listing User Posts
def example_list_posts():
    """Show how to list posts for a user"""
    import boto
    
    conn = boto.connect_instagram(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    
    # List posts with pagination
    try:
        response = conn.list_user_posts(
            user_id='17841405822304914',
            max_results=25
        )
        print("Posts retrieved:", response)
        
        # If there's a next token, fetch more
        if 'NextToken' in response:
            next_response = conn.list_user_posts(
                user_id='17841405822304914',
                max_results=25,
                next_token=response['NextToken']
            )
            print("Next page retrieved:", next_response)
    except Exception as e:
        print("Error:", e)


# Example 7: Complete Workflow
def example_complete_workflow():
    """Show a complete workflow of fetching and processing Instagram data"""
    import boto
    from boto.instagram.metadata import InstagramMetadata
    
    # Step 1: Connect
    conn = boto.connect_instagram(
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    
    # Step 2: Get user information
    user_id = '17841405822304914'
    try:
        user_data = conn.get_user_metadata(user_id=user_id)
        print("Retrieved user:", user_data)
        
        # Step 3: Get user's posts
        posts_data = conn.list_user_posts(
            user_id=user_id,
            max_results=10
        )
        print("Retrieved", len(posts_data), "posts")
        
        # Step 4: Process each post
        for post_id in posts_data:
            post_metadata = conn.get_post_metadata(post_id=post_id)
            print("Post", post_id, "has", post_metadata.get('like_count'), "likes")
            
    except Exception as e:
        print("Error in workflow:", e)


# Example 8: Region-specific Connection
def example_regional_connection():
    """Show how to connect to specific regions"""
    import boto.instagram
    
    # Connect to US East
    conn_east = boto.instagram.connect_to_region(
        'us-east-1',
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    
    # Connect to US West
    conn_west = boto.instagram.connect_to_region(
        'us-west-2',
        aws_access_key_id='YOUR_ACCESS_KEY',
        aws_secret_access_key='YOUR_SECRET_KEY'
    )
    
    print("Connected to US East:", conn_east)
    print("Connected to US West:", conn_west)


if __name__ == '__main__':
    print("=" * 70)
    print("Instagram Metadata Service Examples")
    print("=" * 70)
    
    print("\n--- Example 1: User Metadata ---")
    user = example_user_metadata()
    
    print("\n--- Example 2: Post Metadata ---")
    post = example_post_metadata()
    
    print("\n--- Example 3: Carousel Post ---")
    carousel = example_carousel_post()
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("Note: Replace 'YOUR_ACCESS_KEY' and 'YOUR_SECRET_KEY' with actual credentials")
