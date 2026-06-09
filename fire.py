def fire(grid,i,j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
        return
    grid[i][j]=2
    fire(grid,i+1,j)
    fire(grid,i-1,j)
    fire(grid,i,j+1)
    fire(grid,i,j-1)
matrix=[[1,1,1,1],
        [1,0,0,0],
        [0,0,1,1],
        [1,0,0,0]]
fire(matrix,0,0)
c=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==1:
            c+=1
print(c)