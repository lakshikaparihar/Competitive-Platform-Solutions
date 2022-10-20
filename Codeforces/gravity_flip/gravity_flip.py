n = int(input())
list_of_cubes = list(map(int,input().split(" ")))
max_blocks = max(list_of_cubes)
no_of_places =len(list_of_cubes)
for j in range(no_of_places):
    for i in range(no_of_places-1,j,-1):
        if list_of_cubes[i]< max_blocks:
            diff = list_of_cubes[i-1] - list_of_cubes[i]
            if diff>0:
                list_of_cubes[i]+=abs(diff)
                list_of_cubes[i-1]-=abs(diff)
    print(list_of_cubes[j],end=" ")
