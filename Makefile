NODE_BIN=node_modules/.bin
PELICAN=pelican

BASEDIR=$(PWD)
OUTPUTDIR=$(BASEDIR)/output
PLUGINS_DIR=$(BASEDIR)/pelican_plugins

SSH_USER=web
SSH_HOST=theorangeone.net
SSH_TARGET_DIR=/home/web/v4-theorangeone.net/site  # Dev path only!

FLAKE8_IGNORE=--ignore=E128,E501,E401,E402

build: install
	rm -rf $(OUTPUTDIR)/*
	@echo ">> Building static data..."
	mkdir -p theme/static/build/js/lib theme/static/build/fonts theme/static/build/css
	cp -R node_modules/font-awesome/fonts theme/static/build/
	npm run build-js
	npm run build-scss
	@echo ">> Building pelican..."
	$(PELICAN) -o $(OUTPUTDIR) -v
	mv $(OUTPUTDIR)/assets/robots.txt $(OUTPUTDIR)
	cp -R $(OUTPUTDIR)/assets/* $(OUTPUTDIR)/static
	rm -rf $(OUTPUTDIR)/assets

clean:
	rm -rf $(OUTPUTDIR)/*
	rm -rf $(BASEDIR)/env/
	rm -rf $(BASEDIR)/node_modules/
	rm -rf $(PLUGINS_DIR)/*


install: node_modules pelican_plugins

pelican_plugins:
	rm -rf $(PLUGINS_DIR) || "No existing extensions"
	git clone --recursive https://github.com/getpelican/pelican-plugins $(PLUGINS_DIR) || "Git Fail"
	@echo ">> Hotfixing..."
	rm -rf $(PLUGINS_DIR)/pelican-jinja2content
	git clone https://github.com/RealOrangeOne/pelican-jinja2content -b patch-1 --depth=1 $(PLUGINS_DIR)/pelican-jinja2content

env:
	pyvenv env
	pip install -r requirements.txt

node_modules:
	npm install


test: lint spellcheck

lint:
	$(NODE_BIN)/eslint 'theme/static/src/js/'
	$(NODE_BIN)/sass-lint -vqc .sass-lint.yml
	flake8 $(BASEDIR)/plugins/ $(FLAKE8_IGNORE)
	flake8 $(BASEDIR)/scripts/ $(FLAKE8_IGNORE)
	flake8 $(BASEDIR)/pelicanconf.py $(FLAKE8_IGNORE)

spellcheck:
	$(NODE_BIN)/mdspell --en-gb -ranx theme/templates/**/*.* theme/templates/*.*
	$(NODE_BIN)/mdspell --en-gb -ranx content/**/*.* content/*.*


upload: build
	rsync -e "/usr/bin/ssh" -rvz --delete $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)


.PHONY: build clean test lint install upload
