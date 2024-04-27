def path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True
    
    if start not in graph:
        return False
    
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            if path_exists(graph, neighbor, end, visited):
                return True
            
    return False

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E']
    }
 
while True:
    start = input("Enter the start node:")
    if start == 'QUIT':
        break

    end = input("Enter the end node: ")

    if path_exists(graph, start, end):
        print(f"There is path betwen {start} and {end}")
    else:
        print(f"There is no path between {start} and {end}")
