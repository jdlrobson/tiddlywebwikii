tiddlywiki:
	mkdir tiddlywebplugins/tiddlywebwikii/resources || true
	wget http://jonrobson.me.uk/tiddlywebwiki/tiddlywiki.html -O tiddlywebplugins/tiddlywebwikii/resources/empty.html

remotes: tiddlywiki
	./cacher

dev: remotes
	./twiinstance dev_instance
	cd dev_instance && ln -s ../tiddlywebplugins .

clean:
	rm -rf tiddlywebplugins/tiddlywebwikii/resources
	rm -rf dev_instance