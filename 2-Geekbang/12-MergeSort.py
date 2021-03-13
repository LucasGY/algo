
# 
def merge_sort(array, n):
    merge_sort_c(array, 0 , n-1)

def merge_sort_c(A, p, r):
    # 递归终止条件
    if p>=r: return

    # 取p到r之间的中间位置q
    q = round((p+r)/2)

    # 分治递归
    merge_sort_c(A, p, q)
    merge_sort_c(A, q+1, r)
    merge(A[p:r], )
        
def merge():
    i = p
    j = q+1
    tmp = [] # 申请一个大小跟A[p:r]一样的临时数组

    while (i<=q and j<=r):
        if A[i]>A[j]:
            tmp.append(A[j])
            j += 1
        else:
            tmp.append(A[i])
            i += 1
    
    # 判断哪个子数组中有剩余的数据
    if i<=q:
        start = i, end = q
    else: # j<=r
        start = j, end = r

    # 将剩余的数据拷贝到临时数组tmp
    for k in range(start, end+1):
        tmp.append(A[k])
        
        
    


            



