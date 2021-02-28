

def selectionSort(a):
    for i in range(len(a)):
        """Traverse through the whole array"""
        min_index = i # storing the index as the minimum index
        for j in range(i+1,len(a)): # from index i + 1 to last
            if a[j] < a[min_index]:
                min_index = j

        a[i] , a[min_index ] = a[min_index ] , a[i]  # swaping the current element

a = [3,2,4,51,1,43]
print("Original array" , a)
selectionSort(a)
print("After sorting " , a)
