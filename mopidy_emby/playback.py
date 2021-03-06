from __future__ import unicode_literals

import logging

from mopidy import backend


logger = logging.getLogger(__name__)


class EmbyPlaybackProvider(backend.PlaybackProvider):

    def translate_uri(self, uri):
        if uri.startswith('emby:track:') and len(uri.split(':')) == 3:
            id = uri.split(':')[-1]

            track_url = self.backend.remote.api_url(
                '/Audio/{}/stream?static=true'.format(id)
            )

            logger.debug('Emby track streaming url: {}'.format(track_url))

            return track_url

        else:
            return None
