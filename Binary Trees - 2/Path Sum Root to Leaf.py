"""
----------------------------------------  Path Sum Root to Leaf  -----------------------------------------

Given a binary tree and a number k, print out all root to leaf paths where the sum of all nodes value is 
same as the given number k.

#### Input format :
    Line 1 : Elements in level order form (separated by space)
            (If any node does not have left or right child, take -1 in its place)
    Line 2 : k
#### Output format : 
    Print each path in new line, elements separated by space

#### Sample Input 1 :
    5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1
    13
#### Sample Output 1 :
    5 6 2
    5 7 1
"""

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, lst):

    if root is None:
        return
    
    if k < root.data:
        return
    
    if k == root.data:
        lst.append(root.data)
        print(*lst)
        lst.pop()
        return
    
    if k > root.data:
        k = k - root.data
        
        lst.append(root.data)
        
        rootToLeafPathsSumToK(root.left, k, lst)
        rootToLeafPathsSumToK(root.right, k, lst)
        
        lst.pop()

def buildLevelTree(levelorder):

    index = 0
    length = len(levelorder)

    if length<=0 or levelorder[0]==-1:
        return None

    root = BinaryTreeNode(levelorder[index])

    index += 1
    q = queue.Queue()
    q.put(root)

    while not q.empty():

        currentNode = q.get()
        leftChild = levelorder[index]

        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelorder[index]

        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k=int(input())
rootToLeafPathsSumToK(root, k, [])
