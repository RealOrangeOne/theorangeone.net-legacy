from pelican import signals
import os
import sh

NODE_PRODUCTION = os.environ.get('NODE_ENV') == 'production'

def static_build(*args, **kwargs):
    if NODE_PRODUCTION:
        print('Building Production...')

    sh.mkdir('-p', 'theme/static/build/js/lib')
    os.system('uglifyjs node_modules/bootstrap-sass/assets/javascripts/bootstrap.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/lib/bootstrap.js')
    os.system('uglifyjs theme/static/build/js/lib/* --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/libs.js')
    sh.rm('-rf', 'theme/static/build/js/lib')
    os.system('uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/jquery.js')
    os.system('browserify -t [ babelify --presets [ es2015 react ] ] theme/static/src/js/app.js -o theme/static/build/js/app.js')
    os.system('uglifyjs theme/static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o theme/static/build/js/app.js')
    print('JS built!')

    os.system('pygmentize -S github -f html -a .highlight > theme/static/src/scss/pygment.css')
    os.system('npm run build-scss')
    os.system('node-sass theme/static/src/scss/index.scss theme/static/build/css/index.css --source-map-embed')
    os.system('postcss -u autoprefixer -o theme/static/build/css/index.css theme/static/build/css/index.css')
    os.system('cleancss -d --s0 -o theme/static/build/css/index.css theme/static/build/css/index.css')
    print('SCSS Built!')

def register():
    signals.static_generator_init.connect(static_build)
