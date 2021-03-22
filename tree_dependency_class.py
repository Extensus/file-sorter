class dependency(object):
    def __init__(self, data):
        self.data = data
        self.dir = None
        self.ext = None


class mapper_tree(object):
    def __init__(self, mapping_bool):
        self.root = dependency(mapping_bool)
    def x(self):
        pass


if __name__ == '__main__':
    mapper_tree(1)
    dependency(2)
