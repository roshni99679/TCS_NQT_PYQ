'''Printing all non-repeating elements:'''

def allNonRepeatingElement(arr,n):
    
    mp={}                                           #create an empty hash table(dict)
    
    for i in range(n):                              #i will iterate from 0 to len(arr)-1
        if arr[i] not in mp:                        #if the element at ith position does not already exist in hashtable:
            mp[arr[i]]=0                            #add that ith element into the hashtable as key and provide it a count of 0(value of that key=0)
            print(mp)
        mp[arr[i]]+=1                               #if the element at ith position already exist in hashtable increase its count by 1
        
    for x in mp:                                    #for each element(key) in mp:
        if mp[x]==1:                                #if count / value of that key is 1:
            print(x,end=" ")                        #print that key as it is the non repeating element
arr=[1,2,3,4,1,2,3,5]                   
n=len(arr)
# allNonRepeatingElement(arr,n)

'''
mp:
{1: 0}
{1: 1, 2: 0}
{1: 1, 2: 1, 3: 0}
{1: 1, 2: 1, 3: 1, 4: 0}
{1: 2, 2: 2, 3: 2, 4: 1, 5: 0}
'''
#op: 
# 4 5

'''Printing first non-repeating element'''
def firstNonRepeatingElement(arr,n):
    
    mp={}                                           #create an empty hash table(dict)
    
    for i in range(n):                              #i will iterate from 0 to len(arr)-1
        if arr[i] not in mp:                        #if the element at ith position does not already exist in hashtable:
            mp[arr[i]]=0                            #add that ith element into the hashtable as key and provide it a count of 0(value of that key=0)
        mp[arr[i]]+=1                               #if the element at ith position already exist in hashtable increase its count by 1
        
    for x in mp:                                    #for each element(key) in mp:
        if mp[x]==1:                                #if count / value of that key is 1:
            return x                                #returns the first key with count 1 as it is the first non repeating element
arr=[1,2,3,4,1,2,3,5]                   
n=len(arr)
# print(firstNonRepeatingElement(arr,n))
#4

'''
Time Complexity: O(n)
Auxiliary Space: O(n)
'''


'''Python3 program to find first non-repeating element.'''
def firstNonRepeating(arr, n):

	for i in range(n):
		j = 0
		while(j < n):
			if (i != j and arr[i] == arr[j]):
				break
			j += 1
		if (j == n):
			return arr[i]
	
	return -1
arr = [ 9, 4, 9, 6, 7, 4 ]
n = len(arr)
# print(firstNonRepeating(arr, n))
#6

'''Python3 program to find all non-repeating element.'''
def allNonRepeating(arr,n):
    for i in range(n):
        j=0
        while j<n:
            if (i != j and arr[i]==arr[j]):
                break
            j+=1
        if j==n:
            print(arr[i])
arr = [ 9, 4, 9, 6, 7, 4 ]
n = len(arr)
# allNonRepeating(arr, n)
#6 7

'''
Time Complexity: O(n*n)
Auxiliary Space: O(1)
'''

'''Program for array rotation (left rotation)
Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements. '''
def rotateArray(lst,d,n):
    k=lst.index(d)
    print(k)
    new=[]
    new=lst[k+1:]+lst[0:k+1]
    return new
lst=[1,2,3,4,5,6]
n=len(lst)
d=2
# print(rotateArray(lst,d,2))
#[3, 4, 5, 6, 1, 2]
'''
Time complexity : O(n) 
Auxiliary Space : O(n)
'''

def rotateArraydTimes(arr,d,n):
    p=1
    while p<=d:
        lastEle=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=lastEle    
        p+=1
    return arr

arr=[1,2,3,4,5,6,7,8,9,10]
# print(rotateArraydTimes(arr,3,len(arr)))
#[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
'''
Time Complexity: O(N*d), Where N is the length of the given array and d is the rotation number.
Auxiliary Space: O(1)
'''


