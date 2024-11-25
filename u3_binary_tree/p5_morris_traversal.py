# Time O(N), Space O(1) (no recursion): preorder/inorder/postorder traversal
# Morris Order
# key point: set a pointer from the 'most right of the left subtree' back to the root at 1st visit, set it back at 2nd visit,
# go through 'root -> left -> root -> right' order.
# If a root has left subtree then it will be visited twice.
from utils.trees import TreeNode


def morris_order(rt: TreeNode):
