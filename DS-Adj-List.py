# Implementing Adjacency List data structure for Graph, Breadth First Search, and Depth First Search
# per Steven Skiena's book

from Queue import Queue

class edgeNode:
    def __init__(self, adjInfo=0, weight=0, nextEdge=None):
        self.adjInfo = adjInfo
        self.weight = weight
        self.nextEdge = nextEdge

class Graph:
    
    def __init__(self, numVert, numEdge, directed = False):
        self.numVert = numVert
        self.numEdge = numEdge
        self.directed = directed
        self.outDegree = []
        self.edges = []
        
        # Setting max vertices to 1000 per the book
        for i in range(1000):
            self.outDegree.append(0)
            self.edges.append(edgeNode())
    
    def readGraph(self, directed):
        self.directed = directed
        
        edge = [(1,2), (1,5), (2,5), (2,4), (2,3), (3,4), (4,5)]
        
        for x, y in edge:
            self.insertEdge(x, y, directed)
        
    def insertEdge(self, x, y, directed):
        # Temporary pointer
        temp = edgeNode(y, None, self.edges[x])
        # Insert at the head of the list
        self.edges[x] = temp
        self.outDegree[x] += 1
        
        if directed == False:
            self.insertEdge(y, x, True)
        else:
            self.numEdge += 1
    
    def printGraph(self):
        i = 0
        while i <= self.numVert:
            line = ""
            line += str(i) + ": "
            temp = self.edges[i]
            while temp.nextEdge != None:
                line += str(temp.adjInfo) + ", "
                temp = temp.nextEdge
            print(line)
            i += 1

class BFS:
    def __init__(self, graph=Graph(0,0)):
        self.processed = []
        self.discovered = []
        self.parent = []
        self.graph = graph
        
        i = 0
        while i <= self.graph.numVert:
            self.processed.append(False)
            self.discovered.append(False)
            self.parent.append(-1)
            i+=1
    
    def doBFS(self, startVert):
        q = Queue()
        temp = edgeNode()
        
        q.enqueue(startVert)
        self.discovered[startVert] = True
        
        while q.isEmpty() == False:
            vertex = q.dequeue()
            self.processVertexEarly(vertex)
            self.processed[vertex] = True
            temp = self.graph.edges[vertex]
            while temp != None:
                adjVert = temp.adjInfo
                if (self.processed[adjVert] == False) or self.graph.directed:
                    self.processEdge(vertex, adjVert)
                if self.discovered[adjVert] == False:
                    q.enqueue(adjVert)
                    self.discovered[adjVert] = True
                    self.parent[adjVert] = vertex
                
                temp = temp.nextEdge
            self.processVertexLate(vertex)
    
    def processVertexLate(self, vertex):
        pass
    
    def processVertexEarly(self, vertex):
        print("Processed vertex: ", vertex)
    
    def processEdge(self, edgeV1, edgeV2):
        print("Processed edge: (",edgeV1,", ",edgeV2,")")
        # This next line would keep an accurate count of the number of edges
        # numEdges += 1
    
    def findPath(self, start, end):
        if (start == end) or (end == -1):
            print("")
            print(start, end = "")
        else:
            self.findPath(start, self.parent[end])
            print(end, end="")

class DFS:
    def __init__(self, graph = Graph(0,0)):
        self.processed = []
        self.discovered = []
        self.parent = []
        self.graph = graph
        self.entryTime = []
        self.exitTime = []
        
        i = 0
        while i <= self.graph.numVert:
            self.processed.append(False)
            self.discovered.append(False)
            self.entryTime.append(0)
            self.exitTime.append(0)
            self.parent.append(-1)
            i+=1
    
    def doDFS(self, startVert):
        temp = edgeNode()
        
        if finished: return
        
        self.discovered[startVert] = True
        time = time+1
        self.entryTime[startVert] = time
        
        self.processVertexEarly(startVert)
        
        temp = self.graph.edges[startVert]
        while temp != None:
            adjVert = temp.adjInfo
            
            if self.discovered[adjVert] == False:
                self.parent[adjVert] = startVert
                self.processEdge(startVert, adjVert)
                self.doDFS(adjVert)
            elif (not self.processed[adjVert]) or self.graph.directed:
                self.processEdge(startVert, adjVert)
            if finished: return
            temp = temp.nextEdge
        self.processVertexLate(startVert)
        
        time += 1
        self.exitTime[startVert] = time
            

    def processVertexLate(self, vertex):
        pass
    
    def processVertexEarly(self, vertex):
        print("Processed vertex: ", vertex)
    
    def processEdge(self, edgeV1, edgeV2):
        print("Processed edge: (",edgeV1,", ",edgeV2,")")
        # This next line would keep an accurate count of the number of edges
        # numEdges += 1

def main():
    g = Graph(5, 7)
    g.readGraph(False)
    
    g.printGraph()
    
    bfs = BFS(g)
    bfs.doBFS(1)
    
if __name__ == "__main__":
    main()
