matrix_a=[[3,5],[9,8]]
matrix_b=[[1,3],[8,9]]
print(f'Input: \n {matrix_a} \n {matrix_b}')

#using zip
y=[i for i in zip(matrix_a,matrix_b)]
# print(y)
z=[]
x=[]
for i in y:
    row1=[]
    row2=[]
    for a,b in zip(*i):
        row1.append(a-b)
        row2.append(a+b)
    x.append(row1)
    z.append(row2)
print(f'Output: \naddition of two matrices results: {z}')
print(f'subtraction of two matrices results: {x}')

#without zip
result=[]
for i in range(len(matrix_a)):
    row = []
    for j in range(len(matrix_a[i])):
        sum=matrix_a[i][j]-matrix_b[i][j]
        row.append(sum)
    result.append(row)
print(f'Output: \nsubtraction of two matrices gives: {result}')
