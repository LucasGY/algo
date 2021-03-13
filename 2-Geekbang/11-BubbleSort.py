

def bubbleSort(array, n):
    for i in range(n):
        flag = False  # 提前退出冒泡循环的标志位
        for j in range(n-i-1): ######-i表示，去掉排序好的元素；-1表示跟下一个元素对比，所以不能走到最头上。
            if array[j] > array[j+1]:
                tmp = array[j+1]
                array[j+1] = array[j]
                array[j] = tmp
                flag = True  # 表示有数据交换       
        print(array)
        if flag == False: break
        
if __name__ == '__main__':
    array = [3,5,4,1,2,6]
    bubbleSort(array,len(array))