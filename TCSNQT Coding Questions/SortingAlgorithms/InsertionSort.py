'''Insertion Sort

 
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

Characteristics of Insertion Sort:
This algorithm is one of the simplest algorithm with simple implementation
Basically, Insertion sort is efficient for small data values
Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.
Working of Insertion Sort algorithm:
Consider an example: arr[]: {12, 11, 13, 5, 6}

   12   	   11   	   13   	   5   	   6   
First Pass:

Initially, the first two elements of the array are compared in insertion sort.
   12   	   11   	   13   	   5   	   6   
Here, 12 is greater than 11 hence they are not in the ascending order and 12 is not at its correct position. Thus, swap 11 and 12.
So, for now 11 is stored in a sorted sub-array.
   11   	   12   	   13   	   5   	   6   
Second Pass:

 Now, move to the next two elements and compare them
   11   	   12   	   13   	   5   	   6   
Here, 13 is greater than 12, thus both elements seems to be in ascending order, hence, no swapping will occur. 12 also stored in a sorted sub-array along with 11
Third Pass:

Play Video
Advertisement
Now, two elements are present in the sorted sub-array which are 11 and 12
Moving forward to the next two elements which are 13 and 5
   11   	   12   	   13   	   5   	   6   
Both 5 and 13 are not present at their correct place so swap them
   11   	   12   	   5   	   13   	   6   
After swapping, elements 12 and 5 are not sorted, thus swap again
   11   	   5   	   12   	   13   	   6   
Here, again 11 and 5 are not sorted, hence swap again
   5   	   11   	   12   	   13   	   6   
here, it is at its correct position
Fourth Pass:

Now, the elements which are present in the sorted sub-array are 5, 11 and 12
Moving to the next two elements 13 and 6
   5   	   11   	   12   	   13   	   6   
Clearly, they are not sorted, thus perform swap between both
   5   	   11   	   12   	   6   	   13   
Now, 6 is smaller than 12, hence, swap again
   5   	   11   	   6   	   12   	   13   
Here, also swapping makes 11 and 6 unsorted hence, swap again
   5   	   6   	   11   	   12   	   13   
Finally, the array is completely sorted.
Illustrations:

insertion-sort
 

Insertion Sort Algorithm 
To sort an array of size N in ascending order: 

Iterate from arr[1] to arr[N] over the array. 
Compare the current element (key) to its predecessor. 
If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.'''


def InsertionSort(sequence):
    #sorted part has the first element of the sequence (ele at sequence[0])
    for i in range(1,len(sequence)):        #iterate over the unsorted part (ele at sequence[1] to sequence[n-1]))
        value_to_sort=sequence[i]           #first ele of unsorted part
        j=i-1                               #j=0 (sorted part)
        while j>=0 and value_to_sort<sequence[j]:       #loop until value to sort is lesser than its predecessor
            sequence[j+1]=sequence[j]
            j-=1                            #sort the unsorted part until value_to_sort is at right position(left comparison)
        sequence[j+1]=value_to_sort
    return sequence
print(InsertionSort([22,33,11,44,77,55]))
#[11, 22, 33, 44, 55, 77]

'''Time Complexity: O(N^2) 
Auxiliary Space: O(1)'''


