from pelican import signals
import os


OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'output')


def post_build(*args, **kwargs):
    os.system("mv {0}/assets/robots.txt {0}".format(OUTPUT_PATH))
    os.system("cp -R {0}/assets/* {0}/static".format(OUTPUT_PATH))
    os.system("rm -rf {0}/assets".format(OUTPUT_PATH))


def register():
    signals.finalized.connect(post_build)
