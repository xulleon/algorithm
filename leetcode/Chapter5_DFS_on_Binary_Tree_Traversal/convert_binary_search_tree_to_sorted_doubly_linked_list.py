# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# Solution One: Iteration one (Simple Iteration, get_nodes_iteration1)
# Runtime: 77 ms, faster than 11.77% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.


# Solution Two: Iteration Two (Standard Iteration, get_nodes_iteration2)
# Runtime: 72 ms, faster than 21.65% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.

# Solution 3: DFS (get_nodes_dfs)
# Runtime: 68 ms, faster than 28.06% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None

        def get_nodes_iteration1(root):
            queue = []
            while root or queue:
                while root:
                    queue.append(root)
                    root = root.left

                root = queue.pop()
                res.append(root)
                root = root.right

        def get_nodes_iteration2(root):
            queue = []
            while root:
                queue.append(root)
                root = root.left

            while queue:
                node = queue[-1]
                res.append(node)
                if node.right:
                    node = node.right
                    while node:
                        queue.append(node)
                        node = node.left
                else:
                    node = queue.pop()
                    while queue and queue[-1].right == node:
                        node = queue.pop()




        def get_nodes_dfs(root):
            if root == None:
                return
            get_nodes_dfs(root.left)
            res.append(root)
            get_nodes_dfs(root.right)



        res = []
        get_nodes_iteration2(root)
        #get_nodes_dfs(root)

        head = TreeNode(0)
        n = len(res)
        for i in range(n):
            if i == 0:
                head.right = res[0]
                pre_node = res[0]
                if n == 1:
                    res[0].right = res[0]
                    res[0].left = res[0]
                    return head.right
                continue
            pre_node.right = res[i]
            res[i].left = pre_node

            if i == n - 1:
                res[i].right = head.right
                head.right.left = res[i]

                return head.right
            pre_node = res[i]



# Solution 4: DFS + Yield (The performance is not good, node creation may take time)
# Runtime: 107 ms, faster than 5.79% of Python3 online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
# class LinkNode:
#     def __init__(self, val, pre=None, next = None):
#         self.val = val
#         self.pre = pre
#         self.next = next

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None

        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root
                yield from dfs(root.right)

        head = None
        last = None
        pre_node = None
        for node in dfs(root):
            if last:
                last.right = node
                node.left = last
            else:
                head = node
            last = node

        head.left = last
        last.right = head

        return head



