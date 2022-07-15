#https://www.youtube.com/watch?v=usmp6uL_a9c
def countSort(arr):

    n=len(arr)
    count=[0 for i in range(256)]           #count arr will store count of each element in given array
    output=[0 for i in range(n)]            #output arr will store ele in sorted manner

    for i in range(n):                      #for each ele in given array , store its count in count array
        count[arr[i]]+=1
    # print(count)

    for i in range(len(count)):             #store the cumulative count in count array     example:[0,1,4,2,3,1]=[0,1,5,7,10,11]
        count[i]+=count[i-1]
    # print(count)

    i=n-1
    while i>=0:
        output[count[arr[i]]-1]=arr[i]      #formula to store ele in sorted manner in output array
        count[arr[i]]-=1
        i-=1

    for i in range(n):                      #store the sorted ele in originally given arr
        arr[i]=output[i]

arr=[4, 2, 2, 8, 3, 3, 1]
countSort(arr)
print(arr)
#[1, 2, 2, 3, 3, 4, 8]

'''Time complexity: O(n), where n is total number of elements
Auxiliary Space: O(n)'''
