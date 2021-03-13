def quick_sort(array, n):
    quick_sort_c(array, 0 , n-1)
    
def quick_sort_c(A, p, r):
    if p >= r :return

    q = partition(A, p, r)
    quick_sort_c(A, p, q-1) ##### care for error
    quick_sort_c(A, q+1, r)

def partition(A, p, r):
    i = p
    pivot = A[r]
    for j in range(p,r):
        # swap
        if A[j] < pivot:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1
    # swap
    A[r] = A[i]
    A[i] = pivot
    print (A)

    return i

if __name__ == '__main__':
    array = [3,5,4,1,2,6]
    quick_sort(array,len(array))

        



