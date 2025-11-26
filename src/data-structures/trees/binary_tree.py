from typing import Optional
from math import inf


class BinarySearchTreeNode:
    """
    Constraints:
        - each node has at most 2 children
        - left child value must be LESS than parent
        - right child must be GREATER than parent
        - No two nodes in the BST can have the same value

    Operations:
        - Add
        - Remove
        - Find
        - Update
    """

    def __init__(
        self,
        val=None,
        left: Optional[BinarySearchTreeNode] = None,
        right: Optional[BinarySearchTreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if not self.right:
            return self.left
        if not self.left:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self
            

    def get_min(self):
        if self.left is None:
            return self.val
        return self.left.get_min()

    def get_max(self):
        curr = self
        while curr.right:
            curr = curr.right
        return curr.val

    def insert(self, val):
        if self.val is None or self.val == val:
            self.val = val
            return
        if val < self.val:
            if self.left is None:
                self.left = BinarySearchTreeNode(val)
                return
            self.left.insert(val)
            return
        if self.right is None:
            self.right = BinarySearchTreeNode(val)
            return
        self.right.insert(val)

    def postorder(self,
                 visited: Optional[list[BinarySearchTreeNode]]=None) -> [list[BinarySearchTreeNode]]:
        if visited is None:
            visited = []
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def preorder(self,
                 visited: Optional[list[BinarySearchTreeNode]]=None) -> [list[BinarySearchTreeNode]]:
        if visited is None:
            visited = []
        visited.append(self.val)
        if self.left is not None:
            self.left.preorder(visited)
        if self.right is not None:
            self.right.preorder(visited)
        return visited

    def inorder(self,
                 visited: Optional[list[BinarySearchTreeNode]]=None) -> [list[BinarySearchTreeNode]]:
        if visited is None:
            visited = []
        if self.left is not None:
            visited = self.left.inorder(visited)
        visited.append(self.val)
        if self.right is not None:
            visited = self.right.inorder(visited)
        return visited

    def exists(self, val) -> bool:
        if self.val == val:
            return True
        if self.val > val and self.left:
                return self.left.exists(val)
        if self.val < val and self.right:
            return self.right.exists(val)
        return False

    def __repr__(self):
        return (
            "TreeNode {"
            + f"val: {self.val}, left: {self.left}, right: {self.right}"
            + "}"
        )


if __name__ == "__main__":
    tree = BinarySearchTreeNode()
    tree.insert(4)
    print(tree)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(6)
    print(tree)
    print(".")
    print(tree)
    print(".")
    print(tree.preorder())
    print(tree.postorder())
    print(tree.inorder())
    print(tree.exists(7))
    print(tree.exists(11))
    print(tree.exists(6))
