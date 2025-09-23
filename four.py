matrix=[[1,2],[4,3]]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
#print graph elements
print("graph elements")
graph=[[0,0,0],[0,1,0],[0,0,0]]
for i in graph:
    for j in i:
        print(j,end=" ")
    print()
print("printing target element (2,1)")
for i in range(3):
    for j in range(3):
        if i==2 and j==1:
            print(graph[i][j])
