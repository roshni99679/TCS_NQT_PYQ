'''Program to count vowels, consonant, digits and special characters in string.'''

from re import I
from telnetlib import OUTMRK


def count(str):
    n=len(str)
    vowels=0
    consonants=0
    digit=0
    specialchar=0
    
    for i in range(n):
        ch=str[i]
        ch.lower()
        #check if a character is an alphabet or Number
        if "a"<=ch<="z" or "A"<=ch<="Z":
            # vowels=["a","i","e","o","u"]
            if ch =="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
                vowels+=1
            else:
                consonants+=1
        elif "0"<=ch<="9":
            digit+=1
        else:
            specialchar+=1
    print("Number of vowels:",vowels)
    print("Number of consonants:",consonants)
    print("Number of digits:",digit)
    print("Number of specialcharacter:",specialchar)
# count("abcdefghijklmnopqrstuvwxyz0123456789 ,./#@")
# Number of vowels: 5
# Number of consonants: 21
# Number of digits: 10
# Number of specialcharacter: 6
'''Time Complexity: O(N)
Auxiliary Space: O(1)'''


'''Program to Check if a Given String is Palindrome'''

def palindrome(str):
    n=len(str)
    for i in range(n):
        if str[i]!=str[(n-1)-i]:
            print("Not a Palindrome")
            return
    print("palindrome")  
# palindrome("abbcbba") 
# palindrome("abbcdgsvbba")
# palindrome("cdcddcdc")

# palindrome
# Not a Palindrome
# palindrome

def pal(str):
    n=len(str)
    for i in range(n):
        if str[i]!=str[(n-1)-i]:
            return "Not a palindrome"
    return "Palindrome"
# palindrome("abbcbba") 
# palindrome("abbcdgsvbba")
# palindrome("cdcddcdc")

# palindrome
# Not a Palindrome
# palindrome

'''Program to print ASCII Value of a character'''
def ascii(char):
    asc=ord(char)
    return asc
# print(ascii("A"))   #65
# print(ascii("a"))   #97

def ascii(str):
    n=len(str)
    for i in range(n):
        ch=str[i]
        asc=ord(ch)
        print("Ascii value of",ch,"is",asc)
# ascii("ABCDabcd @!")
# Ascii value of A is 65
# Ascii value of B is 66
# Ascii value of C is 67
# Ascii value of D is 68
# Ascii value of a is 97
# Ascii value of b is 98
# Ascii value of c is 99
# Ascii value of d is 100
# Ascii value of   is 32
# Ascii value of @ is 64
# Ascii value of ! is 33

'''Program to remove vowels from a String'''
def rem(str):
    n=len(str)
    vowels=["a","e","i","o","u"]
    for i in range(n):
        if str[i] in vowels:
            result=[letter for letter in str if letter.lower() not in vowels]
            result=''.join(result)
    print(result)
# rem("AEIOUHELLOBABYaeiou")
#HLLBBY

'''Time Complexity: O(n), where n is the length of the string
Space Complexity: O(1)'''


'''Remove spaces from a given string'''
def remspaces(str):
    n=len(str)
    mylist=[]
    for i in range(n):
        if str[i]!=" ":
            mylist.append(str[i])
    return ''.join(mylist)
str="My na me is Ros hni Gup ta"
# print(remspaces(str))
#MynameisRoshniGupta
'''Time complexity of above solution is O(n)'''


'''Remove characters from the first string which are present in the second string'''
def remChar(str1,str2):
    mylist=[]
    for ch in str1:
        if ch not in str2:
            mylist.append(ch)
    return ''.join(mylist)
str1="geeksforgeeks"
str2="geks"
# print(remChar(str1,str2))
#for


'''Remove all characters other than alphabets from string'''
def remOtherThanAlpha(str):
    n=len(str)
    mylist=[]
    for i in range(n):
        if "a"<=str[i].lower()<="z":
            mylist.append(str[i])
    return ''.join(mylist)
# print(remOtherThanAlpha("P&ra+$BHa;;t*ku, ma$r@@s#in}gh"))
#PraBHatkumarsingh

''''''
def revStr(str):
    n=len(str)
    i=len(str)-1
    while i>=0:
        print(str[i],end="")
        i-=1
