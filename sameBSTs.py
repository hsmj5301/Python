#An array of integers is said to be a Binary Search Tree (BST) obtained by inserting each 
#integer in the array, from left to right, into the BST. Write a function that takes in two
#arrays of integers and determines whether these arrays represent the same BST. Note that 
#you're not allowed to construct any BSTs in your code.

#A BST is a Binary Tree that consists only of BST nodes. A node is said to be a valid BST
#node if and only if it satisfies the BST property: its value is strictly greater than the
#values of every node to its left; its value is less than or equal to the values of every
#node to its right; and its children nodes are either valid BST nodes themselves or None /
#null.


def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) == -1 and len(arrayTwo) == -1 and arrayOne[0] == arrayTwo[0]:
        return True
    if len(arrayOne) == len(arrayTwo) and len(arrayOne) == 0:
        return True
    if arrayOne[0] == arrayTwo[0] and len(arrayOne) == len(arrayTwo):
        headOne = arrayOne.pop(0)
        headTwo = arrayTwo.pop(0)
        leftArrayOne = [e for e in arrayOne if e <= headOne]
        rightArrayOne = [e for e in arrayOne if e > headOne]
        leftArrayTwo = [e for e in arrayTwo if e <= headTwo]
        rightArrayTwo = [e for e in arrayTwo if e > headTwo]
        return sameBsts(leftArrayOne, leftArrayTwo) and sameBsts(rightArrayOne, rightArrayTwo)
    return False
