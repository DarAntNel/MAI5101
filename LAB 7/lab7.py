from collections import defaultdict, deque

def bfs(s, t, adj, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)

    while queue:
        u = queue.popleft()
        for v, capacity in adj[u].items():
            if v not in visited and capacity > 0:
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True
                queue.append(v)

    return False

def edmond_karp(s, t, adj):
    flow = 0
    parent = {}
    while bfs(s, t, adj, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, adj[u][v])
            v = u

        flow += path_flow
        v = t
        while v != s:
            u = parent[v]
            adj[u][v] -= path_flow
            adj[v][u] += path_flow
            v = u

    return flow


def main(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if not line.startswith("#")]
    idx = 0
    n_s, n_c = map(int, lines[idx].split())
    idx += 1

    students = set()
    companies = set()
    student_prefs = defaultdict(set)

    while idx < len(lines) and lines[idx]:
        s, c = lines[idx].split()
        students.add(s)
        companies.add(c)
        student_prefs[s].add(c)
        idx += 1

    idx += 1

    company_prefs = defaultdict(set)

    while idx < len(lines):
        c, s = lines[idx].split()
        companies.add(c)
        students.add(s)
        company_prefs[c].add(s)
        idx += 1

    src = 'Source'
    sink = 'Sink'

    adj = defaultdict(lambda: defaultdict(int))

    for s in students:
        adj[src][s] = 1

    for c in companies:
        adj[c][sink] = 1

    for s in student_prefs:
        for c in student_prefs[s]:
            if s in company_prefs[c]:
                adj[s][c] = 1

    max_flow = edmond_karp(src, sink, adj)

    matching = []
    for s in students:
        for c in companies:
            if adj[c][s] > 0:
                matching.append((s, c))

    with open('output.txt', 'w') as f:
        f.write(f"Maximum matching: {max_flow}\n\n")
        f.write("Matched Pairs:\n")
        for s, c in matching:
            f.write(f"{s} - {c}\n")


if __name__ == "__main__":
    main("input.txt")
