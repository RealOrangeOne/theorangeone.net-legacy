import yaml
import os.path


class DotDictionary(dict):
    def __getattr__(self, attr):
        value = self[attr]
        if type(value) == dict:
            value = DotDictionary(value)
        return value
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class WrappedSettings:
    def __init__(self):
        self.settings_dir = os.path.join(os.path.dirname(__file__), 'config.yml')
        settings = open(self.settings_dir)
        self.settings = yaml.load(settings)

    def __getattr__(self, name):
        value = getattr(self.settings, name)
        if type(value) == dict:
            value = DotDictionary(value)
        return value

    def __str__(self):
        return str(self.settings)

settings = WrappedSettings()