str="roshni"
# revStr(str)
#inhsor

def rev(str):
    print(str[::-1])
# rev("Roshni")
#inhsoR


'''Calculate sum of all numbers present in a string'''
def sumofnum(str):
    n=len(str)
    sum=0
    for i in range(n):
        ch=str[i]
        if "a"<=ch.lower()<="z":
            continue
        else:
            sum+=int(ch)
    return sum
# print(sumofnum("123fhvbjkdl67khf3vjhk9"))
#31

''''''
def capitalizemystr(str):
    mylist=list(str.split(" "))
    new=[]
    for i in range(len(mylist)):
        x=mylist[i]
        # print(x,len(x))
        for j in range(len(x)):
            # print(x[j].upper() if j==0 or j==len(x)-1 else x[j].lower() , end='')
            if j==0 or j==len(x)-1:
                new.append(x[j].upper())
            else :
                new.append(x[j].lower())
    return ''.join(new)

# print(capitalizemystr("roshni guPta"))
# capitalizemystr("roshni guPta")

# Python3 program to capitalise the first
# and last character of each word in a string.
def FirstAndLast(string) :
	
	# Create an equivalent char array
	# of given string
	ch = list(string);
	
	i = 0 ;
	while i < len(ch):

		# k stores index of first character
		# and i is going to store index of last
		# character.
		k = i;
		
		while (i < len(ch) and ch[i] != ' ') :
			i += 1;

		# Check if the character is a small letter
		# If yes, then Capitalise
		if (ord(ch[k]) >= 97 and
			ord(ch[k]) <= 122 ):
			ch[k] = chr(ord(ch[k]) - 32);
		else :
			ch[k] = ch[k]
			
		if (ord(ch[i - 1]) >= 90 and
			ord(ch[i - 1]) <= 122 ):
			ch[i - 1] = chr(ord(ch[i - 1]) - 32);
		else :
			ch[i - 1] = ch[i - 1]
			
		i += 1
		
	return "" . join(ch);
	
# Driver code
if __name__ == "__main__" :
	
	string = "Geeks for Geeks";
	
	# print(string);
	# print(FirstAndLast(string));
	
# This code is contributed by Ryuga



'''Print characters and their frequencies in order of occurrence'''

def countfreq(str):
    n=len(str)
    hm={}
    #count freq of each char and store it in a dict
    for i in range(n):
        if str[i] not in hm:
            hm[str[i]]=0
        hm[str[i]]+=1
    #print char and its occurence from dict  
    for i in str:
        if hm[i]!=0:
            print("{}{}".format(i,hm[i]),end=" ")
            hm[i]=0
# countfreq("geeksforgeeks")
# countfreq("elephant")
# g2 e4 k2 s2 f1 o1 r1
#e2 l1 p1 h1 a1 n1 t1


'''Given a string, find its first non-repeating character'''
def nonrep(str):
    n=len(str)
    hm={}
    #count freq of each char and store it in a dict
    for i in range(n):
        if str[i] in hm:
            hm[str[i]]+=1
        else:
            hm[str[i]]=1
    for i in range(n):
        if hm[str[i]]==1:
            print("First Non repeating character is:",str[i]) 
            return   
# nonrep("elephant")
#First Non repeating character is: l
'''
Time Complexity: O(n). 
As the string need to be traversed at-least once.
Auxiliary Space: O(1). 
Space is occupied by the use of count_array/hash_map to keep track of frequency.
'''

'''Program to find Smallest and Largest Word in a String'''
def findsl(str):
    l=list(str.split(" "))
    hm={}
    for x in l:
        hm[x]=len(x)
    # print(hm)
    a,b= min(hm.values()),max(hm.values())  # a=min len , b=max len
    for x in hm:
        if hm[x]==a:                        #if value of any key is a (min len):
            print("Smallest word is:",x)
        elif hm[x]==b:                      #if value of any key is b (max len):
            print("Largest word is:",x)
# findsl("This is a test string")
# Smallest word is: a
# Largest word is: string


'''Check whether two strings are anagram of each other'''