'''
Equilibrium index of an array
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an array A: 

Example : 
Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
Output: 3 
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Input: A[] = {1, 2, 3} 
Output: -1 
'''
def equilibrium(arr):
    totalsum=sum(arr)
    leftsum=0
    for counter,value in enumerate(arr):
        totalsum=totalsum-value                 #rightsum
        if leftsum==totalsum:
            return counter
        leftsum=leftsum+value
    return -1
arr = [-7, 1, 5, 2, -4, 3, 0]
# print ('First equilibrium index is ',equilibrium(arr))
#First equilibrium index is 3
'''
Time Complexity: O(n)
Auxiliary Space: O(1)
'''

#enumerate
'''
Enumerate is a built-in function of Python. Its usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaware of it. It allows us to loop over something and have an automatic counter. Here is an example:

my_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(my_list):
    print counter, value
# Output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear
And there is more! enumerate also accepts an optional argument that allows us to specify the starting index of the counter.

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
# Output:
# 1 apple
# 2 banana
# 3 grapes
# 4 pear
An example of where the optional argument of enumerate comes in handy is creating tuples containing the index and list item using a list. Here is an example:

my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# Output: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
'''


'''Print array after it is right rotated K times'''
def rightrotate(arr,k,n):
    p=1
    while p<=k:
        
        for i in range(n-1,0,-1):
            val=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=val
        p+=1
    return arr

arr=[ 1, 2, 3, 4, 5 ]
k=2
n=len(arr)
# print(rightrotate(arr,k,n))

# [4, 5, 1, 2, 3]

def RightRotate(a, n, k):
	# If rotation is greater than size of array
	k = k % n
	for i in range(0, n):
		if(i < k):
			# Printing rightmost kth elements
			print(a[n + i - k], end = " ")
		else:
			# Prints array after 'k' elements
			print(a[i - k], end = " ")
Array = [ 1, 2, 3, 4, 5 ,6 ,7]
N = len(Array)
K = 3
# RightRotate(Array, N, K)

# 4 5 1 2 3


def rightRotate(arr,k,n):
    k=k%n 
    for i in range(n):
        if i<k:
            print(arr[n+i-k],end=" ")
        else:
            print(arr[i-k],end=" ")
# rightRotate([33,44,55,66,77,88],4,len([33,44,55,66,77,88]))

# 55 66 77 88 33 44




'''Find whether an array is subset of another array'''

def isSubset(arr1,arr2):
    l1=len(arr1)
    l2=len(arr2)
    s=set()
    for i in range(l1):
        s.add(arr1[i])
    ls=len(s)
    for j in range(l2):
        s.add(arr2[j])
    if len(s)==ls:
        print(f"{arr2} is a subset of {arr1}")
    else:
        print(f"{arr2} is not a subset of {arr1}")

arr1=[1,2,3,4,5,6,7,8,9,0]
arr2=[1,2,3,4,5]
arr3=[2,3,4,22,33]
# isSubset(arr1,arr2)
# isSubset(arr1,arr3)
# [1, 2, 3, 4, 5] is a subset of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [2, 3, 4, 22, 33] is not a subset of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]





''' A Python3 program to find all symmetric pairs in a given array of pairs.
Print all pairs that have a symmetric counterpart
symmetric pair: (10,20) and (20,10)
'''

'''
An Efficient Solution is to use Hashing. The first element of the pair is used as the key and the second element is used as the value. The idea is to traverse all pairs one by one. For every pair, check if its second element is in the hash table. If yes, then compare the first element with the value of the matched entry of the hash table. If the value and the first element match, then we found symmetric pairs. Else, insert the first element as a key and the second element as a value.
'''
def findSymPairs(arr, row):
	# Creates an empty hashMap hM
	hM = dict()
	# Traverse through the given array
	for i in range(row):
		# First and second elements of current pair
		first = arr[i][0]
		sec = arr[i][1]
		# If found and value in hash matches with first element of this pair, we found symmetry
		if (sec in hM.keys() and hM[sec] == first):
			print("(", sec,",", first, ")")

		else: # Else put sec element of this pair in hash
			hM[first] = sec

arr = [[0 for i in range(2)]
		for i in range(5)]
