BASEDIR=$(PWD)
ENV=$(BASEDIR)/env/bin
NODE_BIN=node_modules/.bin
PELICAN=$(ENV)/pelican

OUTPUTDIR=$(BASEDIR)/output
PLUGINS_DIR=$(BASEDIR)/pelican_plugins
DEPLOY_DIR=$(BASEDIR)/deploy
CONFIG_FILE=$(BASEDIR)/pelicanconf.py

build: install
	rm -rf $(OUTPUTDIR)/*
	@echo ">> Building pelican..."
	$(PELICAN) -o $(OUTPUTDIR) -vs $(CONFIG_FILE)
	mv $(OUTPUTDIR)/assets/robots.txt $(OUTPUTDIR)
	cp -R $(OUTPUTDIR)/assets/* $(OUTPUTDIR)/static
	rm -rf $(OUTPUTDIR)/assets


install: env node_modules
