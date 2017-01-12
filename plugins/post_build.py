from pelican import signals
import os
from plugins.utils import run_command


OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')


def post_build(*args, **kwargs):
    run_command('Copying Robots.txt', [
        'mv', os.path.join(OUTPUT_PATH, 'assets', 'robots.txt'), OUTPUT_PATH
    ])
    run_command('Copying Assets', [
        'cp', '-R', os.path.join(OUTPUT_PATH, 'assets', '*'), os.path.join(OUTPUT_PATH, 'static')
    ], True)
    run_command('Remove Old Assets', [
        'rm', '-rf', os.path.join(OUTPUT_PATH, 'assets')
    ])


def register():
    signals.finalized.connect(post_build)
