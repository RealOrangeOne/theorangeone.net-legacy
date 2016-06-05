ENV=env/bin
NODE_BIN=node_modules/.bin
PELICAN=$(ENV)/pelican

BASEDIR=$(PWD)
OUTPUTDIR=$(BASEDIR)/output

FLAKE8_IGNORE=--ignore=E128,E501,E401,E402

build: install
	@echo ">> Building static data..."
	mkdir -p theme/static/build/js/lib theme/static/build/fonts theme/static/build/css
	cp -R node_modules/font-awesome/fonts theme/static/build/
	npm run build-js
	npm run build-scss
	@echo ">> Building pelican..."
	$(PELICAN) -o $(OUTPUTDIR) -v

clean:
	rm -rf $(OUTPUTDIR)/*
	rm -rf $(BASEDIR)/env/
	rm -rf $(BASEDIR)/node_modules/
	rm -rf $(BASEDIR)/pelican_plugins/


install: env node_modules pelican_plugins

pelican_plugins:
	git clone --recursive https://github.com/getpelican/pelican-plugins --depth=1 pelican_plugins/
	@echo ">> Hotfixing..."
	rm -rf pelican_plugins/pelican-jinja2content
	git clone https://github.com/RealOrangeOne/pelican-jinja2content -b patch-1 --depth=1 pelican_plugins/pelican-jinja2content

env:
	pyvenv env
	$(ENV)/pip install -r requirements.txt

node_modules:
	@source ~/.nvm/nvm.sh && nvm install
	npm install


test: lint

lint:
	$(NODE_BIN)/eslint 'theme/static/src/js/'
	$(NODE_BIN)/sass-lint -vqc .sass-lint.yml
	$(ENV)/flake8 $(BASEDIR)/plugins/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/scripts/ $(FLAKE8_IGNORE)
	$(ENV)/flake8 $(BASEDIR)/pelicanconf.py $(FLAKE8_IGNORE)


.PHONY: build clean test lint install
