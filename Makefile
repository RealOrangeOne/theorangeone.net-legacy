BASEDIR=$(PWD)
ENV=$(BASEDIR)/env/bin
NODE_BIN=node_modules/.bin
PELICAN=$(ENV)/pelican

OUTPUTDIR=$(BASEDIR)/output
PLUGINS_DIR=$(BASEDIR)/pelican_plugins
DEPLOY_DIR=$(BASEDIR)/deploy
CONFIG_FILE=$(BASEDIR)/config/pelicanconf.py

FLAKE8_IGNORE=--ignore=E128,E501,E401,E402

build: install
	rm -rf $(OUTPUTDIR)/*
	@echo ">> Building static data..."
	mkdir -p theme/static/build/js/lib theme/static/build/fonts theme/static/build/css theme/static/build/img
	cp -R node_modules/font-awesome/fonts theme/static/build/
	npm run build-js
	npm run build-scss
	@echo ">> Building pelican..."
	$(PELICAN) -o $(OUTPUTDIR) -vs $(CONFIG_FILE)
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
	git clone --recursive https://github.com/getpelican/pelican-plugins $(PLUGINS_DIR) || "Git Fail"
	@echo ">> Hotfixing..."
	rm -rf $(PLUGINS_DIR)/pelican-jinja2content
	git clone https://github.com/RealOrangeOne/pelican-jinja2content -b patch-1 --depth=1 $(PLUGINS_DIR)/pelican-jinja2content

env:
	pyvenv env
	$(ENV)/pip install -r requirements.txt

node_modules:
	npm install


test: unittest lint spellcheck securitycheck

unittest:
	$(ENV)/nose2 --verbose

lint:
	$(NODE_BIN)/eslint 'theme/static/src/js/'
	$(NODE_BIN)/sass-lint -vqc .sass-lint.yml
	$(ENV)/flake8 $(BASEDIR)/plugins/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/scripts/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/config/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/tests/ $(FLAKE8_IGNORE)
	$(ENV)/yamllint config/config.yml

spellcheck:
	$(NODE_BIN)/mdspell --en-gb -ranx theme/templates/**/*.* theme/templates/*.*
	$(NODE_BIN)/mdspell --en-gb -ranx content/**/*.md content/*.md content/**/*.html content/*.html

securitycheck:
	$(NODE_BIN)/nsp check
	$(ENV)/bandit -r plugins/ config/ tests/


upload:
	git clone https://github.com/RealOrangeOne/host-container.git $(DEPLOY_DIR)
	cp -rf $(OUTPUTDIR)/. $(DEPLOY_DIR)/site/
	@cd $(DEPLOY_DIR) && git remote add dokku $(DEPLOY_URL) && git add . && git commit -m "add files" && git push -f dokku master --quiet
	rm -rf $(DEPLOY_DIR)


.PHONY: build clean test lint install upload
