# https://www.youtube.com/watch?v=5iSZ7mh_RAk&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=15

'''# QuickSort

# Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

# Always pick the first element as a pivot.
# Always pick the last element as a pivot (implemented below)
# Pick a random element as a pivot.
# Pick median as the pivot.
# The key process in quickSort is a partition(). The target of partitions is, given an array and an element x of an array as the pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time.

# /* low  -> Starting index,  high  -> Ending index */
'''

# Function to find the partition position

from re import A
from tempfile import tempdir


def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)        
# Driver code
# array = [ 10, 7, 8, 9, 1, 5]
# quick_sort(array, 0, len(array) - 1)
# print(f'Sorted array: {array}')
     

# Output
# Sorted array: 
# 1 5 7 8 9 10 
\

# Implementation of QuickSort using the first element as a pivot
# Function to find the partition position
def partition(arr, l, h):
  low, high = l, h
  if l != h and l < h:
    # Choose the leftmost element as pivot
    pivot = arr[l]
    low = low+1
    # Traverse through all elements compare each element with pivot
    while low <= high:
      if arr[high] < pivot and arr[low] > pivot:
        arr[high], arr[low] = arr[low], arr[high]
      if not arr[low] > pivot:
        low += 1
      if not arr[high] < pivot:
        high -= 1
  arr[l], arr[high] = arr[high], arr[l]
  # Return the position from where partition is done
  return high
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
 
      # Find pivot element such that element smaller than pivot are on the left element greater than pivot are on the right
      pi = partition(array, low, high)
       # Recursive call on the left of pivot
      quick_sort(array, low, pi - 1) 
      # Recursive call on the right of pivot
      quick_sort(array, pi + 1, high)
array=[1,4,3,2,0,99,66,32,1011,0]
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')



# def part(arr,low,high):
#   temp=high
#   if low<high and low!=high:
#     pivot=arr[temp]
#     high-=1
#     while low<=high:
#       if arr[low]>pivot and arr[high]<pivot:
#         arr[low],arr[high]=arr[high],arr[low]
#       if not arr[low]>pivot:
#         low=low+1
#       if not arr[high]<pivot:
#         high=high-1
#   arr[temp],arr[high]=arr[high],arr[temp]
#   return high
# def quicksort(arr,low,high):
#   if low<high:
#     pivot=part(arr,low,high)
#     quicksort(arr,low,pivot-1)
#     quicksort(arr,pivot+1,high)
# arr=[1,4,3,2,0,99,66,32,1011,0]
# quicksort(arr,0,len(arr)-1)
# print(arr)

def part(arr,low,high):
  temp=low
  if low<high and low!=high:
    pivot=arr[temp]
    low+=1
    while low<=high:
      if arr[low]>pivot and arr[high]<pivot:
        arr[low],arr[high]=arr[high],arr[low]
      if not arr[low]>pivot:
        low+=1
      if not arr[high]<pivot:
        high-=1
  arr[temp],arr[high]=arr[high],arr[temp]
  return high
def quicksort(arr,low,high):
  if low<high:
    pivot=part(arr,low,high)
    quicksort(arr,low,pivot-1)
    quicksort(arr,pivot+1,high)
arr=[1,4,3,2,0,99,66,32,1011,0]
quicksort(arr,0,len(arr)-1)
print(arr)
#[0, 0, 1, 2, 3, 4, 32, 66, 99, 1011]




'''
Output
Before Sorting
4 2 8 3 1 5 7 11 6 
After Sorting
1 2 3 4 5 6 7 8 11 
Analysis of QuickSort 
Time taken by QuickSort, in general, can be written as follows. 

 T(n) = T(k) + T(n-k-1) + \theta              (n)

The first two terms are for two recursive calls, the last term is for the partition process. k is the number of elements that are smaller than the pivot. 
The time taken by QuickSort depends upon the input array and partition strategy. Following are three cases.

Worst Case: 
The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. If we consider the above partition strategy where the last element is always picked as a pivot, the worst case would occur when the array is already sorted in increasing or decreasing order. Following is recurrence for the worst case.  

 T(n) = T(0) + T(n-1) + \theta              (n)which is equivalent to  T(n) = T(n-1) + \theta              (n)

The solution to the above recurrence is                   (n2). 

Best Case:
The best case occurs when the partition process always picks the middle element as the pivot. The following is recurrence for the best case. 

 T(n) = 2T(n/2) + \theta              (n)

The solution for the above recurrence is                  (nLogn). It can be solved using case 2 of Master Theorem.

Average Case: 
To do average case analysis, we need to consider all possible permutation of array and calculate time taken by every permutation which doesn’t look easy. 
We can get an idea of average case by considering the case when partition puts O(n/9) elements in one set and O(9n/10) elements in other set. Following is recurrence for this case.  

 T(n) = T(n/9) + T(9n/10) + \theta              (n)

The solution of above recurrence is also O(nLogn):

Although the worst case time complexity of QuickSort is O(n2) which is more than many other sorting algorithms like Merge Sort and Heap Sort, QuickSort is faster in practice, because its inner loop can be efficiently implemented on most architectures, and in most real-world data. QuickSort can be implemented in different ways by changing the choice of pivot, so that the worst case rarely occurs for a given type of data. However, merge sort is generally considered better when data is huge and stored in external storage. 
 '''


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0]))