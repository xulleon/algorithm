# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Traversal Solution 1: add a parent node on each node.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q, None, 0)
        p_list, q_list = [], []
        p_tmp, q_tmp = p, q
        while p_tmp:
            p_list.append(p_tmp)
            p_tmp = p_tmp.parent
        while q_tmp:
            q_list.append(q_tmp)
            q_tmp = q_tmp.parent

        return self.find_lca(p_list[::-1], q_list[::-1], p, q)


    def dfs(self, root, p, q, parent, num_found):
        if root is None:
            return

        if num_found > 1:
            return

        if root in [p, q]:
            num_found += 1

        root.parent = parent
        self.dfs(root.left, p, q, root, num_found)
        self.dfs(root.right, p, q, root, num_found)


    def find_lca(self, p_list, q_list, p, q):
        if all(x in p_list for x in q_list):
            return q

        if all(x in q_list for x in p_list):
            return p

        lca = None
        for pnode, qnode in zip(p_list, q_list):
            if pnode == qnode:
                lca = pnode
            else:
                break
        return lca

# # Traversal Solution 2: strict preorder traverdal
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p == root or q == root:
            return root

        if p is None:
            return q

        if q is None:
            return p

        results = {}
        self.dfs(root, p, q, [], results)
        return self.get_lca(results, p, q)

    def dfs(self, root, p, q, subsets, results):
        if root is None:
            return

        if root == p:
            results[p] = subsets[:] + [root]

        if root == q:
            results[q] = subsets[:] + [root]

        if p in results and q in results:
            return

        subsets.append(root)
        self.dfs(root.left, p, q, subsets[:], results)
        self.dfs(root.right, p, q, subsets[:], results)
        subsets.pop()

    def get_lca(self, results, p, q):

        p_list = results[p]
        q_list = results[q]

        if all(x in p_list for x in q_list):
            return q

        if all(x in q_list for x in p_list):
            return p

        lca = None
        for pnode, qnode in zip(p_list, q_list):
            if pnode == qnode:
                lca = pnode
            else:
                break
        return lca


# Recursive Solution 2: use preorder to find paths and find the last common path to be a LCA.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or p == root or q == root:
            return root

        if p == None and q == None:
            return None

        if p == None:
            return q

        if q == None:
            return p


        results = {}
        self.dfs(root, p, q, [], results)
        return self.common_ancestor(p, q, results)

    def dfs(self, root, p, q, subsets, results):
        if root is None:
            return

        if root == p:
            # Recursive is from top to bottom.
            results[p] = subsets[:] + [root]

        if root == q:
            # Recursive is from top to bottom.
            results[q] = subsets[:] + [root]

        if p in results and q in results:
            return

        subsets.append(root)
        self.dfs(root.left, p, q, subsets[:], results)
        self.dfs(root.right, p, q, subsets[:], results)
        subsets.pop()

    def common_ancestor(self, p, q, results):
        p_list = results[p]
        q_list = results[q]
        lca = None
        if all([x in p_list for x in q_list]):
            return q

        if all([x in q_list for x in p_list]):
            return p

        for p_node, q_node in zip(p_list, q_list):
            if p_node == q_node:
                lca = p_node
            else:
                break

        return lca


# Divided & Conque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if root is None or p == root or q == root:
            return root


        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

