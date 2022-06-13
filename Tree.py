

## Tree Representation

from logging import root
from tkinter.tix import Tree

## Creation of Binary Tree



class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

        """
            1
           / \
         2    3
        / \   / \
       4   5  6  7       
         """
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
    # When I am working on the tree, generally the root will be only given

## Creation of Binary Search Tree

class Node:
    def __init__(self,data):
        self.left=self.right=None
        self.data=data

def insertNode(root,x):
    if root is None:
        root=Node(x)
        return root
    elif(x>root.data):
        root.right=insertNode(root.right,x)
    else:
        root.left=insertNode(root.left,x)
    
    return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
    
    
if __name__ == '__main__':
    root=None
    nodes=[6,8,7,9,4,3,5]
    for i in nodes:
        root=insertNode(root,i)
    inorder(root)
    

        








## Recursive Traversals

def preorder(root):
    if root is None:
        return 
    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)


## Method-1
def levelorder(root):
    qu=[root]
    ans=[]
    while(qu):
        levelnodes=[]
        n=len(que)
        for i in range(n):
            curr=que[0]
            que.pop(0)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            levelnodes.append(curr.data)
        ans.append(levelnodes)
    return ans
## Method-2
def levelorder(root):
            qu=[root]
            ans=[]
            while(qu):
                curr=qu[0]
                qu.pop(0)
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
                ans.append(curr.data)
            return ans



# Iterative Traversals

def inorder(root):
    s=[]
    res=[]
    curr=root
    while True:
        if curr:
            s.append(curr)
            curr=curr.left
        else:
            if(len(s)==0):
                break
            curr=s[-1]
            s.pop()
            res.append(curr.data)
            curr=curr.right
    return res

def iterativePreorder(root):
    stack=[root]
    while stack:
        currNode= stack[-1]
        print(stack.pop())
        if currNode.right:
            stack.append(currNode.right)
        if currNode.left:
            stack.append(currNode.left)
    

def iterativePostorder(root):
    stack=[root]
    path=[]
    while stack:
        currNode = stack[-1]
        stack.pop()
        path.append(currNode.data)
        if currNode.left:
            stack.append(currNode.left)
        if currNode.right:
            stack.append(currNode.right)
    path=path[::-1]
    """
    s=0
    e=len(path)-1
    while s<=e:
        path[s],path[e]=path[e],path[s]
        s+=1
        e-=1
    """
    return path




## Maximum Depth Of BT

def maxDepthOfBinaryTree(root):
    if root is None:
        return 0
    lh=maxDepthOfBinaryTree(root.left)
    rh=maxDepthOfBinaryTree(root.right)
    return 1+max(lh,rh)


## Count No of Nodes

def Count_Nodes(root):
    if not root:
        return 0
    lc=Count_Nodes(root.left)
    rc=Count_Nodes(root.right)
    return 1+lc+rc

    
## Sum of Nodes

def Sum_Nodes(root):
    if not root:
        return 0
    ls=Sum_Nodes(root.left)
    rs=Sum_Nodes(root.right)
    return root.data+ls+rs


## Count Leaf Nodes

def Count_LeafNodes(root):
    if not root:
        return 0
    if(root.left is None and root.right is None):
        return 1
    return Count_LeafNodes(root.left)+Count_LeafNodes(root.right)


## Mirror Tree

def mirrorTree(root):
    if not root:
        return
    root.left,root.right = root.right,root.left
    mirrorTree(root.left)
    mirrorTree(root.right)
    

## Remove Leaf Nodes

def removeLeaf(root):
    if not root:
        return None
    if(root.left is None and root.right is None):
        return None
    
    root.left=removeLeaf(root.left)
    root.right=removeLeaf(root.right)
    return root


## Check for Balanced Binary Tree

# Method-1
def balancedBinaryTree(root):
    if not root:
        return True
    if(abs(maxDepthOfBinaryTree(root.left)-maxDepthOfBinaryTree(root.right))>1):
        return False
    left=balancedBinaryTree(root.left)
    right=balancedBinaryTree(root.right)
    return left and right

