"""
This file contain the following functions:
build binary tree, deep first search, breadth first search, deep first ordered search
build decision tree, deep first search decision tree
"""


class binaryTree(object):
    """build binary tree"""
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None

    def setLeftBranch(self, node):
        self.leftBranch = node

    def setRightBranch(self, node):
        self.rightBranch = node

    def setParent(self, node):
        self.parent = node

    def getLeftBranch(self):
        return self.leftBranch

    def getRightBranch(self):
        return self.rightBranch

    def getParent(self):
        return self.parent

    def getValue(self):
        return self.value

    def __str__(self):
        return self.value


def DFSBinary(root, fcn):
    """
    Deep first search binary tree
    root: root node
    fcn: a function that can check if the node is what we want
        yes return True, no return False
    """
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            print 'at the node:', str(temp.getValue())
            if temp.getRightBranch():
                queue.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0,temp.getLeftBranch())
    return False


def BFSBinary(root,fcn):
    """
    Breadth first search binary tree
    root: root node
    fcn: a function that can check if the node is what we want
        yes return True, no return False
    """
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            print 'at the node:', str(temp.getValue())
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
    return False


def DFSBinaryOrdered(root, fcn, ltFcn):
    """
    Deep first search binary tree ordered
    root: root node
    fcn: a function that can check if the node is what we want
        yes return True, no return False
    lfFcn: a function that can check if the value of the node is bigger than the number we want
        yes return True, no return False
    """
    queue = [root]
    while len(queue) > 0:
        if fcn(queue[0]):
            return True
        elif ltFcn(queue[0]):
            temp = queue.pop(0)
            print temp.getValue()
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
        else:
            temp = queue.pop(0)
            print temp.getValue()
            if temp.getRightBranch():
                queue.insert(0, temp.getRightBranch())
    return False


n5 = binaryTree(5)
n2 = binaryTree(2)
n8 = binaryTree(8)
n1 = binaryTree(1)
n4 = binaryTree(4)
n3 = binaryTree(3)
n6 = binaryTree(6)
n7 = binaryTree(7)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n4.setLeftBranch(n3)
n3.setParent(n4)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)

def find6(node):
    return node.getValue() == 6

def lt6(node):
    return node.getValue() > 6

print DFSBinaryOrdered(n5, find6, lt6)
print
print BFSBinary(n5, find6)
print
print DFSBinary(n5, find6)


# Decision Tree
def builtDTree(sofar, todo):
    """
    build decision tree
    sofar: a list containing choices that have been done
    todo: a list containing choices that have not been done
    return: the root node
    """
    if len(todo) == 0:
        return binaryTree(sofar)
    else:
        withelt = builtDTree(sofar + [todo[0]], todo[1:])
        withoutelt = builtDTree(sofar, todo[1:])
        node = binaryTree(sofar)
        node.setLeftBranch(withelt)
        node.setRightBranch(withoutelt)
        return node

a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]
treeTest = builtDTree([], [a,b,c,d])


def DFSDTree(root, sum_value, has_space):
    """
    Deep first search decision tree
    root: root node
    sum_value: a function that can sum the value of the node
    has_space: a function that can check if there is spare room
    return: the best decision that can get the most value without beyonding the room
    """
    stack = [root]
    best = stack[0]
    while len(stack) > 0:
        if has_space(stack[0]):
            if sum_value(stack[0]) > sum_value(best):
                best = stack[0]
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
        else:
            stack.pop(0)
    return best.getValue()


def sum_value(node):
    e = [lst[0] for lst in node.getValue()]
    return sum(e)


def has_space(node, space = 10):
    e = [lst[1] for lst in node.getValue()]
    return sum(e) <= space

print DFSDTree(treeTest, sum_value, has_space)


