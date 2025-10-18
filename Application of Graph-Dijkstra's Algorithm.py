import sys
def dijkstra(graph, start_vertex):
 n = len(graph)
 visited = [False] * n
 distance = [sys.maxsize] * n
 previous = [-1] * n
 distance[start_vertex] = 0
 for _ in range(n):
 min_distance = sys.maxsize
 u = -1
 for i in range(n):
 if not visited[i] and distance[i] < min_distance:
 min_distance = distance[i]
 u = i
 if u == -1:
 break
 visited[u] = True
 for v in range(n):
 if graph[u][v] > 0 and not visited[v]:
 new_distance = distance[u] + graph[u][v]
 if new_distance < distance[v]:
 distance[v] = new_distance
 previous[v] = u
 return distance, previous
def get_path(previous, destination):
 path = []
 while destination != -1:
 path.insert(0, destination)
 destination = previous[destination]
 return path
n = int(input("Enter the number of cities: "))
city_names = []
print("Enter the name of each city:")
for _ in range(n):
 city_names.append(input())
print("\nEnter the adjacency matrix (enter 0 if no direct path):")
graph = []
for i in range(n):
 row = list(map(int, input(f"Distances from {city_names[i]}: ").split()))
 graph.append(row)
source_city = input("\nEnter the source city: ")
destination_city = input("Enter the destination city: ")
if source_city not in city_names or destination_city not in city_names:
 print("Invalid city name entered.")
 exit()
source_index = city_names.index(source_city)
destination_index = city_names.index(destination_city)
distances, previous = dijkstra(graph, source_index)
path = get_path(previous, destination_index)
if distances[destination_index] == sys.maxsize:
 print(f"No path from {source_city} to {destination_city}")
else:
 print("\nShortest distance:", distances[destination_index])
 print("Shortest path:", " -> ".join(city_names[i] for i in path))
