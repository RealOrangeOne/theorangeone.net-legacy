from pelican import signals
from plugins.utils import node_bin, run_command, NODE_PRODUCTION
import logging

logger = logging.getLogger(__file__)


def static_build(*args, **kwargs):
    if NODE_PRODUCTION:
        logger.info('Building Production...')
        UGLIFY_ARGS = ['--compress', '--screw-ie8', '--define', '--stats', '--keep-fnames']
    else:
        UGLIFY_ARGS = []
    run_command('Copying Fonts', ['cp', '-r', 'node_modules/font-awesome/fonts', 'theme/static/build/'])
    run_command('Building Bootstrap', [node_bin('uglifyjs'), 'node_modules/bootstrap-sass/assets/javascripts/bootstrap.js', UGLIFY_ARGS, '-o', 'theme/static/build/js/bootstrap.js'])
    run_command('Building jQuery', [node_bin('uglifyjs'), 'node_modules/jquery/dist/jquery.js', UGLIFY_ARGS, '-o', 'theme/static/build/js/jquery.js'])
    run_command('Building Application', [
        node_bin('browserify'),
        'theme/static/src/js/app.js',
        '-o', 'theme/static/build/js/app.js'
    ])

    logger.info('JS built!')

    run_command('Building Pygments Style', ['pygmentize', '-S', 'github', '-f', 'html', '-a', '.highlight', '>', 'theme/static/src/scss/pygment.css'], True)
    run_command('Building Styles', [node_bin('node-sass'), 'theme/static/src/scss/index.scss', 'theme/static/build/css/index.css', '--source-map-embed'])

    logger.info('SCSS Built!')

    if NODE_PRODUCTION:
        run_command('Compressing Application', [node_bin('uglifyjs'), 'theme/static/build/js/app.js', UGLIFY_ARGS, '-o', 'theme/static/build/js/app.js'])
        run_command('Prefixing Styles', [node_bin('postcss'), '-u', 'autoprefixer', '-o', 'theme/static/build/css/index.css', 'theme/static/build/css/index.css'])
        run_command('Compressing Styles', [node_bin('cleancss'), '-d', '--s0', '-o', 'theme/static/build/css/index.css', 'theme/static/build/css/index.css'])


def register():
    signals.static_generator_init.connect(static_build)
