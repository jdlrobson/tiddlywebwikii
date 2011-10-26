from setuptools import setup, find_packages

setup(
    name = 'tiddlywebwikii',
    version = '0.2.0',
    description = 'A TiddlyWeb plugin to provide a multi-user TiddlyWiki environment.',
    author = 'Jon Robson',
    author_email = 'jdlrobson@gmail.com',
    platforms = 'Posix; MacOS X; Windows',
    scripts = ['twiinstance'],
    packages = find_packages(exclude=['test']),
    install_requires = [
        'tiddlyweb>=1.2.43',
        'tiddlywebwiki',
        'simplejson'],
    include_package_data = True,
    zip_safe = False
    )
