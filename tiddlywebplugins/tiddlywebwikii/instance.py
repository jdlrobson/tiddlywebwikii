"""
structure and contents of a default TiddlyWebWiki instance
"""

store_contents = {}

instance_config = {
    'system_plugins': ['tiddlywebplugins.tiddlywebwikii'],
    'twanager_plugins': ['tiddlywebplugins.tiddlywebwikii']
}

store_contents['lib'] = [
    'http://jonrobson.me.uk/tiddlywebwiki/index.recipe'
]

store_structure = {
    'bags': {
        'common': {
            'desc': 'shared content',
            'policy': {
                'manage': ['R:ADMIN'],
                'owner': 'administrator'
            }
        },
        'lib': {
            'desc': 'TiddlyWebWiki client plugins',
            'policy': {
                'read': [],
                'write': ['R:ADMIN'],
                'create': ['R:ADMIN'],
                'delete': ['R:ADMIN'],
                'manage': ['R:ADMIN'],
                'accept': ['R:ADMIN'],
                'owner': 'administrator'
            }
        },
    }
}