arr[0][0], arr[0][1] = 11, 20
arr[1][0], arr[1][1] = 30, 40
arr[2][0], arr[2][1] = 5, 10
arr[3][0], arr[3][1] = 40, 30
arr[4][0], arr[4][1] = 10, 5
# findSymPairs(arr, 5)
# findSymPairs([[11,20],[30,40],[5,10],[40,30],[10,5]],5)
# ( 30 , 40 )
# ( 5 , 10 )
# ( 30 , 40 )
# ( 5 , 10 )
'''
Time Complexity: O(n), where n is the size of the given array.
Auxiliary Space: O(n)
'''

'''
Counting Rock Samples | TCS Codevita 2020
John is a geologist, and he needs to count rock samples in order to send it to a chemical laboratory. He has a problem. The laboratory only accepts rock samples by a range of sizes in ppm (parts per million). John needs your help. Your task is to develop a program to get the number of rocks in each range accepted by the laboratory.

Problem Statement: Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], the task is to count the rock samples that are in the range ranges[i][0] to ranges[i][1], for every possible 1 <= i <= N.
'''
def rocksamples(arr,ranges,lr):
    a=[]
    for i in range(lr):
        count=0
        min=ranges[i][0]
        max=ranges[i][1]
        for val in arr:
            if min<=val<=max:
                count+=1
        a.append(count)
    return a
lr = 2
arr = [400, 567, 890, 765, 987]
ranges = [[300, 380], [800, 1000]]
# print(rocksamples(arr,ranges,lr))
#[0 2]

def findRockSample(ranges,n, r, arr):
	a = []
	for i in range(r):
		c = 0
		l, h = ranges[i][0], ranges[i][1]
		for val in arr:
			if l <= val <= h:
				c += 1
		a.append(c)
	return a
n = 5
r = 2
arr = [400, 567, 890, 765, 987]
ranges = [[300, 380], [800, 1000]]
# print(*findRockSample(ranges, n, r, arr))
#0 2


'''Write a program to reverse an array or string'''

def reverse(arr):
    lst=list(arr)
    finallst=lst[::-1]
    return finallst
# print(reverse([1,2,3]))
#[3,2,1]

def reverse(arr):
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
arr=[1,2,3,4,5]
# print("reversed Array",reverse(arr))
#reversed Array [5, 4, 3, 2, 1]
'''Time Complexity : O(n)'''


def reverse(arr,start,end):
    if start>end:
        return
    arr[start],arr[end]=arr[end],arr[start]
    reverse(arr,start+1,end-1)
    return arr
arr=[1,2,3,4,5,6,7,8,9]
# print("reversed Array",reverse(arr,0,len(arr)-1))  
#reversed Array [9, 8, 7, 6, 5, 4, 3, 2, 1]
'''Time Complexity : O(n)'''


'''Program for Mean and median of an unsorted array'''

'''
Given n size unsorted array, find it's mean and median. 
Mean of an array = (sum of all elements) / (number of elements)
Median of a sorted array of size n is defined as the middle element when n is odd and average of middle two elements when n is even.
Since the array is not sorted here, we sort the array first, then apply above formula.
'''

def mean(arr,n):
    sum=0
    for i in range(n):
        sum=sum+a[i]
    return float(sum/n)
def median(arr,n):
    sorted(arr)
    if(n%2 !=0):
        median=arr[int(n/2)]
    median=(arr[int((n-1)/2)]+arr[int(n/2)])/2.0
    return median
a = [1, 3, 4, 2, 7, 5, 8, 6]
n=len(a)
arr2=[1,2,3,4,5]
n2=len(arr2)
# print(mean(arr,n))
# print(median(arr,n))
# print(median(arr2,n2))
# 4.5
# 4.5
# 3.0

def findMean(a, n):
	sum = 0
	for i in range(0, n):
		sum += a[i]
	return float(sum/n)
def findMedian(a, n):
	sorted(a)
	if n % 2 != 0:
		return float(a[int(n/2)])

	return float((a[int((n-1)/2)] +
				a[int(n/2)])/2.0)

a = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(a)
# print("Mean =", findMean(a, n))
# print("Median =", findMedian(a, n))
# Mean = 4.5
# Median = 4.5
'''Time Complexity to find mean = O(n) 
Time Complexity to find median = O(n Log n) as we need to sort the array first. Note that we can find median in O(n) time using methods
Auxiliary Space : O(1)'''


'''Find the smallest and second smallest elements in an array'''
from array import array
import math
def smallest(arr):
    n=len(arr)
    smallest=math.inf
    for i in range(n):
        if a[i]<smallest:
            smallest=a[i]
    print(f"Smallest element is {smallest}")
    secondsmallest=math.inf
    for i in range(n):
        if smallest<a[i]<secondsmallest:
            secondsmallest=a[i]
    print(f"Second smallest is {secondsmallest}")
# smallest([12,34,1,2,3,4,5,6])
# Smallest element is 1
# Second smallest is 2
'''Time complexity: O(N)
Auxiliary space: O(1)'''



'''Largest ele in an array'''
def largest(arr):
    n=len(arr)
    largest=a[0]
    for i in range(1,n):
        if arr[i]>largest:
            largest=arr[i]
    print(f"Largest ele is {largest}")
    secondlargest=a[0]
    for i in range(1,n):
        if secondlargest<arr[i]<largest:
            secondlargest=arr[i]
    print(f"Largest ele is {secondlargest}")
arr=[1,2,3,55,77,99999,4]
# largest(arr)
# Largest ele is 99999
# Largest ele is 77
'''Time complexity: O(N), to traverse the Array completely.
Auxiliary Space: O(1), as only an extra variable is created, which will take O(1) space.'''

'''Counting frequencies of array elements'''
def freq(arr):
    n=len(arr)
    hashmap={}
    for i in range(n):
        if arr[i] not in hashmap:
            hashmap[arr[i]]=0
        hashmap[arr[i]]+=1
    for x in hashmap:
        print(f"element: {x} count: {hashmap[x]}",end="\n")
arr=[1,2,3,1,2,3,4,4,4,5,5,5,5,5,6]
# freq(arr)
# element: 1 count: 2
# element: 2 count: 2
# element: 3 count: 2
# element: 4 count: 3
# element: 5 count: 5
# element: 6 count: 1

def countFreq(arr, n):
	mp = dict()
	for i in range(n):
		if arr[i] in mp.keys():
			mp[arr[i]] += 1
		else:
			mp[arr[i]] = 1
	for x in mp:
		print(x, " ", mp[x])
arr = [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)
# countFreq(arr, n)
# 10   3
# 20   4
# 5   1
'''
Time Complexity : O(n) 
Auxiliary Space : O(n)
'''


'''Sum of elements of an array'''
def sumOfArray(a, n):
    c=float(sum(arr))
    print(c)
arr=[1,2,3,4,5,6]
# sumOfArray(arr,len(arr))

'''Remove duplicates from array'''
def removeduplicates(arr):
    n=len(arr)
    s=set()
    for i in range(n):
        s.add(arr[i])
    ls=len(s)
    return ls
ls=removeduplicates([1,2,3,3,2,1,4,4])
# print(f"Original length: {n} , new length: {ls}")
# Original length: 8 , new length: 4

def dups(a):
    n=len(a)
    mp={}
    for i in range(n):
        if a[i] not in mp:
            mp[a[i]]=0
        mp[a[i]]+=1
    return mp.keys(),len(mp)
a=[1,2,3,3,2,1,4,4]
# print(f"Original length is: {len(a)}")
# mp,l=dups(a)
# print(f"New length is: {l} and array after removal of duplicates is :{mp}")
# Original length is: 8
# New length is: 4 and array after removal of duplicates is :dict_keys([1, 2, 3, 4])

'''Remove duplicates from unsorted array using Map data structure'''
def removedups(arr):
    n=len(arr)
    hm={i:0 for i in arr}           #store all ele of array in a dict
    for i in range(n):
        if hm[a[i]]==0:             #if value of a key is 0:
            print(a[i],end=" ")     #that means that a[i]/key is an unique ele therfore print it
            hm[a[i]]=1
    x=len(hm)
    print("Thus new len is",x)
