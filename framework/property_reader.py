from jproperties import Properties


class PropertyReader:
    @staticmethod
    def get_property(path, key):
        configs = Properties()
        with open(path, 'rb') as read_prop:
            configs.load(read_prop)
        return configs[key].data
