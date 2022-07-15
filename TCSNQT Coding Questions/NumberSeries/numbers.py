'''Prime Numbers''' 
from unicodedata import digit


def isPrime(n):
    if n==1:
        print(n,"is neither prime nor composite")
    elif n==2:
        print(n,"the only even prime number")
    elif n>=3:
        for i in range(2,n):
            if n%i==0:
                print(n,"is not prime")
                break
            else:
                print(n,"is prime")
# isPrime(1)
# isPrime(2)
# isPrime(3)
# isPrime(4)
'''
1 is neither prime nor composite
2 the only even prime number
3 is prime
4 is not prime
'''

# Another approach: It is based on the fact that all primes greater than 3 are of the form 6k ± 1, where k is any integer greater than 0. This is because all integers can be expressed as (6k + i), where i = −1, 0, 1, 2, 3, or 4. And note that 2 divides (6k + 0), (6k + 2), and (6k + 4) and 3 divides (6k + 3). So, a more efficient method is to test whether n is divisible by 2 or 3, then to check through all numbers of the form 6k ± 1 <= √n. This is 3 times faster than testing all numbers up to √n. (Source: wikipedia).  
import math
 
def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
       
    # To check through all numbers of the form 6k ± 1
    # until i <= square root of n, with step value 6
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
 
    return True
# print(isPrime(11))
# print(isPrime(20))



'''Sum of an Arithematic Series'''
def arithematic(a,n,d):
    a,n,d=float(a),float(n),float(d)
    asum=float((n / 2) * (2 * a + (n - 1) * d))
    return asum
# print(arithematic(2,3,2))
#12.0

'''Program for sum of geometric series'''
def sumOfGP( a, r, n) :
    return (a * (1 - pow(r, n))) / (1 - r)
# print(sumOfGP(2, 2, 2)) 
#6.0

'''Find all divisors of a natural number'''
def div(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=",")
n=100
# print(f"Divisors of {n} are:",end=" ")
# div(n)
#Divisors of 100 are: 1,2,4,5,10,20,25,50,100,1203

''''''

'''Write a program to reverse digits of a number'''
'''
num=1234
rev_num=0
rev_num = rev_num*10+num%10 = 0*10+1234%10 = 4
num= num//10 = 1234 // 10 =123
rev_num = rev_num*10+num%10 = 4*10+123%10 = 40+3 = 43
num = num //10 = 123//10 = 12
rev_num=rev_num*10+num%10 = 43*10+12%10 = 430+2 = 432
num=num//10 = 12 // 10 = 1
rev_num=rev_num*10+num%10 = 432*10+1%10 = 4320+1 = 4321
num=num//10 = 1//10 = 0
'''
def rev_num(num):
    rev_number=0
    while num>0:
        rev_number = rev_number*10 + num%10
        num = num //10
    print(rev_number)
# rev_num(987654444532)
#235444456789

'''Replace all 0 with 5 in an input Integer'''
def replace_num(n):
    def rev_again(n):
        rev=0
        while n>0:
            rev=rev*10+n%10
            n=n//10
        return rev                  #123595

    if n==0:
        return 5
    else: 
        rev=0
        while n>0:
            last_digit = n % 10
            if last_digit==0:
                last_digit=5
            rev=rev*10+last_digit
            n = n // 10
        # return rev                  #595321 but ans should be 123595 Therefore reverse the result again
        return rev_again(rev)

# print(replace_num(123090))
# print(replace_num(0))
#123595
#5

'''Program to check if a number is Positive, Negative, Odd, Even, Zero'''
def check(number):
    if number > 0 :
        print(number,"is Positive")
    elif number == 0:
        print(number,"is Zero")
    else:
        print(number,"is Negative")
    if number % 2==0:
        print("Number is Even")
    else:
        print("Number is odd")
# check(-234552)
# check(-234559)
# check(234552)
# check(234557)
# check(-0)
'''-234552 is Negative
Number is Even
-234559 is Negative
Number is odd
Number is Even
234557 is Positive
Number is odd
0 is Zero
Number is Even'''


