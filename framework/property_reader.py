from jproperties import Properties


class PropertyReader:

    def get_property(self, path, key):
        configs = Properties()
        with open(path, 'rb') as read_prop:
            configs.load(read_prop)
        return configs[key].data


if __name__ == '__main__':
    prop = PropertyReader()
    print(prop.get_property('../resources/config.properties', 'base_url'))

