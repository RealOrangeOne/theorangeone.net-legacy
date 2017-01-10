from pelican import signals
import os


def static_build(*args, **kwargs):
    os.system('npm run build-js')
    os.system('npm run build-scss')


def register():
    signals.static_generator_init.connect(static_build)
