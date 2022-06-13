
# Find Pair with given sum in the Array

# Method-1 
# Time and Space O(n),O(n)

def countpairs(arr,targetsum):
    set_num=set()
    n=len(arr)
    count=0
    for i in range(n):
        req_num = targetsum-arr[i]
        if(req_sum in set_num):
            count+=1
        set_num.add(arr[i])
    return count



# Method-2
# Time and Space O(nlogn),O(1)

def count_pairs(arr,target_sum):
    arr.sort()
    n=len(arr)
    left=0
    right=n-1
    count=0
    while(left<right):
        curr_sum=arr[left]+arr[right]
        if(curr_sum==target_sum):
            count+=1
            left+=1
            right-=1
        elif curr_sum > target_sum:
            right-=1
        else:
            left+=1
    return count        


## Check_Subarray_wid_0

def check_sub(arr):
    n=len(arr)
    prefix_sum=[0]*n
    for i in range(n):
        if i==0:
            prefix_sum[i]=arr[i]
        else:
            prefix_sum[i]=arr[i]+prefix_sum[i-1]
    set_pre=set()
    for i in range(n):
        if (prefix_sum[i] in set_pre):
            return True
        set_pre.add(prefix_sum[i])
    if 0 in set_pre:
        return True
    else:
        return False


## Find Duplicates

    # Method-1
#time: O(n) and space: O(n)

def findDupli(arr):
    set={}
    n=len(arr)
    for i in range(n):
        if arr[i] in set:
            return arr[i]
        set.add(arr[i])
    


# Method-2
# time: O(n) and space: O(1)

def findDupli(arr):
    xor_val=arr[0]
    n=len(arr)
    for i in range(1,n):
        xor_val = xor_val ^ arr[i]
    for i in range(1,n):
        xor_val = xor_val ^ i
    return xor_val


## Sort Binary Array

# Method-1

def sortBinaryArray(arr):
    n=len(arr)
    zeroes=0
    for i in range(n):
        if arr[i]==0: 
            zeroes+=1
    for i in range(n):
        if zeroes:
            arr[i]=0
        else:
            arr[i]=1
    return arr



# Method-2

def sortBinaryArray(arr):
    n=len(arr)
    start=0
    for i in range(n):
        if arr[i]==0:
            arr[i],arr[start]=arr[start],arr[i]
            start+=1
    return arr



## Triplet Sum

def tripletSum(a,targetsum):
    n=len(a)
    for i in range(n):
        #a[i]
        map=set()
        for j in range(i+1,n):
            req_num = targetsum - (a[i]+a[j])
            if req_num in map:
                return [a[i],req_num,a[j]]
            map.add(a[j])
    return False


## Equilibrium Index 

def equilibriumIndex(A):
    n=len(A)
    for i in range(1,n):
        A[i]=A[i]+A[i-1]
    for idx in range(n):
        # left hand side sum 0 to idx-1
        right=idx-1
        left_sum=A[right]
        # right hand side sum  idx+1 to n-1
        left=idx+1
        right=n-1
        if idx==n-1:
            right_sum=0
        right_sum=A[right]-A[left-1]

        if left_sum==right_sum:
            return idx
    return -1


# Maximum Product Subset
def maxProductSubset(a):
    n=len(a)
    product=1
   
    for i in range(n):
        if a[i]==0:
            
            continue
        else:
            product *= a[i]
            
    if product > 0:
        return product
    

    
    else:
        maxNeg = float("-inf")
        for i in range(n):
            if(a[i]<0):
                 maxNeg = max(maxNeg,a[i])
        return (product // maxNeg)


## Maximum product subarray

def maxProduct(arr,n):
    minPro=arr[0]
    maxPro=arr[0]
    ans=arr[0]
    for i in range(1,n):
        ch=maxPro * arr[i]
        ch_=minPro * arr[i]
        maxPro = max(arr[i],max(ch,ch_))
        minPro = min(arr[i],min(ch,ch_))
        ans=max(ch,ans)
    return ans

## Maximum Sum Subarray

def maxSumSubarray(arr,n):
    s=arr[0]
    max_s=arr[0]
    for i in range(1,n):
        s+=arr[i]
        max_s = max(s,max_s)
        if (s<0):
            s=0
    return max_s


## Array subset of another array

def arrsubset(arr1,arr2,n,m):
    hs=set()
    for i in range(n):
        if arr1[i] not in hs:
            hs.add(arr1[i])
    for i in range(m):
        if arr2[i] not in hs:
            return False
    return True


## leaders Array

def printLeaders(arr, size):
    
    max_from_right = arr[size-1]  
    print (max_from_right,end=' ')   
    for i in range( size-2, -1, -1):       
        if max_from_right < arr[i]:       
            print (arr[i],end=' ')
            max_from_right = arr[i]
         
# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))


## Intersection of ARrays

def intersectionarr(arr1,arr2):
    hs=set()
    inter=set()
    for i in arr1:
        if i not in hs:
            hs.add(i)
    for i in arr2:
        if i in hs:
            inter.add(i)
    return inter

## Union of Arrays

def doUnion(self,a,n,b,m):
        i=0
        j=0
        
        l=[]
        while i<n and j<m:
            if(a[i]<b[j]):
                if(a[i] not in l):
                    l.append(a[i])
                i+=1
            elif(b[j]<a[i]):
                if(b[j] not in l):
                    l.append(b[j])
                j+=1
            else:
                if(a[i] not in l):
                    l.append(a[i])
                i+=1
                j+=1
        
        while i<n:
            if(a[i] not in l):
                l.append(a[i])
            i+=1
        while j<m:
            if(b[j] not in l):
                l.append(b[j])
            j+=1
        return len(l)


def sortedOrNot(arr):
    if len(arr)==1 or len(arr)==0:
        return True
    return arr[0]<arr[1] and sortedOrNot(arr[1:])
    


