import yaml
import os.path


settings_dir = os.path.dirname(__file__)


def get_config(filename):
    with open(os.path.join(settings_dir, '{}.yml'.format(filename))) as f:
        return yaml.safe_load(f)


social = get_config('social')
