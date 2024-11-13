# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Divide & Conque
class NewType:
    def __init__(self, lca = None,found_p = False, found_q = False):
        self.lca = lca
        self.found_p = found_p
        self.found_q = found_q

# Divide & Conquor
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.dfs(root, p, [])
        q_path = self.dfs(root, q, [])
        return self.find_lca(p, q, p_path, q_path)

    def dfs(self, root, target, subsets):
        if root is None:
            return []

        if root == target:
            return subsets[:] + [root]

        subsets.append(root)
        left = self.dfs(root.left, target, subsets[:])
        if left:
            return left

        right = self.dfs(root.right, target, subsets[:])

        if right:
            return right
        subsets.pop()

        return []

    def find_lca(self, p, q, p_path, q_path):
        lca = None
        if p_path == [] or q_path == []:
            return None

        if all(node in p_path for node in q_path):
            return q

        if all(node in q_path for node in p_path):
            return p

        for pnode, qnode in zip(p_path, q_path):
            if pnode == qnode:
                lca = pnode
            else:
                return lca


# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Divide & Conque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.num_found = 0
        parent = None
        def inorder(root, parent):
            if root is None:
                return

            root.parent = parent
            if root in [p, q]:
                self.num_found += 1
            if self.num_found == 2:
                return

            inorder(root.left, root)
            inorder(root.right, root)

        if root == None:
            return root

        inorder(root, None)
        if not hasattr(p, 'parent') or not hasattr(q, 'parent'):
            return None

        p_list, q_list = [], []
        pp, qq = p, q
        while pp:
            p_list.append(pp)
            pp = pp.parent
        while qq:
            q_list.append(qq)
            qq = qq.parent

        return self.find_lca(p_list[::-1], q_list[::-1], p, q)

    def find_lca(self, p_list, q_list, p, q):
        if all([node in p_list for node in q_list]):
            return q

        if all([node in q_list for node in p_list]):
            return p

        lca = None
        for pnode, qnode in zip(p_list, q_list):
            if pnode == qnode:
                lca = pnode
            else:
                break

        return lca
