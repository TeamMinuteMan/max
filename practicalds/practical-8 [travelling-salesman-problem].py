#Travelling Salesman Problem.

from sys import maxsize
from itertools import permutations

V=4

def travellingSalesmanProblem(graph,s):
    vertex=[]
    for i in range(V):
        if i!=s:
            vertex.append(i)
        print(vertex)
        min_path = maxsize
        print(min_path)
        next_permutation=permutations(vertex)
        print(next_permutation)
        for i in next_permutation:
            print(i)
            current_pathweight = 0
            k = s
            for j in i:
                current_pathweight += graph[k][j]
                k = j
            current_pathweight += graph[k][s]
            print(current_pathweight)
            min_path = min(min_path, current_pathweight)
        return min_path
graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print("Minimum cost is: ",travellingSalesmanProblem(graph, s))

#travellingSalesmanProblem([[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]],0)



