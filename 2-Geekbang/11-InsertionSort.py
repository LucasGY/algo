def insertionSort(array, n):
    for i in range(1,n):
        value = array[i]
        j = i-1
        while(j >= 0):
            if array[j] > value:
                array[j+1] = array[j]
                j -= 1
            else:
                break
        array[j+1] = value
        print(array)
        
               
            
        

        
if __name__ == '__main__':
    array = [3,5,4,1,2,6]
    insertionSort(array,len(array))