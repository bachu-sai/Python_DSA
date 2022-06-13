
# Reverse String

ip_str='alekhya'
ip_str=list(ip_str)
i=0
j=len(ip_str)-1
while i<j:
    ip_str[i],ip_str[j]=ip_str[i],ip_str[j]
    i+=1
    j-=1
ip_str=''.join(ip_str)
print(ip_str)


# Max Occur String

def max_occur(ip_str):
    count={}
    for i in ip_str:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    maxi=-1
    ans=''
    for char,fre in count:
        if(fre>maxi):
            maxi=fre
            ans=char
    return ans


# Remove Character From String

def remove_char(ip_str,chr):
    ip_str=list(ip_str)
    i=0
    while i<len(ip_str):
        if ip_str[i]==chr:
            ip_str.pop(i)
        else:
            i+=1
    ip_str=''.join(ip_str)
    return ip_str


 # Duplicate Characters
def dupliChar(ip_str):
     c={}
     ans=[]
     for i in ip_str:
         if i in c:
             c[i]+=1
         else:
             c[i]=1
     for ch,co in c.items():
         if co>1:
             ans.append(ch)
     return ans
    

# Remove ALl Duplicates

def removeAllDupli(ip):
    count={}
    for i in ip:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    ip=list(ip)
    i=0
    while i<len(ip):
        if count[ip[i]]>1:
            ip.pop(i)
        else:
            i+=1
    ip=''.join(ip)
    return ip


# Check Substring

def isSubstring(s1,s2):
    t=0
    l=len(s1)
    for i in range(l):
        if t==len(s2):
            break
        if s1[i]==s2[t]:
            t+=1
        else:
            t=0
    if t<len(s2):
        return -1
    else:
        return i-t


# Anagram

def areanagrams(s1,s2):
    c1=[0]*256
    c2=[0]*256
    for i in s1:
        c1[ord[i]]+=1
    for i in s2:
        c2[ord[i]]+=1

    if(len(s1)!=len(s2)):
        return 0

    for i in range(256):
        if(c1[i]!=c2[i]):
            return 0
    return 1

# First Non Repeating
def firstNonRepeating(ip):
    count={}
    for i in ip:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1

    ans=' '
    for i in ip:
        if count[i]==1:
            ans=i
    return ans


# Check palindrome

def checkPal(ip_str):
    i=0
    j=len(ip_str)-1
    while i<j:
        if ip_str[i]!=ip_str[j]:
            return False
        i+=1
        j-=1
    return True    


# Is ALl Unique

def isAllUnique(ip_str):
    count={}
    for i in ip_str:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for char,c in count.items():
        if c!=1:
            return False
    return True



        
