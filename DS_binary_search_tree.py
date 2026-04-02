# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        def delete_node(prev, curr):
            """
            10
            4           13
            2    7      14   15
                 6  8

            delete 4
            10
            6           13
            2    7      14   15
                    8
            """
            nonlocal root

            if curr.left is None or curr.right is None:
                child = curr.left if curr.left else curr.right

                if prev is None:
                    root = child
                else:
                    if prev.left == curr:
                        prev.left = child
                    else:
                        prev.right = child
                return root

            # two child case
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left

            # delete successor
            curr.val = succ.val
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

            return root

        found = False
        prev, curr = None, root
        while curr is not None:
            if curr.val == key:
                found = True
                root_updated = delete_node(prev, curr)
                return root_updated
            elif curr.val > key:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        return root
