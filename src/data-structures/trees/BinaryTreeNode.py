from typing import Optional

class BinaryTreeNode:
    def __init__(self, val, left: Optional[BinaryTreeNode]=None,
                 right: Optional[BinaryTreeNode]=None):
        self.val = val
        self.left = left
        self.right = right


