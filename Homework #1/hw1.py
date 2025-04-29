import heapq

def dijkstra(graph, start):
    dist = {u: float('inf') for u in graph}
    prev = {u: None for u in graph}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev

def build_path(prev, start, end):
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path if path and path[0] == start else None

def main():
    with open("graph2.txt", 'r') as f:
        num_vertices, num_edges = map(int, f.readline().split())
        start = f.readline().strip()

        graph = {}
        edges = []
        for _ in range(num_edges):
            vertice_1, vertice_2, weight = f.readline().split()
            weight = int(weight)
            graph.setdefault(vertice_1, [])
            graph.setdefault(vertice_2, [])
            edges.append((vertice_1, vertice_2, weight))

        for vertice_1, vertice_2, weight in edges:
            graph[vertice_1].append((vertice_2, weight))

    dist, prev = dijkstra(graph, start)


    for node in sorted(graph): #printing nodes
        d = dist[node]
        d_str = 'infinite' if d == float('inf') else str(d)
        print(f"Distance from {start} to {node} = {d_str}")


    print("\nPaths:\n") #printing paths sotred so infinite printed last

    node_dist_pairs = []
    for u in graph:
        if dist[u] < float('inf'):
            node_dist = dist[u]
        else:
            node_dist = float('inf')
        node_dist_pairs.append((node_dist, u))

    node_dist_pairs.sort()

    nodes_by_dist = [u for _, u in node_dist_pairs]


    for node in nodes_by_dist:
        path = build_path(prev, start, node)
        if path is None:
            print(f"No path to {node}")
        else:
            print("->".join(path))

if __name__ == '__main__':
    main()
