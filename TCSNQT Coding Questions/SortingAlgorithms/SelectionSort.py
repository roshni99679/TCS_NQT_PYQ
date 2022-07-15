'''Selection Sort Algorithm'''

'''Initialize minimum value(min_idx) to location 0
Traverse the array to find the minimum element in the array
While traversing if any element smaller than min_idx is found then swap both the values.
Then, increment min_idx to point to next element
Repeat until array is sorted'''

A = [64, 25, 12, 22, 11]
# Traverse through all array elements
for i in range(len(A)):
    min_idx = i
    # Find the minimum element in remaining unsorted array
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
              
    # Swap the found minimum element with the first element        
    A[i], A[min_idx] = A[min_idx], A[i]
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i],end=" ") 
#11 12 22 25 64

#Ascending order
def selectionSort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

A=[22,44,11,33,88,66,44]
selectionSort(A)
# for i in range(len(A)):
#     print("%d" %A[i],end=" ") 
#88 66 44 44 33 22 11 

#Descending order
def selectionSort(arr):
    for i in range(len(arr)):
        max_index=i
        for j in range(i+1,len(arr)):
            if arr[max_index]<arr[j]:
                max_index=j
        arr[i],arr[max_index]=arr[max_index],arr[i]
arr=[22,33,55,11,77,31]
selectionSort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
#77 55 33 31 22 11 

'''Complexity Analysis of Selection Sort:
Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

One loop to select an element of Array one by one = O(N)
Another loop to compare that element with every other Array element = O(N)
Therefore overall complexity = O(N)*O(N) = O(N*N) = O(N2)

Auxiliary Space: O(1) as the only extra memory used is for temporary variable while swapping two values in Array. The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation. '''



