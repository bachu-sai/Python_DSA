
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insertNode(head,i):
    if head is None:
        head = Node(i)
        return head
    curr=head
    while curr:
        if curr.next==None:
            break
        curr=curr.next
    curr.next=Node(i)
    return head
        
def PrintList(head):
    curr=head
    while curr:
        print(curr.data )
        curr=curr.next
    
    
        
if __name__=='__main__':
    head=None
    nodes=[6,8,7,9,4,3,5]
    for i in nodes:
        head=insertNode(head,i)
    PrintList(head)

## Creation of LinkedList

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
first = Node(56)
second = Node(332)
third = Node("alee")

## Linking of nodes
head=first
first.next=second
second.next=third

printLinkedList(head)

def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current=current.next



def insertAtStart(root):
    newnode = Node(89)
    curr=head
    head=newnode
    newnode.next=curr
    return head

def insertAtEnd(root):
    newnode = Node(123)
    curr=head
    while curr:
        if curr.next == None:
            break
        curr=curr.next
    curr.next=newnode
    return head


def insertNodeInSortedLinkedList(head,newnode):
    prev=head
    curr=head
    while curr:
        if curr.data >= newnode.data:
            prev.next=newnode
            newnode.next=curr
            break
        else:
            prev=curr
            curr=curr.next
    return head


def removeDupliSortedLinkedList(head):
    curr=head
    while curr.next:
        if curr.data==curr.next.data:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head


def mergeList(head1,head2):
    head3 = Node(-1)
    node=head3

    while True:
        if head1 is None:
            node.next=head2
            break
        if head2 is None:
            node.next=head1
            break

        if head1.data<=head2.data:
            node.next=head1
            head1=head1.next
        else:
            node.next=head2
            head2=head2.next
        
        node=node.next
    
    return head3.next




def intersection_List(first,second):
    res_head=None
    curr=None
    while first and second:
        if first.data == second.data:
            if res_head is None:
                res_head=first
                curr=first
            else:
                curr.next=first
                curr=first

            first=first.next
            second=second.next
        elif first.data<second.data:
            first=first.next
        else:
            second=second.next
    return res_head



def kthNodeFromEnd(head,k):
    fast=head
    slow=head
    while k:
        k-=1
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    return slow


def splitLL(head):
    curr=head
    A=None
    B=None
    c=0
    while curr:
        if c%2==0:
            if A is None:
                A=curr
                currA=curr
            else:
                currA.next=curr
                currA=curr
        else:
            if B is None:
                B=curr
                currB=curr
            else:
                currB.next=curr
                currB=curr
        curr=curr.next
        c+=1
    return (A,B)


def reverseLinkedList(head):
    prev=None
    curr=head
    while curr:
        nextNode = curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    return prev

def reverseLLRecur(head):
    curr=head
    if(curr is None):
        return
    if(curr.next is None):
        head=curr
        return
    reverseLLRecur(curr.next)
    curr.next.next=curr
    curr.next=None

def reverseKGroups(head,k):
    c=0
    prev=None
    curr=head
    while curr and c<k:
        c+=1
        nextNode = curr.next
        curr.next=prev
        prev=curr
        curr=nextNode
    # VVIMP
    head.next = reverseKGroups(curr,k)
    return prev


def Palindrome(head):
    fast=head
    slow=head
    prev=None
    even=0
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    if fast is None:
        even=1
    if even==0:
        slow=slow.next
    prev.next=None
    slow=reverseLinkedList(slow)
    return compareValues(head,slow)

def compareValues(first,second):
    while first:
        if first.data==second.data:
            first=first.next
            second=second.next
        else:
            return False
    return True
    

def detectCycle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def CountLoop(slow):
    curr=slow
    c=1
    while curr.next!=slow:
        c+=1
        curr=curr.next
    return c

def lenOfLoop(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if(slow==fast):
            return CountLoop(slow)
    return 0


def moveLastNodeToFirst(head):
    if head is None or head.next is None:
        return  head
    prev=head
    curr=head
    while curr.next:
        prev=curr
        curr=curr.next
    prev.next=None
    curr.next=head
    head=curr
    return head


def removeDupliUnsorted(head):
    mySet=set()
    prev=None
    curr=head
    while curr:
        val=curr.data
        if val not in mySet:
            mySet.add(val)
            prev=curr
        else: # val in set
            prev.next=curr.next
        ##VVIMP
        curr=prev.next
    return head
    


def addDigitLL(head,digit):
    head=reverseLinkedList(head)
    carry=digit
    curr=head
    while carry>0:
        totalval= curr.data+carry
        curr.data = totalval % 10
        carry = totalval // 10
        if curr.next is None:
            break
        curr=curr.next
    if carry>0:
        curr.next=Node(carry)
    head=reverseLinkedList(head)
    return head


def addTwoLL(head1,head2):
    head1=reverseLinkedList(head1)
    head2=reverseLinkedList(head2)
    carry=0
    head,curr=None,None
    while head1 or head2:
        tot=0
        if head1:
            tot += head1.data
            head1=head1.next
        if head2:
            tot += head2.data
            head2=head2.next
        
        tot += carry
        newnode = Node(tot % 10)
        carry = tot // 10

        if head is None:
            head = newnode
            curr=newnode
        else:
            curr.next=newnode
            curr=newnode
    if carry>0:
        curr.next= Node(carry)

    ## VVIMP
    head=reverseLinkedList(head)
    return head



def implementStack():
    obj=Stack()
    obj.push(12)
    obj.push(15)
    obj.pop()
    obj.pop()
    obj.peek()
    
class Stack:
    def __init__(self):
        self.top=None
        self.length=0
    def push(self,value):
        newnode=Node(value)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode
        self.length+=1
    
    def pop(self):
        if self.top is None:
            return "Stack Undeflow"
        val=self.top
        self.top=self.top.next
        return val.data
    def peek(self):
        if self.top is None:
            return -1
        topval=self.top.data
        return topval

    

            
            

    

     











