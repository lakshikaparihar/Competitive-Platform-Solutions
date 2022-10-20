n = int(input())
list_of_cubes = sorted(list(map(int,input().split(" "))))
for i in range(len(list_of_cubes)):
    print(list_of_cubes[i],end=" ")