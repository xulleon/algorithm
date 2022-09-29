# # https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ''

        res, queue = [], [root]

        while queue:
            node = queue.pop(0)
            if node == None:
                res.append('null')
            else:
                res.append(str(node.val))
                queue.extend([node.left, node.right])

        while res[-1] == 'null':
            res.pop()

        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        data = data.split(',')
        root = TreeNode(data.pop(0))
        queue = [root]
        while data and queue:
            node = queue.pop(0)
            left = data.pop(0)
            if left:
                node.left = TreeNode(left)
                queue.append(node.left)
            if data:
                right = data.pop(0)
                if right:
                    node.right = TreeNode(right)
                    queue.append(node.right)
        return root


