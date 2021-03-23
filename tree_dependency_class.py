class dependency(object):       # creates Nodes in Tree
    def __init__(self, data):
        self.data = data    # file mapping boolean
        self.dir = None     # directory according to map
        self.ext = None     # extension according to directory


class mapper_tree(object):
    def __init__(self, mapping_bool):       # creates root with class function
        self.root = dependency(mapping_bool)

    def print_tree(self, traversal_type):       # how to print out the tree
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):     # prints root then from left to right
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):      # prints from left to right
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):        # prints from left to right and then the root node
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


if __name__ == '__main__':
    tree = mapper_tree(1)
    tree.ext = dependency(2)
