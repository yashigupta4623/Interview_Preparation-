# cycle detection in unidirected graph 

'''
condition for cyclic -> not parent & visited == True 
'''

# using bfs
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

# cycle detection in directed graph 
'''
conditions for cycle detection:
visited is True and dfsvisitedcall is True
'''

# using dfs

def detectCycledfs(v,adj):
    def dfs(node, parent):
        if dfsvisitedcall[node]: # If the node is already in the recursion stack, we have a cycle
            return True 
        if visited[node]:  # If the node is already visited, skip it
            return False 
        
        visited[node] = True
        dfsvisitedcall[node] = True

        # Visit all neighbors of the current node
        for neig in adj[node]:
            if dfs(neig):
                return True
        dfsvisitedcall[node] = False # Backtrack, remove node from recursion stack
        return False

    visited = [False]*v 
    dfsvisitedcall = [False]*v
    for start in range(v):
        if not visited[start]:
            if dfs(start): # start dfs from this node
                return True
    return False

#bfs