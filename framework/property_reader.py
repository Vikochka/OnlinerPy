import os

from jproperties import Properties


class PropertyReader:
    dir = os.path.dirname(__file__)

    def get_property(self, path, key):
        filename = os.path.join(self.dir, path)
        configs = Properties()
        with open(filename, 'rb') as read_prop:
            configs.load(read_prop)
        return configs[key].data
