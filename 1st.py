from collections import deque
def water_jug_bfs():
    max_a, max_b = 4, 3  
    visited = set()
    queue = deque()
    
    queue.append((0, 0))  
    while queue:
        a, b = queue.popleft()
        
        if a == 2:
            print("Goal Reached: (A =", a, ", B =", b, ")")
            return
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print("Visited: A =", a, ", B =", b)

        #All possible states
        possible_states = [
            (max_a, b),        
            (a, max_b),        
            (0, b),            
            (a, 0),           
            (a - min(a, max_b - b), b + min(a, max_b - b)), 
            (a + min(b, max_a - a), b - min(b, max_a - a)), 
        ]
        for state in possible_states:
            if state not in visited:
                queue.append(state)
            print("Q",queue)
    print("No solution found.")

water_jug_bfs()
