class Vertex:
    def __init__(self, element):
        self._element = element
    
    def __str__(self):
    """ Return a string representation of the vertex. """
        return str(self._element)

    def element():
        return self._element 

    def __lt__(v):
        return self._element < v.element()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Edge:
    def __init__(self, v, w, element):
        self._vertices(v,w)
        self._element = element

    #return string rep of the edge
    def __str__(self):
        return ('(' + str(self._vertices[0]) + '--'+ str(self._vertices[1]) + ' : '+ str(self._element) + ')')

    def vertices(self):
        return self._vertices

    def element(self):
        return self._element

    def start():
        return self._vertices[0]

    def end():
        return self._vertices[1]

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class Graph:
    def __init__(self):
        self._structure = dict()
    
    def __str__(self):
    """ Return a string representation of the graph. """
    hstr = ('|V| = ' + str(self.num_vertices()) + '; |E| = ' + str(self.num_edges()))
    vstr = '\nVertices: '

    for v in self._structure:
        vstr += str(v) + ' '
        edges = self.edges()
        estr = '\nEdges: '
    for e in edges:
        estr += str(e) + ' '
    return hstr + vstr + estr



    def num_vertices(self):
        return len(self._structure)



    def num_edges(self):
        num = 0 
        for v in self._structure:
            num += len(self.stucture[v])
        return num // 2     # to root out repeated num of edges



    def vertcies(self):
        return [key for key in self._structure]



    def get_vertex_by_label(self, element):
        for v in self._structure:
            if v.element() == element:
                return v
        return None 


    def edges(self):
        #return a list of all edges in the graph 
        edgeList = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid dupes, only return if v is the first vertex
                if self._structure.start[v][w] == v:
                    edgeList.append(self._structure[v][w])
                return edgeList
    def get_edges(self,v):
        if v in self._structure:
            edgeList = []
            for w in self._structure[v]:
                edgeList.append(self._structure[v][w])
            return edgeList
        return None

    def get_edge(self, v, w):
        #return the edge between two vertices
        if (self._structure != None and v in self._structure and w in self._structure[v]):
            return self._structure[v][w]
        return None 

    def degree(self, v):
        return len(self._structure[v])


    #Functionality for adding a new vertex 
    def add_vertex(self, element):
        v = Vertex(element)
        self._structure[v] = dict()
        return v 

    def add_vertex_if_new(self, element):
        #check for equality between elements, if they are the same dont allow its inclusion 
        for v in self._structure:
            if v.element() == element:
                #already in graph!
                return v 
            return self.add_vertex(element)

    def add_edge(self, v, w, element):
        if not v in self._structure or if not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e 

    def add_edge_pairs(self, elist):
        for (v,w) in elist:
            self.addEdge(v,w,None)

    def test_graph():
""" Test on a simple 3-vertex, 2-edge graph. """
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex_if_new('b') #should not create a vertex
    eab = graph.add_edge(a, b, 2)
    ebc = graph.add_edge(b,c,9)
    vnone = Vertex('dummy')
    evnone = graph.add_edge(vnone, c, 0) #should not create an edge
    if evnone is not None:
        print('ERROR: attempted edges should have been none')
        edges = graph.get_edges(vnone) #should be None: vnone not in graph
    if edges != None:
        print('ERROR: returned edges for non-existent vertex.')
        print('number of vertices:', graph.num_vertices())
        print('number of edges:', graph.num_edges())
        print('Vertex list should be a,b,c in any order :')
        vertices = graph.vertices()
    for key in vertices:
        print(key.element())
        print('Edge list should be (a,b,2),(b,c,9) in any order :')
        edges = graph.edges()
    for edge in edges:
        print(edge)
        print('Graph display should repeat the above:')
        print(graph)
        v = graph.add_vertex('d')
        edges = graph.get_edges(v)
    if edges != []:
        print('ERROR: should have returned an empty list, but got', edges)
        print('Graph should now have a new vertex d with no edges')
        print(graph)

    
    def test_graph2():
       " "" Test Graph with the standard 6-vertex graph from lectures. """
        graph = Graph()
        a = graph.add_vertex('a')
        b = graph.add_vertex('b')
        c = graph.add_vertex('c')
        d = graph.add_vertex('d')
        e = graph.add_vertex('e')
        f = graph.add_vertex('f')
        graph.add_edge(a,b,1)
        graph.add_edge(a,c,1)
        graph.add_edge(b,c,1)
        graph.add_edge(b,d,1)
        graph.add_edge(b,e,1)
        graph.add_edge(c,f,1)
        graph.add_edge(e,f,1)
        print('Graph:')
        print(graph)
        print()
        hdv = graph.highestdegreevertex()
        print(hdv.element(),
        'has the highest degree =',
        graph.degree(hdv))
        print()


    def test_graph3():
    """ Test on the larger graph from lectures. """
        graph = Graph()
        a = graph.add_vertex('a')
        b = graph.add_vertex('b')
        c = graph.add_vertex('c')
        d = graph.add_vertex('d')
        e = graph.add_vertex('e')
        f = graph.add_vertex('f')
        g = graph.add_vertex('g')
        h = graph.add_vertex('h')
        i = graph.add_vertex('i')
        j = graph.add_vertex('j')
        k = graph.add_vertex('k')
        l = graph.add_vertex('l')
        m = graph.add_vertex('m')
        graph.add_edge(a,b,1)
        graph.add_edge(a,e,1)
        graph.add_edge(a,h,1)
        graph.add_edge(b,c,1)
        graph.add_edge(b,e,1)
        graph.add_edge(c,d,1)
        graph.add_edge(c,g,1)
        graph.add_edge(d,f,1)
        graph.add_edge(e,f,1)
        graph.add_edge(e,k,1)
        graph.add_edge(f,i,1)
        graph.add_edge(g,j,1)
        graph.add_edge(h,m,1)
        graph.add_edge(i,j,1)
        graph.add_edge(i,k,1)
        graph.add_edge(j,l,1)
        graph.add_edge(k,l,1)
        graph.add_edge(k,m,1)
        hdv = graph.highestdegreevertex()
        print(hdv.element(),
        'has the highest degree =',
        graph.degree(hdv))
        print(graph)

    def read_dolphin_graph():
    """ Read the dolphins file, return the graph and separate names dict. """
graph = Graph()
file = open('dolphins.gml', 'r')
names = dict()
file.readline() #the header with author details
file.readline() #the start of the graph
file.readline() #the opening square bracket
file.readline() #the comment that the graph is not directed
wordlist = file.readline().split()
while wordlist[0] != ']':
if wordlist[0] == 'node':
file.readline() #open bracket
nodeid = int(file.readline().split()[1])
vertex = graph.add_vertex(nodeid)
names[nodeid] = file.readline().split()[1]
#print('added vertex', vertex, 'with label', names[nodeid])
file.readline() #close bracket
elif wordlist[0] == 'edge':
file.readline() #open bracket
source = int(file.readline().split()[1])
target = int(file.readline().split()[1])
sv = graph.get_vertex_by_label(source)
tv = graph.get_vertex_by_label(target)
edge = graph.add_edge(sv, tv, 1)
#print('added edge, source =', source, '; target =', target, ':', edge)
file.readline()
else:
print('ERROR: unrecognised line:', wordlist[0])
wordlist = file.readline().split()
return graph,names
