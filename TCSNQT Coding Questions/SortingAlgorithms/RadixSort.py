
'''The lower bound for Comparison based sorting algorithm (Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(nLogn), i.e., they cannot do better than nLogn. Counting sort is a linear time sorting algorithm that sort in O(n+k) time when elements are in the range from 1 to k.

What if the elements are in the range from 1 to n2? 

We can't use counting sort because counting sort will take O(n2) which is worse than comparison-based sorting algorithms. Can we sort such an array in linear time? 

Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.'''
def countSort(arr,exp):
    n=len(arr)

    count=[0 for i in range(256)]
    output=[0 for i in range(n)]

    for i in range(n):
        index=arr[i]//exp
        count[index%10]+=1
    
    for i in range(len(count)):
        count[i]+=count[i-1]
    
    i=n-1
    while i>=0:
        output[count[arr[i]]-1]=arr[i]
        count[arr[i]]-=1
        i-=1
    
    for i in range(n):
        arr[i]=output[i]
def radixSort(arr):
    maximum=max(arr)
    exp=1
    while maximum/exp>1:
        countSort(arr,exp)
        exp*=10
arr=[0,6,2,1,4,2,0,4,3]
radixSort(arr)
print(arr)
#[0, 0, 1, 2, 2, 3, 4, 4, 6]

'''Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers, for example, for the decimal system, b is 10. What is the value of d? If k is the maximum possible value, then d would be O(logb(k)). So overall time complexity is O((n+b) * logb(k)). Which looks more than the time complexity of comparison-based sorting algorithms for a large k. Let us first limit k. Let k <= nc where c is a constant. In that case, the complexity becomes O(nLogb(n)). But it still doesn’t beat comparison-based sorting algorithms. 
What if we make the value of b larger?. What should be the value of b to make the time complexity linear? If we set b as n, we get the time complexity as O(n). In other words, we can sort an array of integers with a range from 1 to nc if the numbers are represented in base n (or every digit takes log2(n) bits). '''
