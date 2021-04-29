'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes
        have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        satisfied = True
        if not node:
            return satisfied
        if node.left:
            satisfied &= AVLTree._is_avl_satisfied(node.left)
        if node.right:
            satisfied &= AVLTree._is_avl_satisfied(node.right)

        bf = AVLTree._balance_factor(node)
        if abs(bf) >= 2:
            satisfied = False

        return satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.right:
            old_root = Node(node.value)
            old_root.left = node.left
            old_root.right = node.right.left
            new_root = Node(node.right.value)
            new_root.right = node.right.right
            new_root.left = old_root
        else:
            new_root = node
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code
        is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node.left:
            old_root = Node(node.value)
            old_root.right = node.right
            old_root.left = node.left.right
            new_root = Node(node.left.value)
            new_root.left = node.left.left
            new_root.right = old_root
        else:
            new_root = node
        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to
        insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code
        is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        '''
        Helper function for insert
        '''
        if node.value < value:
            if node.right:
                AVLTree._insert(node.right, value)
            else:
                node.right = Node(value)
        elif node.value > value:
            if node.left:
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
        if AVLTree._is_avl_satisfied(node):
            pass
        else:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            node = AVLTree._rebalance(node)
        return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        print("Entered")
        if AVLTree._balance_factor(node) < -1:
            if AVLTree._balance_factor(node.right) > 0:
                rot_child = AVLTree._right_rotate(node.right)
                node.right = rot_child
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 1:
            if AVLTree._balance_factor(node.left) < 0:
                rot_child = AVLTree._left_rotate(node.left)
                node.left = rot_child
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
        return node


av1 = AVLTree()
xs = [0, 1, -8, -10, -11, -12, 19, 84, 83, 96]
for x in xs:
    av1.insert(x)
    print(str(av1))
