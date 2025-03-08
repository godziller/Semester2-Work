#class VERTEX
from Stack import *
class Vertex:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        return str(self._element)

    def element(self):
        return self._element

    def __lt__(self, v):
        return self._element < v.element()


#class EDGE
class Edge: 
    def __init__(self, v, w, element):
        #v = vertex object
        #w = another vertex object
        #element = a LABEL -> name of edge
        self._vertices = (v,w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    def vertices(self):
        return self._vertices

    def opposite(self, v):
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        return self._element

    def start(self):
        return self._vertices[0]

    def end(self):
        return self._vertices[1]


#class Graph
class Graph:
    def __init__(self):
        self._structure = dict()

    def str(self):
        """ Return a string representation of the graph. """
        hstr = ('|V| = ' + str(self.num_vertices())
            + '; |E| = ' + str(self.num_edges()))
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
            num += len(self._structure[v])
        return num // 2 

    def vertices(self):
        return [key for key in self._structure]

    def get_vertex_by_label(self,element):
        #get the first vertex that matches the element
        for v in self._structure:
            if v.element() == element:
                return v 
        return None 

    def edges(self):
        for v in self._structure:
            edgelist = []
            for w in self._structure:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None
    
    def get_edges(self,v):
        #return a list of all vertices incident on v

        if v in self._structure:
            return list(self._structure[v].values())
        return None


    def get_edge(self,v,w):
        if (self._structure != None and v in self._structure and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self,v):
        return len(self._structure[v])

    #functions for modding the graph

    def add_vertex(self,element):
        v = Vertex(element)
        self._structure[v] = dict()
        return v

    def add_vertex_if_new(self, element):
        for v in self._structure:
            if v.element() == element:
                return v    #already in graph
            return self.add_vertex(element)

    def add_edge(self,v,w,element):
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v,w,element)
        self._structure[v][w] = e 
        self._structure[w][v] = e
        return e 

    def add_edge_pair(self,elist):
        for (v,w) in elist:
            self.add_edge(v,w,None)

    def highestdegreevertex(self):
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v 
        return hdv 

#.............................................................................#
#graph traversal
    def dfs_Stack(self,v):
        marked = {}
        stack = Stack()
        stack.push((v, None))
        while stack.len() > 0:
            (vertex, edge) = stack.pop()
            if vertex not in marked:
                marked[vertex] = edge
                for e in self.get_edges(vertex):
                    w = e.opposite(vertex)
                    if w not in marked:
                        stack.push((w,e))
        return marked

    def depthfirstsearch(self,v):
        #return a DFS tree from V.
        marked = {v:None}
        self._depthfirstsearch(v,marked)
        return marked

    def _depthfirstsearch(self,v, marked):
        #Do a recursive DFS from v, storing nodes in marked
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)


#testing graph
def test_graph():
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
    print(hdv.element(), 'has the highest degree =', graph.degree(hdv))
    print(graph)

    hdv = graph.highestdegreevertex()
    print(hdv.element(),'has the highest degree =',graph.degree(hdv))
    print(graph)

    vlist = graph.depthfirstsearch(c)
    for key in vlist:
        print(key, vlist[key])

    print('Depth first search:')
    vlist = graph.depthfirstsearch(hdv)
    for key in vlist:
        print(key, vlist[key])

    print('Depth first search using a stack:')
    vlist = graph.dfs_Stack(hdv)
    for key in vlist:
        print(key, vlist[key])

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

def process_dolphins():
    """ Process the dolphin graph. """
    graph,names = read_dolphin_graph()
    print('Graph has', graph.num_vertices(), 'vertices.')
    print('Graph has', graph.num_edges(), 'edges.')
    # for v in sorted(graph.vertices()):
    for v in graph.vertices():
        print(v, names[v.element()], '; deg =', graph.degree(v))
        #For comparison, print out element with highest degree.
    hdv = graph.highestdegreevertex()
    print(hdv.element(),
        '(', names[hdv.element()], ')'
        'has the highest degree =',
        graph.degree(hdv))

process_dolphins()
test_graph()
