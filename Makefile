tiddlywiki:
	mkdir tiddlywebplugins/tiddlywebwikii/resources || true
	wget https://raw.github.com/tiddlyweb/tiddlywiki/custombuild/twebwiki-release/latest/tiddlywiki.html -O tiddlywebplugins/tiddlywebwikii/resources/empty.html

remotes: tiddlywiki
	./cacher

dev: remotes
	./twiinstance dev_instance
	cd dev_instance && ln -s ../tiddlywebplugins .

clean:
	rm -rf tiddlywebplugins/tiddlywebwikii/resources
	rm -rf dev_instance