# removedups([1,2,3,3,2,1,4,4])
#1 2 3 4 Thus new len is 4


'''Remove duplicates from an sorted array'''
def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n
    arr.sort()
    print("Original Sorted Array:",arr,"original len of array:",len(arr))
    j = 1
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j += 1
    return j
# print("New length is",removeDuplicates([1,2,2,3,4,5,2,3],8))

'''rotate an array k times'''
def rotation(arr,k,n):
    p=1
    while p<=k:
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
        p+=1
    return arr
# arr=[1,2,3,4,5,6,7,8,9,10]
# print(rotation(arr,3,len(arr)))
#[4, 5, 6, 7, 8, 9, 10, 1, 2, 3]


'''Program for average of an array (Iterative and Recursive)'''
def ItrAvg(arr,n):
    addn=0
    for i in range(n):
        addn=addn+arr[i]
    return float(addn/n)
arr=[10, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Average is:",ItrAvg(arr,len(arr)))
# Average is: 6.0

def RecAvg(arr,i,n):
    if i==n-1:
        return arr[i]
    if i==0:
        return ((arr[i]+RecAvg(arr,i+1,n))/n)
    return (arr[i]+RecAvg(arr,i+1,n))
def avg(arr,n):
    return RecAvg(arr,0,n)
arr=[10, 2, 3, 4, 5, 6, 7, 8, 9]
n=len(arr)
# print(avg(arr,n))
# 6.0


'''How to add an element to an Array'''
import array as array
def addEle(arr,x,n):
    new = array.array('i', [0]*(n+1))
    for i in range(0,n):
        new[i]=arr[i]
    new[n]=x
    return new
arr=[1,2,3,4,5,6]
n=len(arr)
x=37
# print(addEle(arr,x,n))
#array('i', [1, 2, 3, 4, 5, 6, 37])

'''Find duplicates in O(n) time and O(1) extra space '''
def dups(arr,n):
    for i in range(n):
        x=arr[i]%n
        arr[x]+=n 
    for i in range(n):
        if arr[i]>=n*2:
            print(i,end=" ")
arr=[0, 4, 3, 2, 7, 8, 2, 3]
n=len(arr)
# dups(arr,n)


'''Function to replace each element of a list by its rank in the list'''
'''The rank of an element is defined as the distance between the element with the first element of the array when the array is arranged in ascending order. If two or more are same in the array then their rank is also the same as the rank of the first occurrence of the element. '''
def changeArr(input1):
	# Copy input array into newArray
	newArray = input1.copy()
	# Sort newArray[] in ascending order
	newArray.sort()
	# Dictionary to store the rank of the array element
	ranks = {}
	rank = 1
	for index in range(len(newArray)):
		element = newArray[index]
		# Update rank of element
		if element not in ranks:
			ranks[element] = rank
			rank += 1		
	# Assign ranks to elements
	for index in range(len(input1)):
		input1[index] = ranks[input1[index]]

# Driver Code
if __name__ == "__main__":
	# Given array arr[]
	arr = [ 100, 2, 70, 2 ]
	# Function call
	changeArr(arr)
	# Print the array elements
	print(arr)
#[3, 1, 2, 1]

'''
1.make a newarray which is a copy of given array
2.sort the newarray in ascending order(in an sorted array rank is the index of distinct elements)
3.create an empty hashmap/dict for storing elements of array and its corresponding rank
4.Initialize rank as 1 as initially all ele will have rank as 1
5.for each element of newarray,if element is not in hashmap store the ele in hashmap and give it a rank 1 and increment the rank
if the element already exist dont increment rank as same ele have same rank
6.for each ele in given arr , replace arra ele with the value of that ele in the hashmap
'''
def findrank(arr,n):
    newarr=arr.copy()
    newarr.sort()
    ranks={}
    rank=1
    for i in range(len(newarr)):
        element=newarr[i]
        if element not in ranks:
            ranks[element]=rank
            rank+=1
    for i in range(n):
        arr[i]=ranks[arr[i]]
arr = [ 100, 2, 70, 2 ]
findrank(arr,len(arr))
print(arr)
#[3, 1, 2, 1]


''''''