# Copyright 2013 Google Inc. All Rights Reserved.

"""Auth for the Google Cloud SDK.
"""

from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Auth(base.Group):
  """Manage oauth2 credentials for the Google Cloud SDK."""
