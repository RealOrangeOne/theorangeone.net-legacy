import os.path
import yaml


def generate_config(base_dir):
    default = yaml.load(open(os.path.join(base_dir, 'data/context.yml'))) or {}
    page = yaml.load(open(os.path.join(base_dir, 'data/page_context.yml'))) or {}
    return default, page
