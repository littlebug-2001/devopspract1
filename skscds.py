def insertion_sort(array,size):
    for i in range(1,size):
        key=array[i]
        j=i
        while(j>0) and (array[j-1]>key):
            array[j]=array[j-1]
            j=j-1
            array[j]=key
array=[3,6,1,8]
n=len(array)
print("array before sorting:",array)
insertion_sort(array,n)
print("array after sorting:",array)

     
