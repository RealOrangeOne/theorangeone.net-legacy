from pelican import signals
import os
import subprocess
import logging

logger = logging.getLogger(__file__)

NODE_PRODUCTION = os.environ.get('NODE_ENV') == 'production'


def flatten_list(array):
    res = []
    for el in array:
        if isinstance(el, (list, tuple)):
            res.extend(flatten_list(el))
            continue
        res.append(el)
    return res


def run_command(detail, args, use_system=False):
    logger.info(detail + '...')
    if use_system:
        exit_code = os.system(' '.join(flatten_list(args)))
        if exit_code:
            exit(exit_code)
    else:
        subprocess.run(flatten_list(args), check=True)


def node_bin(exec):
    return os.path.join('node_modules', '.bin', exec)


def static_build(*args, **kwargs):
    if NODE_PRODUCTION:
        logger.info('Building Production...')
        UGLIFY_ARGS = ['--compress', '--screw-ie8', '--define', '--stats', '--keep-fnames']
    else:
        UGLIFY_ARGS = []

    run_command('Building Bootstrap', [node_bin('uglifyjs'), 'node_modules/bootstrap-sass/assets/javascripts/bootstrap.js', UGLIFY_ARGS , '-o', 'theme/static/build/js/bootstrap.js'])
    run_command('Building jQuery', [node_bin('uglifyjs'), 'node_modules/jquery/dist/jquery.js', UGLIFY_ARGS, '-o', 'theme/static/build/js/jquery.js'])
    run_command('Building Application', [
        node_bin('browserify'),
        '-t', '[', 'babelify', '--presets', '[', 'es2015', 'react', ']', ']',
        'theme/static/src/js/app.js',
        '-o', 'theme/static/build/js/app.js'
    ])
    run_command('Compressing Application', [node_bin('uglifyjs'), 'theme/static/build/js/app.js', UGLIFY_ARGS, '-o', 'theme/static/build/js/app.js'])

    logger.info('JS built!')

    run_command('Building Pygments Style', ['pygmentize', '-S', 'github', '-f', 'html', '-a', '.highlight', '>', 'theme/static/src/scss/pygment.css'], True)
    run_command('Building Styles', [node_bin('node-sass'), 'theme/static/src/scss/index.scss', 'theme/static/build/css/index.css', '--source-map-embed'])
    run_command('Prefixing Styles', [node_bin('postcss'), '-u', 'autoprefixer', '-o', 'theme/static/build/css/index.css', 'theme/static/build/css/index.css'])
    run_command('Compressing Styles', [node_bin('cleancss'), '-d', '--s0', '-o', 'theme/static/build/css/index.css', 'theme/static/build/css/index.css'])

    logger.info('SCSS Built!')


def register():
    signals.static_generator_init.connect(static_build)
