# youtube link : https://www.youtube.com/watch?v=nCNfu_zNhyI

'''Merge Sort Algorithm  (divide and conquer)'''
def mergeSort(seq):
    if len(seq)<=1:
        return

    #divide (len(seq)>1)
    mid = len(seq)//2
    left=seq[:mid]
    right=seq[mid:]

    #recursively divide left and right seq until their len > 1
    mergeSort(left)
    mergeSort(right)

    #merge the two sorted seq left and right into the sequence arr
    merge_two_sorted_seq(left,right,seq)

def merge_two_sorted_seq(left,right,seq):
    #i works on left seq , j works on right seq and k works on the seq to merge the ele from right and left in sorted manner into seq array
    i=j=k=0

    while i<len(left) and j<len(right): 

        if left[i]<=right[j]:       #if ele in left seq is lesser than ele in right seq
            seq[k]=left[i]          #place that lesser ele that is ele of left seq into the final seq named seq
            i+=1                    #after placing the lesser ele increase its counter

        else:                       #if ele in right seq is lesser than ele in left seq
            seq[k]=right[j]         #place that lesser ele that is ele of right seq into the final seq named seq
            j+=1                    #after placing the lesser ele increase its counter
        k+=1                        #after placing sorted ele in seq inc its counter too

    #if len(left)<len(right) or vice versa and the seq having greater number ele will not be included in the final seq thus run a loop for each seq so as to place the extra ele in the final sorted seq
    while i<len(left):
        seq[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        seq[k]=right[j]
        j+=1
        k+=1

testCases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
for x in testCases:
    mergeSort(x)
    print(x)


'''Time Complexity: O(n logn),  Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 

T(n) = 2T(n/2) + θ(n)

The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of Master Method and the solution of the recurrence is θ(nLogn). Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
Auxiliary Space: O(n)

Space Complexity :

• In merge sort all elements are copied into an auxiliary array 
• so N auxiliary space is required for merge sort.'''


def divide(seq):
    if len(seq)<=1:
        return

    mid=len(seq)//2
    left=seq[:mid]
    right=seq[mid:]

    divide(left)
    divide(right)

    mergeLeftandRight(left,right,seq)

def mergeLeftandRight(left,right,seq):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            seq[k]=left[i]
            i+=1
        else:
            seq[k]=right[j]
            j+=1
        k+=1

    while i < len(left):
            seq[k]=left[i]
            i+=1
            k+=1
    while j<len(right):
            seq[k]=right[j]
            j+=1
            k+=1

testCases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]
for x in testCases:
    divide(x)
    print(x)
