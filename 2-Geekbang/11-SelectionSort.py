def selectionSort(array, n):
    for i in range(0,n-1):
        min = array[i]
        min_index = i
        for j in range(i+1,n):
            if min > array[j]:
                min = array[j]
                min_index = j
        array[min_index] = array[i]
        array[i] = min
        print(array)

            

        
if __name__ == '__main__':
    array = [3,5,4,1,2,6]
    selectionSort(array,len(array))