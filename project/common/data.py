import os.path
import yaml
from glob import glob
from project.pages.utils import get_title_from_markdown, parse_content


def generate_config(base_dir):
    default = yaml.load(open(os.path.join(base_dir, 'data/context.yml'))) or {}
    page = yaml.load(open(os.path.join(base_dir, 'data/page_context.yml'))) or {}
    switcher = yaml.load(open(os.path.join(base_dir, 'data/path_switch.yml'))) or {}

    default['projects'] = generate_projects(base_dir)
    for i in range(len(default['projects'])):
        project = default['projects'][i]
        if project['path'] in page:  # If there's a custom config
            default['projects'][i] = dict(project, **page[project['path']])
            default['projects'][i]['url'] = '/' + project['path']
    return default, page, switcher


def generate_projects(base_dir):
    projects_path = os.path.join(base_dir, 'templates/projects')
    files = []
    for path in glob(projects_path + '/*.*'):
        filename = path.replace(projects_path, '')
        if filename == '/all.html':
            continue
        with open(path) as f:
            if filename.split('.')[1] == 'md':
                parsed_content = parse_content(f.read(), filename.split('.')[1])
                filename = get_title_from_markdown(parsed_content)
            else:
                filename = filename.split('.')[0]
            files.append({
                "name": filename,
                "path": 'projects' + path.replace(projects_path, '').split('.')[0]
            })
    return files