'''Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
For example, 
“abcd” and “dabc” are an anagram of each other
“listen” and “silent” are an anagram of each other
'''
def anagram(str1,str2):
    n1=len(str1)
    n2=len(str2)
    if n1==n2:
        for i in range(n1):
            if str1[i] not in str2:
                return "Not anagram"
            else:
                return "Anagram"
str1="SILENT"
str2="LISTEN"
str3="ABCDEF"
# print(str1,"and",str2,"are",anagram(str1,str2))
# print(str1,"and",str3,"are",anagram(str1,str3))
# SILENT and LISTEN are Anagram
# SILENT and ABCDEF are Not anagram


'''Sort string of characters'''
def sortstr(str):
    n=len(str)
    hm={}
    str=sorted(str)
    for i in range(n):
        if str[i] not in hm:
            hm[str[i]]=0
        hm[str[i]]+=1
    for k,v in hm.items():
        print(k*v,end="")
# sortstr("aaaabbbzccccc")


MAX_CHAR = 26
# function to print string in sorted order
def sortString(str):
      
    # Hash array to keep count of characters.
    # Initially count of all characters is 
    # initialized to zero.
    charCount = [0 for i in range(MAX_CHAR)]
    print(charCount)
    # Traverse string and increment 
    # count of characters
    for i in range(0, len(str), 1):
          
        # 'a'-'a' will be 0, 'b'-'a' will be 1,
        # so for location of character in count 
        # array we will do str[i]-'a'.
        charCount[ord(str[i]) - ord('a')] += 1
        print(charCount)
      
    # Traverse the hash array and print 
    # characters
    for i in range(0, MAX_CHAR, 1):
        for j in range(0, charCount[i], 1):
            print(chr(ord('a') + i), end = "")
  
# Driver Code
if __name__ == '__main__':
    s = "geeksforgeeks"
    # sortString(s)

def sortstr(str):
    maxchar=26                              #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    chararr=[0 for i in range(maxchar)]
    for i in range(len(str)):
        chararr[ord(str[i])-ord('a')]+=1    
        # [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 3, 1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 4, 1, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 4, 1, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 4, 1, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0]
    for i in range(maxchar):
        for j in range(chararr[i]):
            print(chr(ord('a')+i),end="")
# sortstr("geeksforgeeks")

'''Convert characters of a string to opposite case'''
def oppcase(str):
    for i in range(len(str)):
        if "a"<=str[i]<="z":
            #convert to uppercase
            str[i] = chr(ord(str[i]) - 32)
        elif "A"<=str[i]<="Z":
            #convert to lowercase
            str[i] = chr(ord(str[i]) + 32)
    return ''.join(str)
str="RoshnI GupTA"
str=list(str)
# print(str)      #['R', 'o', 's', 'h', 'n', 'I', ' ', 'G', 'u', 'p', 'T', 'A']
# print(oppcase(str))
#rOSHNi gUPta


'''Count words in a given string'''
def countwords(str):
    n=len(str)
    state=0
    word_count=0
    for i in range(n):
        if str[i]==" " or str[i]=="\n" or str[i]=="\t":
            state=0
        elif state==0:
            state=1
            word_count+=1
    return word_count
# print(countwords("Roshni Gupta \n THREE \t four"))
#4
'''Time complexity: O(n)
Auxiliary Space: O(1)'''

'''Return maximum occurring character in an input string'''
def maxch(str):
    hm={}
    n=len(str)
    for i in range(n):
        if str[i] not in hm:
            hm[str[i]]=0
        hm[str[i]]+=1
    maxchar=max(hm.values())
    for i in hm:
        if hm[i]==maxchar:
            return i
# print("Max occuring character is:",maxch("abccccccdavrfkjhabjfvtva"))
#Max occuring character is: c


def maxch(str):
    c=''
    ASCII_SIZE=256
    count=[0]*ASCII_SIZE
    # print(count)
    max=-1
    for i in str:
        count[ord(i)]+=1
        # print(count)  
    for i in str: 
        if max<count[ord(i)]:
            max=count[ord(i)]
            c=i
    return c
# print("Max occuring character is:",maxch("abccccccdavrfkjhabjfvtva"))
#Max occuring character is: c