'''Harshad (Or Niven) Number
An integer number in base 10 which is divisible by the sum of its digits is said to be a Harshad Number. An n-harshad number is an integer number divisible by the sum of its digit in base n.
Below are the first few Harshad Numbers represented in base 10:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20………
Given a number in base 10, our task is to check if it is a Harshad Number or not.
'''
def harshad(number):
    addn = 0
    temp=number
    while temp>0:
        digits=temp%10
        addn+=digits
        temp = temp //10
    if number % addn == 0:
        print(number,"is Harshad")
    else:
        print(number,"is not a harshad number")
# harshad(2)
# harshad(13)
# harshad(12)
'''
2 is Harshad
13 is not a harshad number
12 is Harshad
'''

'''Program to find GCD or HCF of two numbers'''
#gcd matlab a and b dono ko konsa max number divide krta h
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
# print(gcd(98,59))
#14
'''Time Complexity: O(min(a,b))
Auxiliary Space: O(min(a,b))'''

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
# if gcd(98,56):
#     print(gcd(98,59))
# else:
#     print("Not found")
#14
'''Time Complexity: O(log(min(a,b))
Auxiliary Space: O(log(min(a,b))'''


'''LCM of two numbers'''
#LCM matlb a and b dono k table me konsa least number aata hai
#we know a * b = LCM(a,b) * GCD(a,b)    therefore LCM(a,b) = a*b / GCD(a,b)
def lcm(a,b):
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    lcm=a*b / gcd(a,b)
    return lcm
a,b=15,20
# print(f"LCM of {a} and {b} is {lcm(a,b)}")
#LCM of 15 and 20 is 60.0
'''Time Complexity: O(log(min(a,b))
Auxiliary Space: O(log(min(a,b))'''


'''Program to check Strong Number

Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number, check if it is a Strong Number or not.
Examples: 

Input  : n = 145
Output : Yes
Sum of digit factorials = 1! + 4! + 5!
                        = 1 + 24 + 120
                        = 145
Input :  n = 534
Output : No'''

def strongnum(num):
    def fact(num):
        if num == 0 or num ==1:
            return 1
        else:
            return num * fact(num-1)
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        fact_of_digit=fact(digit)
        sum+=fact_of_digit
        temp=temp//10
    if num % sum ==0:
        print(num,"is a Strong Number")
    else:
        print(num,"is not a Strong Number")
# strongnum(145)
# strongnum(534)
# 145 is a Strong Number
# 534 is not a Strong Number
'''Time Complexity: O(logn)
Auxiliary Space: O(n)'''


'''list to fill factorials of digits from 0 to 9'''
# f=[None]*10
# def fact():
#         f[0]=f[1]=1
#         for i in range(2,10):
#             f[i]=f[i-1]*i


'''Program to check if a given year is leap year'''
def leapyr(yr):
    if yr % 4 == 0 and yr % 100 != 0 or yr % 400 ==0:
        print(yr," is a leap year")
    else:
        print(yr,"is not a leap year")
# leapyr(2000)
#2000  is a leap year
'''Auxiliary Space: O(1)'''

'''Program to add two fractions (Add two fraction a/b and c/d and print answer in simplest form)'''
def gcd(num1,num2):
    if num2==0:
        return num1
    return gcd(num2,num1%num2)
def simplest(n3,d3):
    common_factor=gcd(n3,d3)
    n3=int(n3/common_factor)        
    d3=int(d3/common_factor)
    print(n3 , "/" , d3)
def add_frac(n1,d1,n2,d2):
    # a*b = lcm(a,b) * gcd(a,b)
    d3 = d1 * d2 / gcd(d1,d2)
    n3=n1*(int(d3/d1)) + n2*(int(d3/d2))
    simplest(n3,d3)
# add_frac(1,2,3,9)
#5 / 6

def addfracs(n1,d1,n2,d2):
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def simplify(n,d):
        common_factor=gcd(n,d)
        n=int(n/common_factor)
        d=int(d/common_factor)
        print(n,"/",d)
    n=int(n1*d2 + n2*d1)
    d=int(d1*d2)
    simplify(n,d)
n1,d1,n2,d2=1,2,3,9
# print(f"Addition of {n1}/{d1} and {n2}/{d2} is",end=" ")
# addfracs(n1,d1,n2,d2)
#Addition of 1/2 and 3/9 is 5 / 6
'''Time Complexity: O(log(min(a, b)), where a and b are two integers.
Auxiliary Space: O(1), no extra space required so it is a constant.'''

