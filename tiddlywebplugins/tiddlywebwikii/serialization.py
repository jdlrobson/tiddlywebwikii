"""
Serialize into a tiddlywiki wiki, leaving out most of the tiddlers
so they can be loaded later by something else.

The missing tiddlers are placed in a tiddler called LazyTiddlers.
"""

from tiddlywebwiki.serialization import (
        Serialization as WikiSerialization)
from tiddlyweb.web.util import tiddler_etag, get_route_value, server_base_url
import simplejson

WIKI = ''

class Serialization(WikiSerialization):

    def _get_config(self):
        def get_container(environ):
          routing_args = environ.get('wsgiorg.routing_args', ([], {}))[1]
          container_name = False
          container_type = 'bags'
          store = environ['tiddlyweb.store']
          if routing_args:
              if 'recipe_name' in routing_args:
                  container_name = get_route_value(self.environ,
                      'recipe_name')
                  container_type = 'recipes'
              elif 'bag_name' in routing_args:
                  container_name = get_route_value(self.environ, 'bag_name')
          if container_name:
              return "%s/%s" % (container_type, container_name)
          else:
              return ""
        json = {"workspace": get_container(self.environ),
            "host": server_base_url(self.environ)}
        return '''
        <script id="tiddlywikiconfig" type="application/json">
        %s
        </script>
        ''' % (simplejson.dumps(json))


    def _get_wiki(self):
        """
        Read base_tiddlywiki from its location.
        """
        global WIKI
        if WIKI:
            return WIKI
        base_tiddlywiki = open(
            self.environ['tiddlyweb.config']['base_tiddlywikii'])
        wiki = base_tiddlywiki.read()
        base_tiddlywiki.close()
        tag = "<!--POST-SCRIPT-END-->"
        wiki = wiki.replace(tag, '''
        %(config)s
        <script type="text/javascript" src="%(host)s/bags/common/tiddlers/jquery.js"></script>
        <script type="text/javascript" src="%(host)s/bags/common/tiddlers/jQuery.twStylesheet.js"></script>
        <script type="text/javascript" src="%(host)s/bags/common/tiddlers/custom_twcore.js"></script>
        %(tag)s
        ''' % {"tag": tag, "config": self._get_config(), "host": server_base_url(self.environ)})
        wiki = unicode(wiki, 'utf-8')
        WIKI = wiki
        return WIKI