'''Remove duplicates from a given string'''
def remdups(str):
    n=len(str)
    s=set()
    res=''
    for i in range(n):
        s.add(str[i])
    for i in s:
        res+=i
    print(res,end="")
# remdups("roshnirosh")
#nirsoh
'''Time Complexity: O(n) 
Auxiliary Space: O(n)
It does not keep the order of elements the same as the input but prints them in sorted order.'''


def dups(str):
    n=len(str)
    temp=""+str[0]
    for i in range(1,n):
        if str[i] not in temp:
            temp=temp+str[i]
    return temp
# print(dups("roshnirosh"))
#roshni
'''
Time Complexity : O(n) 
Auxiliary Space: O(n)
'''

'''print Duplicate characters'''
def dups(str):
    hm={}
    n=len(str)
    for i in range(n):
        if str[i] not in hm:
            hm[str[i]]=0
        hm[str[i]]+=1
    for k,v in hm.items():
        if v>1:
            print(k,"count:",v)
# dups("hello pello")
# e count: 2
# l count: 4
# o count: 2
'''
Time Complexity: O(N), where N = length of the string passed and it takes O(1) time to insert and access any element in an unordered map
Auxiliary Space: O(K), where K = size of the map (0<=K<=input_string_length).'''



'''Lexicographically next string'''
'''Input : geeks
Output : geekt
The last character 's' is changed to 't'.

Input : raavz
Output : raawz
Since we can't increase last character, 
we increment previous character.

Input :  zzz
Output : zzza'''

def lexo(str):
    n=len(str)
    #if len of string is 0 , just return a
    if n==0:
        return 'a'
    #if len of str is non zero then traverse the string from end to beginning index and check wheather it contains all z 
    i=n-1
    while str[i]=="z" and i>=0:
        i-=1
    #i == -1 implies string contains all z , thus append a after the string
    if i==-1:
        str=str+'a'
    #replace that first str[i] from end with the character next to it if str contains a non z char
    else:
        str=str.replace(str[i],chr(ord(str[i])+1))
    return str
# print(lexo("zzzz"))         #zzzza
# print(lexo("zscz"))         #zsdz
# print(lexo(""))             #a
    
'''Check if a string is substring of another'''
def substr(str1,str2):
    if str1 in str2:
        return str2.index(str1)
    else:
        return -1
str1="G"
str2="Roshni Gupta"
res=substr(str1,str2)
# if res==-1:
#     print(f"{str1} is not in {str2}")
# else:
#     print(f"{str1} is present at index {res} in {str2}")
#Gupta is present at index 7 in Roshni Gupta

def substr(s1,s2):
    n=len(s1)
    counter=0
    i=0
    while i<n:
        if len(s2)==counter:
            break
        if s2[counter]==s1[i]:
            counter+=1
        else:
            if counter>0:
                i=i-counter
            counter=0
        i+=1
    if counter<len(s2):
        return -1
    else:
        return i-counter
# print(substr("tit for tat","for"))
#4

'''Reverse words in a given string'''
def revwords(str):
    mylist=list(str.split(" "))
    return ' '.join(mylist[::-1])
    # print(mylist[::-1],end=" ")
ans=revwords("Rosh is my name")
# print(ans)
#ROSH IS NAME MY

def revwords(str):
    s=str.split()[::-1]
    return ' '.join(s)
ans=revwords("Rosh is my name")
# print(ans)
#name my is Rosh


'''String matching where one string contains wildcard characters

Given two strings where first string may contain wild card characters and second string is a normal string. Write a function that returns true if the two strings match. The following are allowed wild card characters in first string. 

* --> Matches with 0 or more instances of any character or set of characters.
? --> Matches with any one character.
For example, “g*ks” matches with “geeks” match. And string “ge?ks*” matches with “geeksforgeeks” '''

def wildcard(str1,str2):
    n1=len(str1)
    n2=len(str2)
    #star condition 
    if n2==n1+1:
        for i in range(n1):
            if str1[i]=="*":
                ind=i
        if str2[ind]==str2[ind+1]:
            return "True"
        else:
            return "False"
    else:
        return "False"
str1="g*gle"
str2="google"
print(wildcard(str1,str2))
#True


    