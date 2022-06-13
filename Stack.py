

class Stack:
    def __init__(self):
        self.st=[]

    def push(self,data):
        self.st.append(data)

    def pop(self):
        popELe=-1
        if len(self.st)>0:
            popELe=self.st.pop(-1)
        return popELe

    def print(self):
        for i in range(len(self.st)-1,-1,-1):
            print(self.st[i],end=" ")
        print()
    
s=Stack()
values=[1,2,3,4,5]
for i in values:
    s.push(i)

s.print()


## QUEUE

class Queue:
    def __init__(self):
        self.q=[]

    def enqueue(self,data):
        self.q.append(data)

    def dequeue(self):
        popEle=-1
        if len(self.q)>0:
            popEle.pop(0)
        return popEle

    def print(self):
        for i in self.q:
            print(i,end=' ')
        print()


qu=Queue()
qu.enqueue(5)
qu.enqueue(6)
qu.enqueue(7)
qu.enqueue(8)
qu.dequeue()
qu.print()


# Paranthesis Checker

def paranthesisChecker(exp):
    stack=[]
    for c in exp:
        if c in ['(','[','{']:
            stack.append(c)
        elif c in [')','}',']']:

            if not stack:
                return False
            popEle=stack.pop()
            if popEle=='(':
                if c !=')':
                    return False
            if popEle=='[':
                if c !=']':
                    return False
            if popEle=='{':
                if c !='}':
                    return False
    if stack:
        return False
    return True
exp='[{()}]'
print(paranthesisChecker(exp))




# Next Greater Right

def nextGreaterRight(arr):
    op=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            op.append(-1)
        if stack[-1]>arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]<arr[i]:
                stack.pop()
            if len(stack)==0:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(arr[i])
    op.reverse()
    return op

arr=[1,3,2,4]
op=solve(arr)
print(op)


# Next Greater Left

def nextGreaterLeft(arr):
    op=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            op.append(-1)
        if stack[-1]>arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]<arr[i]:
                stack.pop()
            if len(stack)==0:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(arr[i])
    
    return op

arr=[1,3,2,4]
op=solve(arr)
print(op)


# Next Smaller Right


def nextSmallerRight(arr):
    op=[]
    stack=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            op.append(-1)
        if stack[-1]<arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]>arr[i]:
                stack.pop()
            if len(stack)==0:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(arr[i])
    op.reverse()
    return op

arr=[1,3,2,4]
op=solve(arr)
print(op)

# Next Smaller Left


def nextSmallerLeft(arr):
    op=[]
    stack=[]
    for i in range(len(arr)):
        if len(stack)==0:
            op.append(-1)
        if stack[-1]<arr[i]:
            op.append(stack[-1])
        else:
            while len(stack)>0 and stack[-1]>arr[i]:
                stack.pop()
            if len(stack)==0:
                op.append(-1)
            else:
                op.append(stack[-1])
        stack.append(arr[i])
    
    return op

arr=[1,3,2,4]
op=solve(arr)
print(op)


                        

            