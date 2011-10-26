"""
structure and contents of a default TiddlyWebWiki instance
"""

store_contents = {}

instance_config = {
    'system_plugins': ['tiddlywebplugins.tiddlywebwikii'],
    'twanager_plugins': ['tiddlywebplugins.tiddlywebwikii']
}

store_contents['common'] = [
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
        }
    }
}
