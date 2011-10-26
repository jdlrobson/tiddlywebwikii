from tiddlywebplugins.instancer.util import get_tiddler_locations
from tiddlywebplugins.tiddlywebwikii.instance import store_contents

try:
    from pkg_resources import resource_filename
except ImportError:
    from tiddlywebplugins.utils import resource_filename

PACKAGE_NAME = 'tiddlywebplugins.tiddlywebwikii'
BASE_TIDDLYWIKII = resource_filename(PACKAGE_NAME, 'resources/empty.html')

config = {
        'instance_tiddlers': get_tiddler_locations(store_contents, PACKAGE_NAME),
        'base_tiddlywikii': BASE_TIDDLYWIKII,
        'extension_types': {
            'wikii': 'text/x-tiddlywikii',
            },
        'serializers': {
            'text/x-tiddlywikii': ['tiddlywebplugins.tiddlywebwikii.serialization',
                'text/html; charset=UTF-8'],
            },
        }
