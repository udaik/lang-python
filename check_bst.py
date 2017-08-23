class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def checkNode(root):
    if root.left and (root.left.data >= root.data)

def checkBST(root):

    if (root.left and (root.left.data < root.data)) and (root.right and root.right.data > root.data):
        return True;
    else:
        return False;
    return (checkBST(root.left) | checkBST(root.right))
