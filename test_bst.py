from bst import BST

def test_empty():
    tree = BST()
    assert tree.size() == 0

def test_size():
    my_tree = BST()
    my_tree.add(3)
    assert my_tree.size() == 1