# Diagonal Matrix

def diagonal_left(mat):
    dia=[]
    for i in range(len(mat)):
        dia.append(mat[i][i])
    return dia

def diagonal_right(mat):
    dia=[]
    j=len(mat)-1
    for i in range(len(mat)):
        dia.append(mat[i][j])
        j-=1
    return dia


# Upper-Lower Triangle

def upperTri(mat):
    tri=[]
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat[0])):
            if i<=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri

def lowerTri(mat):
    tri=[]
    for i in range(len(mat)):
        row=[]
        for j in range(len(mat[0])):
            if i>=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri


# Transpose Matrix
def transpose(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>j:
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
