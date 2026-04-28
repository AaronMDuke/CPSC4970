import unittest



class BinaryTreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.parent = None
        self._left_child = left_child
        self._right_child = right_child
        if left_child:
            left_child.parent = self
        if right_child:
            right_child.parent = self


    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child



class BinaryTree:
    def __init__(self, root=None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    def __iter__(self):
        return InOrderIterator(self)



class PreOrderIterator:
    def __init__(self, tree):
        self._values = []
        self._collect(tree.root)
        self._index = 0

    def _collect(self, node):
        if node is None:
            return
        self._values.append(node.value)
        self._collect(node.left_child)
        self._collect(node.right_child)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value



class InOrderIterator:
    def __init__(self, tree):
        self._values = []
        self._collect(tree.root)
        self._index = 0

    def _collect(self, node):
        if node is None:
            return
        self._collect(node.left_child)
        self._values.append(node.value)
        self._collect(node.right_child)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value


class PostOrderIterator:
    def __init__(self, tree):
        self._values = []
        self._collect(tree.root)
        self._index = 0

    def _collect(self, node):
        if node is None:
            return
        self._collect(node.left_child)
        self._collect(node.right_child)
        self._values.append(node.value)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value



def build_tree():
        n1 = BinaryTreeNode("A")
        n2 = BinaryTreeNode("B")
        n3 = BinaryTreeNode("C", n1, n2)
        n4 = BinaryTreeNode("D")
        n5 = BinaryTreeNode("E", n4, n3)
        n6 = BinaryTreeNode("F", n5)
        n7 = BinaryTreeNode("G")
        n8 = BinaryTreeNode("H", n6, n7)
        return BinaryTree(n8)




class TestPreOrderIterator(unittest.TestCase):
    def test_build_tree(self):
        tree = build_tree()
        result = list(PreOrderIterator(tree))
        self.assertEqual(result, ["H", "F", "E", "D", "C", "A", "B", "G"])

    def test_single_node(self):
        tree = BinaryTree(BinaryTreeNode("A"))
        self.assertEqual(list(PreOrderIterator(tree)), ["A"])

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertEqual(list(PreOrderIterator(tree)), [])



class TestInOrderIterator(unittest.TestCase):
    def test_build_tree(self):
        tree = build_tree()
        result = list(InOrderIterator(tree))
        self.assertEqual(result, ["D", "E", "A", "C", "B", "F", "H", "G"])

    def test_single_node(self):
        tree = BinaryTree(BinaryTreeNode("A"))
        self.assertEqual(list(InOrderIterator(tree)), ["A"])

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertEqual(list(InOrderIterator(tree)), [])

    def test_for_loop(self):
        tree = build_tree()
        result = [value for value in tree]
        self.assertEqual(result, ["D", "E", "A", "C", "B", "F", "H", "G"])



class TestPostOrderIterator(unittest.TestCase):
    def test_build_tree(self):
        tree = build_tree()
        result = list(PostOrderIterator(tree))
        self.assertEqual(result, ["D", "A", "B", "C", "E", "F", "G", "H"])

    def test_single_node(self):
        tree = BinaryTree(BinaryTreeNode("A"))
        self.assertEqual(list(PostOrderIterator(tree)), ["A"])

    def test_empty_tree(self):
        tree = BinaryTree()
        self.assertEqual(list(PostOrderIterator(tree)), [])



if __name__ == "__main__":
    tree = build_tree()
    unittest.main()


