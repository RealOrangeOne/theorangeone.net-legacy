import os.path
import yaml
from glob import glob
from project.pages.utils import get_title_from_markdown, parse_content


def get_data_from_file(base_dir, filename):
    with open(os.path.join(base_dir, 'data', filename)) as data_file:
        return yaml.load(data_file) or {}


def generate_config(base_dir):
    default = get_data_from_file(base_dir, 'context.yml')
    page = get_data_from_file(base_dir, 'page_context.yml')
    switcher = get_data_from_file(base_dir, 'path_switch.yml')

    # Add projects config
    default['projects'] = generate_projects(base_dir)
    # Join projects config with it's page context
    for i in range(len(default['projects'])):
        project = default['projects'][i]
        if project['path'] in page:  # If there's a custom config
            default['projects'][i] = dict(project, **page[project['path']])

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
                "path": 'projects' + path.replace(projects_path, '').split('.')[0],
                "url": '/projects' + path.replace(projects_path, '').split('.')[0],
            })
    return files
