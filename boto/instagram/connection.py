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

from boto.connection import AWSQueryConnection
from boto.regioninfo import RegionInfo
from boto.instagram.metadata import InstagramMetadata
import boto


class InstagramConnection(AWSQueryConnection):
    """
    Instagram Metadata Service Connection
    
    This service provides access to Instagram metadata information
    including posts, users, and media details.
    """
    
    APIVersion = '2014-01-01'
    DefaultRegionName = 'us-east-1'
    DefaultRegionEndpoint = 'instagram.us-east-1.amazonaws.com'
    ResponseError = None

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 is_secure=True, port=None, proxy=None, proxy_port=None,
                 proxy_user=None, proxy_pass=None, debug=0,
                 https_connection_factory=None, region=None, path='/',
                 api_version=None, security_token=None,
                 validate_certs=True, profile_name=None):
        """
        Initialize an Instagram connection.
        
        :type aws_access_key_id: string
        :param aws_access_key_id: Your AWS Access Key ID
        
        :type aws_secret_access_key: string
        :param aws_secret_access_key: Your AWS Secret Access Key
        
        :type region: :class:`boto.regioninfo.RegionInfo`
        :param region: The region to connect to.
        """
        if not region:
            region = RegionInfo(self, self.DefaultRegionName,
                                self.DefaultRegionEndpoint)
        self.region = region
        
        super(InstagramConnection, self).__init__(
            aws_access_key_id, aws_secret_access_key,
            is_secure, port, proxy, proxy_port, proxy_user, proxy_pass,
            self.region.endpoint, debug, https_connection_factory, path,
            security_token, validate_certs=validate_certs,
            profile_name=profile_name)

    def _required_auth_capability(self):
        return ['hmac-v4']

    def get_user_metadata(self, user_id):
        """
        Get metadata for a specific Instagram user.
        
        :type user_id: string
        :param user_id: The Instagram user ID
        
        :rtype: :class:`boto.instagram.metadata.InstagramMetadata`
        :return: Instagram user metadata
        """
        params = {'UserId': user_id}
        return self.make_request(
            action='GetUserMetadata',
            verb='POST',
            path='/',
            params=params
        )

    def get_post_metadata(self, post_id):
        """
        Get metadata for a specific Instagram post.
        
        :type post_id: string
        :param post_id: The Instagram post ID
        
        :rtype: :class:`boto.instagram.metadata.InstagramMetadata`
        :return: Instagram post metadata
        """
        params = {'PostId': post_id}
        return self.make_request(
            action='GetPostMetadata',
            verb='POST',
            path='/',
            params=params
        )

    def get_media_metadata(self, media_id):
        """
        Get metadata for a specific Instagram media item.
        
        :type media_id: string
        :param media_id: The Instagram media ID
        
        :rtype: :class:`boto.instagram.metadata.InstagramMetadata`
        :return: Instagram media metadata
        """
        params = {'MediaId': media_id}
        return self.make_request(
            action='GetMediaMetadata',
            verb='POST',
            path='/',
            params=params
        )

    def list_user_posts(self, user_id, max_results=None, next_token=None):
        """
        List posts for a specific Instagram user.
        
        :type user_id: string
        :param user_id: The Instagram user ID
        
        :type max_results: int
        :param max_results: Maximum number of results to return
        
        :type next_token: string
        :param next_token: Token for pagination
        
        :rtype: list
        :return: List of Instagram post metadata
        """
        params = {'UserId': user_id}
        if max_results:
            params['MaxResults'] = max_results
        if next_token:
            params['NextToken'] = next_token
        return self.make_request(
            action='ListUserPosts',
            verb='POST',
            path='/',
            params=params
        )