# Method-2
def balancedBinaryTree(root):
    res=solve(root)
    if(res==-1):
        return False
    return True

def solve(root):
    if not root:
        return 0
    lh=solve(root.left)
    if(lh==-1):
        return -1
    rh=solve(root.right)
    if(rh==-1):
        return -1
    if(abs(lh-rh)>1):
        return -1
    return 1+max(lh,rh)



## Diameter Of Tree

def diameter(root):
    if(not root):
        return 0
    leftheight=maxDepthOfBinaryTree(root.left)
    rightheight=maxDepthOfBinaryTree(root.right)
    d=1+leftheight+rightheight
    leftdia=diameter(root.left)
    rightdia=diameter(root.right)
    return max(max(leftdia,rightdia),d)


## Maximum Path Sum

def maxPathSum(root):
    maxsum=[0]
    solve(root,maxsum)
    return maxsum[0]




def solve(root,maxsum):
    if not root:
        return 0
    leftsum=solve(root.left,maxsum)
    rightsum=solve(root.right,maxsum)
    ##VVIMP
    if(leftsum<0): leftsum=0
    if(rightsum<0): rightsum=0
    maxsum[0]=max(maxsum[0],root.data+leftsum+rightsum)
    return root.data+max(leftsum,rightsum)


## Trees are Identical or not

    
def identicalTrees(root1,root2):
    path1=[]
    path2=[]
    path1=preorder(root1,path1)
    path2=preorder(root2,path2)
    for v1,v2 in zip(path1,path2):
        if v1 != v2:
            return False
    return True


def preorder(root,path):
    if not root:
        return 
    path.append(root.data)
    preorder(root.left)
    preorder(root.right)


## Zig-Zag Traversal

def zig_zag(root):
    que=[root]
    ans=[]
    while que:
        n=len(que)
        levelnodes=[]
        for i in range(n):
            curr = que[0]
            que.pop(0)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            levelnodes.append(curr.data)
        ans.append(levelnodes)
    
    for i in range(1,len(ans),2):
        ans[i]=ans[i][::-1]
    return ans



def verticaltraversal(root):
    que=[(root,0)]
    d={}
    while que:
        curr,pos=que[0]
        que.pop(0)
        if pos not in d:
            d[pos]=[curr.data]
        else:
            d[pos].append(curr.data)
        
        if curr.left:
            que.append((curr.left,pos-1))
        if curr.right:
            que.append((curr.right,pos+1))
    
    for k in sorted(d.keys()):
        print(d[k])



def topView(root):
    que=[(root,0)]
    d={}
    while que:
        curr,pos=que[0]
        que.pop(0)
        if pos not in d:
            d[pos]=curr.data
        
        
        if curr.left:
            que.append((curr.left,pos-1))
        if curr.right:
            que.append((curr.right,pos+1))
    
    for k in sorted(d.keys()):
        print(d[k])


def bottomView(root):
    que=[(root,0)]
    d={}
    while que:
        curr,pos=que[0]
        que.pop(0)
        
        d[pos]=curr.data
        
        
        if curr.left:
            que.append((curr.left,pos-1))
        if curr.right:
            que.append((curr.right,pos+1))
    
    for k in sorted(d.keys()):
        print(d[k])
    


def leftView(root):
    qu=[root]
    ans=[]
    while(qu):
        levelnodes=[]
        n=len(que)
        for i in range(n):
            curr=que[0]
            que.pop(0)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            levelnodes.append(curr)
        ans.append(levelnodes[0])
    return ans


def rightView(root):
    qu=[root]
    ans=[]
    while(qu):
        levelnodes=[]
        n=len(que)
        for i in range(n):
            curr=que[0]
            que.pop(0)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
            levelnodes.append(curr)
        ans.append(levelnodes[-1])
    return ans








