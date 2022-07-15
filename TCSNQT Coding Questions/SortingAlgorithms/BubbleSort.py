'''Bubble Sort Algorithm'''

'''Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst case time complexity is quite high.

How Bubble Sort Works?
Consider an array arr[] = {5, 1, 4, 2, 8}

First Pass: 

Bubble sort starts with very first two elements, comparing them to check which one is greater.
( 5 1 4 2 8 ) -> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
( 1 5 4 2 8 ) ->  ( 1 4 5 2 8 ), Swap since 5 > 4 
( 1 4 5 2 8 ) ->  ( 1 4 2 5 8 ), Swap since 5 > 2 
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass: 

Now, during second iteration it should look like this:
( 1 4 2 5 8 ) -> ( 1 4 2 5 8 ) 
( 1 4 2 5 8 ) -> ( 1 2 4 5 8 ), Swap since 4 > 2 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) ->  ( 1 2 4 5 8 ) 
Third Pass: 

Now, the array is already sorted, but our algorithm does not know if it is completed.
The algorithm needs one whole pass without any swap to know it is sorted.
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) 
( 1 2 4 5 8 ) -> ( 1 2 4 5 8 ) '''


def bubbleSort(arr):
    indexing_len=len(arr)-1         #because last ele doesnt not have any right ele to it for comparison and hence we dont traverse upto last ele
    sorted =False                   
    while not sorted:
        sorted =True                #breaks the loop as soon as the arr is sorted (improves time complexity)
        for i in range(indexing_len):
            if arr[i]>arr[i+1]:
                sorted=False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
print(bubbleSort([3,2,4,5,1,7,6]))
#[1, 2, 3, 4, 5, 6, 7]