'''Program for Sum of the digits of a given number'''
def sum_of_digits(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit
        temp=temp // 10
    return sum
num=1234
# print(f"Sum of digits of Number '{num}' is",end=" ")
# print(sum_of_digits(num))
#Sum of digits of Number '1234' is 10
'''Time Complexity : O(logn)
Auxiliary Space: O(1)'''


'''Efficient program to print all prime factors of a given number'''
def primefact(num):
    prime_num=2
    while num>1:
        if num % prime_num == 0:
            print(prime_num,end=" ")
            num=num/prime_num
        else:
            prime_num+=1
# primefact(315)
# primefact(19)
#3 3 5 7
# #19 
'''Time Complexity: This Approach is best for all composite numbers and achieves O(log n) but is O(n) otherwise.
Auxiliary Space: O(1)'''


'''Kth largest factor of number N'''
def klargestfact(num,k):
    for i in range(num,0,-1):
        if num % i == 0:
            k-=1
        if k==0:
            return i
num=12
k=3
# print(f"{k}rd largest factor of {num} is",klargestfact(num,k))
#3rd largest factor of 12 is 4
'''Time Complexity: O(N)          
Auxiliary Space: O(1)'''


'''Perfect Number

A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its positive divisors excluding the number itself. Write a function to check if a given number is perfect or not. '''

def propernum(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum+=i
    if sum==num:
        print(num,"is a Proper Number")
    else:
        print(num,"is not a Proper Number")
# propernum(15)
# propernum(6)
# 15 is not a Proper Number
# 6 is a Proper Number



def propernum(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum+=i
    if sum==num:
        print(num,"is a Proper Number")
def check(num):
    print("Below are the Proper Numbers till 10000")
    for i in range(1,num):
        propernum(i)
# check(10000)
# Below are the Proper Numbers till 10000
# 6 is a Proper Number
# 28 is a Proper Number
# 496 is a Proper Number
# 8128 is a Proper Number

'''Program to print all palindromes in a given range'''
def palindrome(num):
    rev=0
    temp=num
    while temp>0:
        rev = rev * 10 + temp % 10
        temp=temp//10
    if num==rev:
        print(num,end=" ")
def check(a,b):
    print(f"Below are the Palindromes between range{a} and {b}")
    for i in range(a,b+1):
        palindrome(i)
# check(100,2000)
# Below are the Palindromes between range100 and 2000
# 101 111 121 131 141 151 161 171 181 191 202 212 222 232 242 252 262 272 282 292 303 313 323 333 343 353 363 373 383 393 404 414 424 434 444 454 464 474 484 494 505 515 525 535 545 555 565 575 585 595 606 616 626 636 646 656 666 676 686 696 707 717 727 737 747 757 767 777 787 797 808 818 828 838 848 858 868 878 888 898 909 919 929 939 949 959 969 979 989 999 1001 1111 1221 1331 1441 1551 1661 1771 1881 1991
'''Time Complexity:
Time complexity of function to check if a number N is palindrome or not is O(logN).
We are calling this function each time while iterating from min to max.
So the time complexity will be O(Dlog(M)).
Where,
D= max-min
M = max
Auxiliary Space: O(1)'''

'''Program for Armstrong Numbers'''
'''Given a number x, determine whether the given number is Armstrong number or not. 
A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if. 
abcd… = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + …. '''
def armstrong(num):
    num=str(num)
    n=len(num)
    sum=0
    for i in num:
        sum+=int(i)**n
    if int(sum)==int(num):
        print("Armstrong")
    else:
        print("Nope")
# armstrong(1634)
# armstrong(1253)
# Armstrong
# Nope
'''Time Complexity: O(n).
Auxiliary Space: O(1).'''

def armstrong(num):
    count=0
    temp=num
    arr=[]
    while temp>0:
        digit=temp%10
        count+=1
        arr.append(digit)
        temp=temp//10
    sum=0
    for i in arr:
        sum+=i**count
    if sum==num:
        print("Armstrong")
    else:
        print("Nope")
# armstrong(1634)
# armstrong(1253)
#Armstrong
# Nope

def order(x):
    order = 0
    while (x != 0):
        order = order+1
        x = x/10
    return order
def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + r ** n
        temp = temp/10
    if sum1==num:
        print("Armstrong")
    else:
        print("Nope")
# armstrong(1634)
# armstrong(1253)
# Armstrong
# Nope

'''Abundant Number
A number n is said to be an Abundant Number if the sum of all the proper divisors of the number denoted by sum(n) is greater than the value of the number n. And the difference between these two values is called abundance. '''

def abundance(num):
    sum=0
    for i in range(1,num):
        if num % i ==0:
            sum+=i
    if sum>num:
        abun=sum-num
        print(num,"is an Abundant number")
        print("abundance is",abun)
    else:
        print(num,"is not an Abundant number")
# abundance(12)
# abundance(21)
# 12 is an Abundant number
# abundance is 4
# 21 is not an Abundant number


def is_abundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
#     return fctr_sum > n
# print(is_abundant(12))
# print(is_abundant(13))


'''Program to find sum of first n natural numbers'''
def sumofn(n):
    return n*(n+1)/2
n=5
# print(f"Sum of first {n} natural number is ",end=" ")
# print(sumofn(n))
# Sum of first 5 natural number is  15.0
'''Time Complexity: O(1)
Auxiliary Space: O(1)
The above program causes overflow, even if the result is not beyond the integer limit. We can avoid overflow up to some extent by dividing first.'''
 
def sumofn(n):
    #if n is even:
    if n%2==0:
        return (n/2)*(n+1)
    else:
        return ((n+1)/2)*n
n=6
# print(f"Sum of first {n} natural number is ",end=" ")
# print(sumofn(n))
#Sum of first 6 natural number is  21.0


'''Sum of all natural numbers in range L to R'''
def suminrange(L,R):
    def sumofn(n):
        if n%2==0:
            sum=(n/2) * (n+1)
        else:
            sum=((n+1)/2) * n
        return sum
    return sumofn(R)-sumofn(L-1)
# print(suminrange(2,5))
#14.0



'''Primitive Abundant Number'''
'''A number N is said to be Primitive Abundant Number if N is an Abundant number and all its proper divisors are Deficient Numbers. 
The first few Primitive Abundant Numbers are:
20, 70, 88, 104, 272, 304……… '''

'''
A number n is said to be Deficient Number if sum of all the divisors of the number denoted by divisorsSum(n) is less than twice the value of the number n. And the difference between these two values is called the deficiency.
Mathematically, if below condition holds the number is said to be Deficient: 
divisorsSum(n) < 2 * n
deficiency = (2 * n) - divisorsSum(n)
The first few Deficient Numbers are:
1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19 …..'''

def primAbun(n):
    sum=0
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    if sum>n and sum<2*n:
        return True
# n=18
# if(primAbun(n)):
#     print(n,"is Primitive Abundant number")
# else:
#     print(n,"is not a Primitive Abundant number")


import math

# Function to sum of divisors
def getSum(n):
	sum = 0
	
	# Note that this loop
	# runs till square root of N
	for i in range(1, int(math.sqrt(n) + 1)):
		if (n % i == 0):
			
			# If divisors are equal,
			# take only one of them
			if (n // i == i):
				sum = sum + i
			else:
				
				# Otherwise take both
				sum = sum + i
				sum = sum + (n // i)
	return sum

# Function to check Abundant Number
def checkAbundant(n):
	
	# Return True if sum
	# of divisors is greater
	# than N.
	if (getSum(n) - n > n):
		return True
	return False

# Function to check Deficient Number
def isDeficient(n):
	
	# Check if sum(n) < 2 * n
	if (getSum(n) < (2 * n)):
		return True
	return False

# Function to check all proper divisors
# of N is deficient number or not
def checkPrimitiveAbundant(num):
	
	# if number itself is not abundant
	# return False
	if not checkAbundant(num):
		return False
	
	# find all divisors which divides 'num'
	for i in range(2, int(math.sqrt(num) + 1)):
		
		# if 'i' is divisor of 'num'
		if (num % i == 0 and i != num):
			# if both divisors are same then add
			# it only once else add both
			if (i * i == num):
				if (not isDeficient(i)):
					return False
			elif (not isDeficient(i) or
				not isDeficient(num // i)):
				return False
	return True
# n = 18
# if (checkPrimitiveAbundant(n)):
# 	print("Yes")
# else:
# 	print("No")


'''Count prime numbers that can be expressed as sum of consecutive prime numbers
Given an integer N, the task is to find the number of prime numbers up to N that can be expressed as a sum of consecutive primes.
Examples:

Input: N = 45
Output: 3
Explanation:
Below are the prime numbers up to 45 that can be expressed as sum of consecutive prime numbers:

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Therefore, the count is 3. 

Input: N = 4
Output: 0 '''

def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0 or n<=1:
        return False
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
def primeCons(n):
    count=0
    arr=[]

    for i in range(n+1):
        if isPrime(i):
            arr.append(i)
    sum=arr[0]
    print("Array of prime numbers in considered range: ",arr)
    print("Numbers with prime consecutive sum are: ",end=" ")
    for i in range(1,len(arr)):
        sum+=arr[i]
        if sum>n:
            break
        if isPrime(sum):
            count+=1
            print(sum,end=" ")
    return count
n=95
# print("\nPrime consecutive count is :",primeCons(n))
# Array of prime numbers in considered range:  [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
# Numbers with prime consecutive sum are:  5 17 41 
# Prime consecutive count is : 3


'''Fibonacci series'''
def fibo(n):
    f=[0,1]
    for i in range(2,n+1):
        ans = f[i-1]+f[i-2]
        f.append(ans)
    return f
# print(fibo(4))
#[0, 1, 1, 2, 3]

def nthFibo(n):
    a=0
    b=1
    if n==0:
        return a
    if n==1:
        return b
    else:
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
# print(nthFibo(4))
#3
'''Time Complexity:O(n) 
Extra Space: O(1)'''


'''Count ways to reach the nth stair

There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.
Consider the example shown in the diagram. The value of n is 3. There are 3 ways to reach the top. The diagram is taken from Easier Fibonacci puzzles

Examples: 

Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2) 
Recommended PracticeReach the Nth pointTry It!
Method 1: The first method uses the technique of recursion to solve this problem.
Approach: We can easily find the recursive nature in the above problem. The person can reach nth stair from either (n-1)th stair or from (n-2)th stair. Hence, for each stair n, we try to find out the number of ways to reach n-1th stair and n-2th stair and add them to give the answer for the nth stair. Therefore the expression for such an approach comes out to be : 

ways(n) = ways(n-1) + ways(n-2)
The above expression is actually the expression for Fibonacci numbers, but there is one thing to notice, the value of ways(n) is equal to fibonacci(n+1). 

ways(1) = fib(2) = 1
ways(2) = fib(3) = 2
ways(3) = fib(4) = 3
For a better understanding, let’s refer to the recursion tree below -: 

Input: N = 4

                  fib(5)
           '3'  /        \   '2'
               /          \
           fib(4)         fib(3)
     '2'  /      \ '1'   /      \  
         /        \     /        \ 
     fib(3)     fib(2)fib(2)      fib(1) 
     /    \ '1' /   \ '0'
'1' /   '1'\   /     \ 
   /        \ fib(1) fib(0) 
fib(2)     fib(1)
So we can use the function for Fibonacci numbers to find the value of ways(n). Following is C++ implementation of the above idea. '''

# Recursive function to find nth fibonacci number
def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

# Returns no. of ways to reach sth stair
def countWays(s):
	return fib(s + 1)
s = 8
# print ("Number of ways = ",end=" ")
# print (countWays(s))
#Number of ways =  34


'''Largest and smallest digit of a number'''
def largest_smallest(num):
    largest=0
    smallest=0
    temp=num
    while temp>0:
        digit=temp%10
        if digit < smallest:
            smallest=digit
        if digit>largest:
            largest=digit
        temp=temp//10
    print(f"Smallest digit is: {smallest} and Largest digit is: {largest}")
n=739207
# print("The number is:",n)
# largest_smallest(n)
# The number is: 739207
# Smallest digit is: 0 and Largest digit is: 9

'''Square Free Number
Given a number, check if it is square free or not. A number is said to be square free if no prime factor divides it more than once, i.e., largest power of a prime factor that divides n is one. First few square free numbers are 1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34, 35, 37, 38, 39, …
Examples: 
Input : n = 10
Output : Yes
10 can be factorized as 2*5. Since
no prime factor appears more than
once, it is a square free number.

Input :  n = 20
Output : No
20 can be factorized as 2 * 2 * 5.
Since prime factor appears more than
once, it is not a square free number.'''
def isSquareFree(n):
     
    if n % 2 == 0:
        n = n / 2
 
    # If 2 again divides n, then n is not a square free number.
    if n % 2 == 0:
        return False
 
    # n must be odd at this point. So we can skip one element (Note i = i + 2)
    for i in range(3, int(math.sqrt(n) + 1)):
         
        # Check if i is a prime factor
        if n % i == 0:
            n = n / i
 
        # If i again divides, then n is not square free
        if n % i == 0:
            return False
    return True
# n=20
# if (isSquareFree(n)):
#     print(n,"is Square free")
# else:
#     print(n,"isnt Sqaure free")
# 20 isnt Sqaure free
'''Time Complexity : O(sqrt(N)) 
In the worst case when the number is a perfect square, then there will be sqrt(n)/2 iterations .'''

def isSqfree(n):
    if n%2==0:
        n=n/2
    if n%2==0:
        return False
    for i in range(3,int(math.sqrt(n))+1):
        if n%i==0:
            n=n/i
        if n%i==0:
            return False
    return True
n=20
# if(isSqfree(n)):
#     print(n,"is Square free")
# else:
#     print(n,"isnt Sqaure free")
# 20 isnt Sqaure free



'''Permutations to arrange N persons around a circular table'''
'''arranging n people in circular manner can be done in (n-1) factorial ways'''
def arrange(n):
    ans=1
    while n>0:
        ans=ans*n
        n-=1
    return ans
n=4
# print(arrange(n-1))
#6
'''Time Complexity: O(N) where N is the number of persons.
Auxiliary Space: O(1)'''

''''''

def fact(n):
    # ans=1
    # while n>0:
    #     ans=n*fact(n-1)
    # return ans
    return n*fact(n-1)
n=5
# print(arrange(n-1))
#24

'''Check if a prime number can be expressed as sum of two Prime Numbers
Input : N = 13
Output : Yes
Explanation : The number 13 can be written as 11 + 2, 
here 11 and 2 are both prime.

Input : N = 11
Output : No
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Simple Solution: A simple solution is to create a sieve to store all the prime numbers less than the number N. Then run a loop from 1 to N and check whether i   and n-i   are both prime or not. If yes then print Yes, else No.

Efficient solution: Apart from 2, all of the prime numbers are odd. So it is not possible to represent a prime number (which is odd) to be written as a sum of two odd prime numbers, so we are sure that one of the two prime number should be 2. So we have to check whether n-2 is prime or not. If it holds we print Yes else No.
For example, if the number is 19 then we have to check whether 19-2 = 17 is a prime number or not. If 17 is a prime number then print yes otherwise print no.
'''

def isPrime(n):
    if n==2 or n==3 :
        return True
    if n<=1 or n%2==0 or n%3==0:
        return False
    i=5
    while(i*i<n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True
def sumofPrime(n):
    if isPrime(n) and isPrime(n-2):
        return True
    return False
n=19
# if(sumofPrime(n)):
#     print("Can be expressed ")
# else:
#     print("Cannot be expressed")
#Can be expressed 


'''Program to find area of a circle'''
def area(r):
    return 3.142*r*r
print(area(5))
#78.55


'''Program to find the Roots of Quadratic equation'''
def findRoots(a, b, c):

	# If a is 0, then equation is
	# not quadratic, but linear
	if a == 0:
		print("Invalid")
		return -1
	d = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(d))

	if d > 0:
		print("Roots are real and different ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))
	elif d == 0:
		print("Roots are real and same")
		print(-b / (2*a))
	else: # d<0
		print("Roots are complex")
		print(- b / (2*a), " + i", sqrt_val/ (2 * a))
		print(- b / (2*a), " - i", sqrt_val/ (2 * a))

a = 1
b = -7
c = 12
findRoots(a, b, c)
# Roots are real and different 
# 4.0
# 3.0
'''Time Complexity: O(log(D)), where D is the discriminant of the given quadratic equation.
Auxiliary Space: O(1)'''