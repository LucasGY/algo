class TreeNode(object):
    def __init__(self, val = None):
        # super(TreeNode, self).__init__(*args))
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree(object):
    def __init__(self, val_list = []):
        # super(BinarySearchTree, self).__init__(*args))
        self.root = None
        for n in val_list:
            self.insert(n)
    
    def insert(self, data):
        # 根结点插入
        if self.root == None:
            self.root = TreeNode(data)
        else:  # 不是根结点
            n = self.root
            



            
            
            
        
        