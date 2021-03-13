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