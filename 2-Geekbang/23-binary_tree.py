from typing import *
# T = TypeVar("T")
class Stack(object):
    def __init__(self, maxsize):
        # super(Stack, self).__init__(*args))
        self.values = [] # list,array
        self.count = 0 # num of element
        self.maxsize = maxsize

    def push(self, value):
        """入栈操作
        """
        # 判断栈满
        if self.count == self.maxsize : 
            print("full")
            return
        else:
            self.values.append(value)
            self.count += 1
            return

    def pop(self,):
        """出栈操作
        """
        # 判断栈空
        if self.count == 0 : 
            print("NULL")
            return
        buf = self.values[self.count-1]
        self.values = self.values[:-1] # 删除最后一个元素
        self.count -= 1
        return buf


        

class TreeNode(object):
    def __init__(self, value):
        # super(TreeNode, self).__init__(*args))
        self.val = value
        self.left = None
        self.right = None
# Pre-order traversal 先序遍历（递归）
def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

# In-order traversal 中序遍历（递归）
def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

# In-order traversal 中序遍历（栈）
def in_order_stack(root):
    T = root
    stack = Stack(1000)
    while(T or stack.count!=0):
        while(T):
            stack.push(T)
            T = T.left
        if stack.count!=0:
            T = stack.pop()
            print(T.val)
            T = T.right
        # else:
        #     break
        




# Post-order traversal 后序遍历（递归）
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)



if __name__ == '__main__':
    singer = TreeNode("Taylor Swift")

    genre_country = TreeNode("Country")
    genre_pop = TreeNode("Pop")

    album_fearless = TreeNode("Fearless")
    album_red = TreeNode("Red")
    album_1989 = TreeNode("1989")
    album_reputation = TreeNode("Reputation")

    song_ls = TreeNode("Love Story")
    song_wh = TreeNode("White Horse")
    song_wanegbt = TreeNode("We Are Never Ever Getting Back Together")
    song_ikywt = TreeNode("I Knew You Were Trouble")
    song_sio = TreeNode("Shake It Off")
    song_bb = TreeNode("Bad Blood")
    song_lwymmd = TreeNode("Look What You Made Me Do")
    song_g = TreeNode("Gorgeous")

    singer.left, singer.right = genre_country, genre_pop
    genre_country.left, genre_country.right = album_fearless,album_red
    genre_pop.left, genre_pop.right = album_1989, album_reputation
    album_fearless.left, album_fearless.right = song_ls, song_wh
    album_red.left, album_red.right = song_wanegbt, song_ikywt
    album_1989.left, album_1989.right = song_sio, song_bb
    album_reputation.left, album_reputation.right = song_lwymmd, song_g

    in_order_stack(singer)