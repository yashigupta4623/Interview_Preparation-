'''
condition for cyclic -> not parent & visited == True 
'''

# cycle detection in unidirected graph using bfs
from collections import deque
def detectCycle(v,adj):
    # adj -> adj list & v ->no of vertices
    visited = [False] * v # to keep the track of visited nodes
    for start in range(v): #handle disconnected components
        if not visited[start]:
            queue = deque([(start, -1)]) #(curr_node, parent_node)
            visited[start] = True 

            while queue:
                node, parent = queue.popleft()
                for neig in adj[node]:
                    if not visited[neig]:
                        visited[neig] = True
                        queue.append((neig, node))              
                    elif neig != parent:
                        return True # if neig is visited & not the parent, it's a cycle
    return False  


# using dfs

def detectCycledfs(v,adj):
    def dfs(node, parent):
        visited[node] = True 
        for neig in adj[node]:
            if not visited[neig]:
                if dfs(neig, node): # recurs for the neig
                    return True
            elif neig != parent:
                return True #cycle
        return False

    visited = [False]*v 
    for start in range(v):
        if not visited[start]:
            if dfs(start, -1): # start dfs from this node
                return True
    return False