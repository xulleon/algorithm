# https://www.lintcode.com/problem/242
# 1140 ms time cost· 6.56 MB memory cost· Your submission beats 87.20 % Submissions

from collections import deque
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        outputs = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node is None:
                    continuie
                if i == 0:
                    link_node = ListNode(node.val)
                    # remember to use this to be added into outputs
                    tmp_link = link_node
                else:
                    link_node.next = ListNode(node.val)
                    # remember to update link_node
                    link_node = link_node.next
                for nbr in [node.left, node.right]:
                    if nbr is None:
                        continue
                    queue.append(nbr)
            outputs.append(tmp_link)
        return outputs
