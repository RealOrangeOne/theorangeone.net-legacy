ENV=env/bin
NODE_BIN=node_modules/.bin
PELICAN=$(ENV)/pelican

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


install: env node_modules pelican_plugins

pelican_plugins: env
	rm -rf $(PLUGINS_DIR) || "No existing extensions"
	git clone --recursive https://github.com/getpelican/pelican-plugins --depth=10 $(PLUGINS_DIR) || "Git Fail"
	@echo ">> Hotfixing..."
	rm -rf $(PLUGINS_DIR)/pelican-jinja2content
	git clone https://github.com/RealOrangeOne/pelican-jinja2content -b patch-1 --depth=1 $(PLUGINS_DIR)/pelican-jinja2content
	rm -rf $(PLUGINS_DIR)/ace_editor/static/ace-build
	git clone https://github.com/ajaxorg/ace-builds --depth=1 $(PLUGINS_DIR)/ace_editor/static/ace-build  --recursive  # Fix because reasons I don't quite understand

env:
	pyvenv env
	$(ENV)/pip install -r requirements.txt

node_modules: env
	npm install


test: lint

lint:
	$(NODE_BIN)/eslint 'theme/static/src/js/'
	$(NODE_BIN)/sass-lint -vqc .sass-lint.yml
	$(ENV)/flake8 $(BASEDIR)/plugins/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/scripts/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/pelicanconf.py $(FLAKE8_IGNORE)


upload: build
	rsync -e "/usr/bin/ssh" -rvz --delete $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)


.PHONY: build clean test lint install upload
