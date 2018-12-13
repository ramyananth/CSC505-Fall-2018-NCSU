class Vertex:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adjacency_list = {}
        self.parent = None
        self.minimum_distance = float("inf")
    def __lt__(self, other):
        return self.minimum_distance < other.minimum_distance
    def __str__(self):
        return str(self.vertex) + " : " + str(self.minimum_distance)

def GenerateGraph(edge_count):
    graph = []
    nameVertex = {}
    for i in range(0, edge_count):
        source, destination, weight = map(int, input().split())
        source_object = nameVertex.get(source)
        if source_object is None:
            source_object = Vertex(source)
            graph.append(source_object)
        destination_object = nameVertex.get(destination)
        if destination_object is None:
            destination_object = Vertex(destination)
            graph.append(destination_object)
        source_object.adjacency_list[destination] = weight
        destination_object.adjacency_list[source] = weight
        nameVertex[source] = source_object
        nameVertex[destination] = destination_object
    return graph, nameVertex

def singleSource(source):
    source.minimum_distance = 0

def djikstras(graph, nameVertex, source, destination):
    queue = graph
    import heapq
    heapq.heapify(queue)
    solution = []
    while len(queue) != 0:
        u = queue.pop(0)
        solution.append(u)
        for vertex, weight in u.adjacency_list.items():
            v = nameVertex.get(vertex)
            relax(u, v, weight, graph, nameVertex)
    return solution

def print_graph(graph):
    for vertex in graph:
        print(vertex.vertex)
        print(vertex.minimum_distance)
        print(vertex.adjacency_list)
        print(vertex.parent)

def relax(u, v, weight, graph, nameVertex):
    import heapq
    if v.minimum_distance > u.minimum_distance + weight:
        v.minimum_distance = u.minimum_distance + weight
        v.parent = u
    elif v.minimum_distance == u.minimum_distance + weight:  
        u_length = get_edge_count(u)
        v_length = get_edge_count(v)
        if u_length + 1 < v_length:  
            v.minimum_distance = u.minimum_distance + weight
            v.parent = u
        else:  
            flag = compare_paths(u, v)  
            if flag == 0:
                v.minimum_distance = u.minimum_distance + weight
                v.parent = u
    heapq.heapify(graph)

def get_edge_count(vertex):
    count = 0
    obj = vertex
    while obj is not None:
        count += 1
        obj = obj.parent
    return count

def compare_paths(u, v):
    u1 = u
    v1 = v.parent
    u_list = []
    v_list = []
    while u1 is not None and v1 is not None:
        u_list.append(u1.vertex)
        u1 = u1.parent
        v_list.append(v1.vertex)
        v1 = v1.parent
    u_list.reverse()
    v_list.reverse()
    for i in range(0, len(u_list)):
        if u_list[i] == v_list[i]:
            continue
        elif u_list[i] < v_list[i]:
            return 0
        else:
            return 1

def get_solution(solution, source, destination, nameVertex):
    destination_object = nameVertex.get(destination)
    minimum_distance = destination_object.minimum_distance
    FinalPath = [destination_object.vertex]
    obj = destination_object.parent
    while obj is not None:
        FinalPath.append(obj.vertex)
        obj = obj.parent
    FinalPath.reverse()
    return FinalPath, minimum_distance

def main():
    vertices_count, edge_count = map(int, input().split())
    graph, nameVertex = GenerateGraph(edge_count)
    source, destination = map(int, input().split())
    source = nameVertex.get(source)
    singleSource(source)
    solution = djikstras(graph, nameVertex, source, destination)
    FinalPath, minimum_distance = get_solution(solution, source, destination,
                                                   nameVertex)
    print(minimum_distance)
    s = " ".join(map(str, FinalPath))
    print(s)

if __name__ == '__main__':
    main()