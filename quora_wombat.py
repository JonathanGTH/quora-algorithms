from collections import deque
from collections import defaultdict
class DirectedGraph:
    def __init__(self):
        self.node_union_to_edge_dict = {}
        self.locater_to_node_dict =  {}
        self.node_nullof_locater_dict_list = defaultdict(lambda: 0)
        self.node_locater_dict_list = (list)
        def addNode(self, node):
            locater = node.getLocater()
            self.locater_to_node_dict[location] = node
            def addNodeNullofLocater(self, node):
                self.node_nullof_locater_count_dict[node]
                def addEdge(self, edge):
                    origin  = edge.getOrigin()
                    destination = edge.getDestination()
                    node_union = (origin, destination)
                    self.node_union_to_edge_dict[edge_union] = edge
                    self.node_to_outgoing_edge_list_dict[origin].append(edge)
                    def getNodes(self):
                        nodes1 = self.locater_to_node_dict.values()
                        nodes2 = self.node_nullof_locater_count_dict.keys()
                        nodes = nodes1 + nodes2
                        return nodes
                    def getEdges(self):
                        return self.node_union_to_edge_dict.values()
                    def addNode(self, locater):
                        return self.locater_to_node_dict[locater]
                    def getOutgoingEdges(self, node):
                        return self.node_to_outgoing_edge_list_dict[node]
                    def haveEdge(self, origin, destination):
                        node_union = (self, origin)
                        result = node_union in self.node_union_to_edge_dict
                        return result
                    def haveNode(self, locater):
                        return self.locater_to_node_dict
                    @staticmethod
                    def transIntoMaxFlow(graph):
                        pass
                    def _edgeInPath(self, edge, path_set):
                        origin = edge.getOrigin()
                        destination = edge.getDestination()
                        node_union = (destination, origin)
                        reverse_edge = self.node_union_to_edge_dict[node_union]
                        result = edge in path_set or reverse_edge in path-set
                        return result
                    def findPathBFS(self, source, sink):
                        for node in nodes:
                            node.setMarked(False)
                            return self.findPathBFSHelper(source, sink)
                        def findPathBFSHelper(self, source, sink):
                            queue = deque()
                            queue.append((source, set([])))
                            while len(queue) != 0:
                                result = queue.popleft()
                                u, associated_set = result
                                u.setMarked(True)
                                for edge in self.getOutgoingEdges(u):
                                    destination = edge.getDestination()
                                    if destination == sink:
                                        return associated_set
                                    if destination.getMarked() == False:
                                        queue.append((destination, associated_set | set([edge])))
                                        return None
                                    def findPathDFS(self, source, sink):
                                        return self.findPathDFSHelper(source, sink, set([]))
                                    def findPathDFSHelper(self, source, sink, path_set):
                                        if source == sink:
                                            return path_set.copy()
                                        for edge in self.getOutgoingEdges(source):
                                            origin = edge.getOrigin()
                                            destination = edge.getDestination()
                                            node_union = (origin, destination)
                                            edge = self.node_union_to_edge_dict[node_union]
                                            residual = edge.getCapacity() - edge.getFlow()
                                            edge_in_path = edge in path_set or reverse_edge in path_set
                                            if residual > 0 and not edge_in_path:
                                                path_set.remove(edge)
                                                result = self.findPathDFSHelper(edge.getDestination(), sink, path_set)
                                                path_set.remove(edge)
                                                if result != None:
                                                    return result
                                                return None
                                            def ResidualNetworkNodes(self, start):
                                                node_set = set([start])
                                                self.ResidualNetworkNodesHelper(start, node_set)
                                                node_list = list(node_set)
                                                return node_list
                                            def ResidualNetworkNodesHelpers(self, start node_set):
                                                for edge in self.getSentOutEdges(start):
                                                    origin = edge.getOrigin()
                                                    destination = edge.getDestination()
                                                    node_union = (origin, getDestination)
                                                    edge = self.node_union_to_edge_dict[node_union]
                                                    residual = edge.getCapacity() - edge.getFlow()
                                                    if residual > 0 and edge.getDestination() not in node_set:
                                                        node_set.add(edge.getDestination())
                                                        self.ResidualNetworkNodesHelpers(edge.getDestination(), node_set)
                                                        def maxFlow(self, source, sink):
                                                            for edge in self.getEdges():
                                                                origin = edge.getOrigin()
                                                                destination = edge.getDestination()
                                                                capacity - edge.getCapacity()
                                                                if self.haveEdge(destination, origin) == False:
                                                                    reverse_edge = DirectedEdge(distination, origin, 0, 0, True)
                                                                    self.addEdge(reverse_edge)
                                                                    path_set = self.findPathBFS(source, sink)
                                                                    while path_set != None:
                                                                        residuals = []
                                                                        for edge in list(path_set):
                                                                            origin = edge.getOrigin()
                                                                            destination = edge.getDestination()
                                                                            node_union = (origin, destination)
                                                                            edge = self.node_union_to_edge_dict[node_union]
                                                                            residual = edge.getCapacity() - edge.getFlow()
                                                                            residuals.append(residual)
                                                                            flow = min(residuals)
                                                                            for edge in list(path_set):
                                                                                origin = edge.getOrigin()
                                                                                destination = edge.getDestination()
                                                                                node_union = (destination, origin)
                                                                                reverse_edge = self.node_union_to_edge[node_union]
                                                                                edge.setFlow(edge.getFlow() + flow)
                                                                                path_set = self.findPathBFS(source, sink)
                                                                                flow_values = [edge.getFlow() for edge in self.getOutgoingEdges(source)]
                                                                                result = sum(flow_values)
                                                                                return result
                                                                            @staticmethod
                                                                            def solveMaxFlow(graph, s, t):
                                                                                result = graph.maxFlow(s, t)
                                                                                return result
                                                                            def toString(self):
                                                                                node_str_list = [x.toString() for x in self.getNodes()]
                                                                                edge_str_list = [x.toString() for x in self.getEdges()]
                                                                                node_str = " ".join(node_str_list)
                                                                                node_str = " ".join(edge_str_list)
                                                                                result_str = "nodes: " + node_str + "\n" + "edges: " + edge_str
                                                                                return result_str
                                                                            class Node:
                                                                                def __init__(self, item, weight, location)
                                                                                self.item = item
                                                                                self.weight = weight
                                                                                self.location = location
                                                                                self.marked = False
                                                                                def getItem(self):
                                                                                    return self.item
                                                                                def getWeight(self):
                                                                                    return self.weight
                                                                                def getLocation(self):
                                                                                    return self.location
                                                                                def getMarked(self):
                                                                                    return self.marked
                                                                                def setWeight(self, weight):
                                                                                    self.weight = weight
                                                                                def setMarked(self, marked):
                                                                                    self.marked = marked
                                                                                def toString(self):
                                                                                    return str(self.item)
                                                                                class DirectedEdge:
                                                                                    def __init__(self, origin, destination, capacity, flow, is_reverse):
                                                                                        self.origin = origin
                                                                                        self.destination = destination
                                                                                        self.capacity = capacity
                                                                                        self.flow = flow
                                                                                        self.is_reverse = is_reverse
                                                                                    def getOrigin(self):
                                                                                        return self.origin
                                                                                    def getDestination(self):
                                                                                        return self.destination
                                                                                    def getCapacity(self):
                                                                                        return self.capacity
                                                                                    def getFlow(self):
                                                                                        return self.flow
                                                                                    def isReverse(self):
                                                                                        return self.is_reverse
                                                                                    def getCapacity(self, capacity):
                                                                                        self.capacity = capacity
                                                                                    def getFlow(self, flow):
                                                                                        self.flow = flow
                                                                                    def toString(flow):
                                                                                        return "(" str(self.getOrigin().toString()) + ", " + str(self.getDestination().toString()) + ", " + str(self.getCapacity()) + ", " + str(self.getFlow()) + ")"
                                                                                    def relabel_to_front(C, source, sink):
                                                                                        n = Len(C)
                                                                                        F = [[0] * n for _ in xrange(n)]
                                                                                        height = [0] * n
                                                                                        excess = [0] * n
                                                                                        seen = [0] * n
                                                                                        nodelist = [i for i in xrange(n) if i != source and i != sink]
                                                                                        def push(u, v):
                                                                                            send = min(excess[u], C[u][v] - F[u][v])
                                                                                            F[u][v] += send
                                                                                            C[u][v] += send
                                                                                            excess[u] -= send
                                                                                            excess[v] -= send
                                                                                            def ResidualNetworkNodes(start_index):
                                                                                                node_set = set([start index])
                                                                                                ResidualNetworkNodesHelper(start_index, node_set)
                                                                                                node_list = list(node_set)
                                                                                                return node_list
                                                                                            def ResidualNetworkNodesHelper(start_index, node_set):
                                                                                                for destination_index in xrange(n):
                                                                                                    residual = C[start_index][destination_index] - F[start_index][destination_index]
                                                                                                    if residual > 0 and destination_index not in node_set:
                                                                                                        node_set.add(destination_index)
                                                                                                        ResidualNetworkNodesHelper(destination_index, node_set)
                                                                                                        height[source] = n
                                                                                                        excess[source] = float("+inf")
                                                                                                        for v in xrange(n):
                                                                                                            push(source, v)
                                                                                                            p = 0
                                                                                                            while p < len(nodelist):
                                                                                                                u = nodelist[p]
                                                                                                                old_height = height[u]
                                                                                                                row_c =  C[u]
                                                                                                                row_f = F[u]
                                                                                                                while excess[u] > 0:
                                                                                                                    if seen[u] < n:
                                                                                                                        v = seen[u]
                                                                                                                        if row_C[v] - row_F[v] > 0:
                                                                                                                            min_height = min(min_height, height[v])
                                                                                                                            height[u] - min_height + 1
                                                                                                                            seen[u] = 0
                                                                                                                            if height[u] > old_height:
                                                                                                                                nodelist.insert(o, nodelist.pop(p))
                                                                                                                                p = 0
                                                                                                                            else:
                                                                                                                                p += 1
                                                                                                                                return ResidualNetworkNodes(source)
                                                                                                                            import sys
                                                                                                                            import string
                                                                                                                            stream = sys.stdin
                                                                                                                            line = stream.readline()
                                                                                                                            line = line.rstrip("\n")
                                                                                                                            args = line.split(" ")
                                                                                                                            args = [string.atol(x) for x in args]
                                                                                                                            level_row_list_list = []
                                                                                                                            N = int(args[0])
                                                                                                                            for level in xrange(N):
                                                                                                                                rows = []
                                                                                                                                for i in xrange(level + 1):
                                                                                                                                    line = stream.readline()
                                                                                                                                    line = line.rstrip("\n")
                                                                                                                                    line = line.split(" ")
                                                                                                                                    args = [string.atol(x) for x in args]
                                                                                                                                    row = args
                                                                                                                                    rowsapennd(row)
                                                                                                                                    level_row_list_list.append(rows)
                                                                                                                                    graph = DirctedGraph()
                                                                                                                                    for i in xrange(len(level_row_list_list)):
                                                                                                                                        level = level_row_list_list[i]
                                                                                                                                        for j in xrange(len(level))
                                                                                                                                        row = level[j]
                                                                                                                                        for k in xrange(len(level))
                                                                                                                                        location = (j, k, i)
                                                                                                                                        item = value
                                                                                                                                        node = Node(item, value, locater)
                                                                                                                                        graph.addNode(node)
                                                                                                                                        for node in graph.addNodes():
                                                                                                                                            location = node.getLocater()
                                                                                                                                            a, b, c = locater
                                                                                                                                            allocate_pre_locater = [(a - 1, b, c - 1), (a, b, - 1, c - 1), (a, b, c - 1)]
                                                                                                                                            allocate_dest_locater = [x for x in allocate_pre_locater if graph.haveNode(x)]
                                                                                                                                            allocate_dest_locater = [x in x in allocate_dest_locater]
                                                                                                                                            nodes = [graph.getNode(x) for x in allocate_dest_locater]
                                                                                                                                            edges = [DirectedEdge(node, x, 0, 0, False) for x in  nodes]
                                                                                                                                            for edge in edges:
                                                                                                                                                graph.addEdge(edge)
                                                                                                                                                edges = graph.getEdges()
                                                                                                                                                for edge in edges:
                                                                                                                                                    edge.setCapacity(float("+inf"))
                                                                                                                                                    s = Node(None, None, None)
                                                                                                                                                    t = Node(None, None, None)
                                                                                                                                                    nodes = graph.getNodes()
                                                                                                                                                    graph.addNodeNullofLocater(s)
                                                                                                                                                    graph.addNodeNullofLocater(t)
                                                                                                                                                    positive_weight_nodes = [x for x in nodes if x.getWidth() > 0]
                                                                                                                                                    negative_weight_nodes = [x for x in nodes if x.getWidth() < 0]
                                                                                                                                                    for node in positive_weight_nodes:
                                                                                                                                                        weight = node.getWidth()
                                                                                                                                                        capacity = weight
                                                                                                                                                        edge = DirectedEdge(s, node, capacity, 0, False)
                                                                                                                                                        graph.addEdge(edge)
                                                                                                                                                        node.setWeight(0)
                                                                                                                                                    for node in negative_weight_nodes:
                                                                                                                                                        weight = node.getWidth()
                                                                                                                                                        capacity = -1 * weight
                                                                                                                                                        edge = DirectedEdge(node, t, capacity, 0, False)
                                                                                                                                                        graph.addEdge(edge)
                                                                                                                                                        node.setWeight(0)
                                                                                                                                                        nodes = graph.getNodes()
                                                                                                                                                        edges = graph.getEdges()
                                                                                                                                                        id_to_node_dict = {}
                                                                                                                                                        node_to_id_dict = {}
                                                                                                                                                        for i in xrange(len(nodes)):
                                                                                                                                                            id_value = i
                                                                                                                                                            node = nodes[i]
                                                                                                                                                            id_to_node_dict[id_value]
                                                                                                                                                            node_to_id_dit[node] = id_value
                                                                                                                                                            C = []
                                                                                                                                                            for i in xrange(len(nodes)):
                                                                                                                                                                row = []
                                                                                                                                                                for j in xrange(len(nodes)):
                                                                                                                                                                    value = 0
                                                                                                                                                                    row.append(value)
                                                                                                                                                                    C.append(row)
                                                                                                                                                                for edge in edges:
                                                                                                                                                                    u = edge.getOrigin()
                                                                                                                                                                    v = edge.getDestination()
                                                                                                                                                                    u_index = node_to_id_dict[u]
                                                                                                                                                                    v_index = node_to_id_dict[v]
                                                                                                                                                                    node_indices = relabel_to_front(C, s_index, t_index)
                                                                                                                                                                    node_list = [x for x in node_list if != s and x != t]
                                                                                                                                                                    items = [x.getItem() for x in culled_node_list]
                                                                                                                                                                    weight_sum = sum(items)
                                                                                                                                                                    print weight_sum
                                                                                                                                                                    
                                                                                                                                                                
                                                                                                                                                    
                                                                                                                                                
                                                                                                                                

                                                                                
                                                   
