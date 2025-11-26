from BinaryTreeNode import BinaryTreeNode

"""
red black trees have O(log(n)) insertion, deletion, lookups and rearrangements
add fix step to insert method
    - check state of tree
      - if unbalanced: rotate (fold longer branch back into tree)
    - red and black are booleans attached to each node that denote balance
    - root is black
    - all Nil leaf nodes are black
    - if a node is red then both its children must be black
    - all paths from a node to any descendant nil node must go through
      the same number of black nodes
Consider left rotation:
    2 <= pivot's parent
1       4 <= pivot
     3     5
     update pivot.left to now point to parent node
     orphaned left child becomes right child of old parent

     Rotation:
         - when a branch starts to get too long, rotate those branches to keep
         the tree shallow. 
         - rotation does not invalidate order
         - left rotation:
             - initial pivot-parent becomes it's left child
             - pivot node old left child becomes it's initial parent's right
               child
             - old left child becomes new left child's new right child
"""


class RedBlackNode(BinaryTreeNode):
    def __init__(self, val):
        super().__init__(val)
        self.red = False
        self.parent = None

    def __repr__(self):
        return (
            (
                "TreeNode {"
                + f"val: {self.val}, \n\tleft: {self.left}, \n\tright: {self.right}"
                + "}"
            )
            if self.val is not None
            else "None"
        )


class RedBlackTree:
    def __init__(self):
        self.nil = RedBlackNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def __repr__(self):
        return str(self.root)

    def rotate_left(self, pivot_parent: RedBlackNode):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            old_left = pivot.left
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RedBlackNode):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            old_right = pivot.right
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def insert(self, val):
        """Insert val into tree if val is not already in tree"""
        new_node = RedBlackNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root

        while current is not self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        elif new_node.val > parent.val:
            parent.right = new_node
        self.fix_insert(new_node)

    def fix_insert(self, new_node: RedBlackNode):
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent
            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node is parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
            if parent is grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node is parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
        self.root.red = False


if __name__ == "__main__":
    rb_tree = RedBlackTree()
    print("Empty tree: ")
    print(rb_tree)
    rb_tree.insert(1)
    print("Added 1")
    print(rb_tree)
    rb_tree.insert(2)
    print("Added 2")
    print(rb_tree)
    rb_tree.insert(3)
    print("Added 3")
    print(rb_tree)
    rb_tree.insert(4)
    print("Added 4")
    print(rb_tree)

"""
output:
1 None None
"""
