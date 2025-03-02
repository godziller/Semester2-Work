#class VERTEX
class Vertex:
    def __init__(self, element):
        self._element = element     #the finest data -> stores our vertex data -> 'granny smith'

    def __str__(self):              #string representation of vertex
        return str(self._element)

    def element(self):              #getter for element
        return self._element

    def __lt__(self, v):            #lt dunder for comparison
        return self._element < v.element()


#class EDGE
class Edge: 
    def __init__(self, v, w, element):
        #v = vertex object
        #w = another vertex object
        #element = a LABEL -> name of edge
        self._vertices = (v,w)      #saved in touple
        self._element = element     #saving & protecting label

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    def vertices(self):
        return self._vertices

    def opposite(v):
        if self._vertices[0] == v:      #if first vertex in touple == the desired vertex.
            return self._vertices[1]    #return vertex incident to the current.
        elif self._vertices[1] == v:    #if 2nd vertex == the desired vertex.
            return self._vertices[0]    #return incident vertex
        else:                           #if there is no opposite variable -> None
            return None

    def element(self):
        return self._element            #returns label

    def start(self):
        return self._vertices[0]        #get the vertex at the start of the edge x---o

    def end(self):
        return self._vertices[1]        #get the vertex at the 'end' of the edge o---x


#class Graph
class Graph:
    def __init__(self):
        self._structure = dict()        #create a dictionary for our structure -> easiest data type to 
                                        #work with for GraphADT

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
        return len(self._structure)     #SE

    def num_edges(self):
        num = 0                                 #counter for edge counter (needed for legible division)
        for v in self._structure:               #for every vertex in the structure(Graph)
            num += len(self._structure[v])      #add up the number of vertices from start to the point
        return num // 2                         #floor divide this to get amount of edges between.

    def vertices(self):
        return [key for key in self._structure]     #list comp, get all vertices in structure(Graph)

    def get_vertex_by_label(self,element):          
        #get the first vertex that matches the element (label)
        for v in self._structure:               #for all vertices in the structure
            if v.element() == element:          #if the vertex's label == chosen label
                return v                        #return that VERTEX
        return None                             #SE

    def edges(self):
        for v in self._structure:           
            edgelist = []                       #creating python list to house edges
            for w in self._structure:           #for every EDGE in the structure
                edgelist.append(self._structure[v][w])      #append edge to edgelist 
            return edgelist                     #return list of edges.
        return None                             #SE

    def get_edge(self,v,w):
        if (self._structure != None and v in self._structure and w in self._structure[v]):
            return self._structure[v][w]    #return edge from dictionary
        return None

    def degree(self,v):
        return len(self._structure[v])      #SE

    #functions for modding the graph

    def add_vertex(self,element):
        v = Vertex(element)                 #create new vertex object
        self._structure[v] = dict()         #create a new dictionary on vertex key
        return v                            #return this vertex

    def add_vertex_if_new(self, element):   
        for v in self._structure:           #for every vertex in graph
            if v.element() == element:      #if the vertex's element == desired element
                return v                    #already in graph
            return self._add_vertex(element)    #funnel into add_vertex(). Create vertex.

    def add_edge(self,v,w,element):
        if not v in self._structure or not w in self._structure:        #if either vertex is missing
            return None                                                 #we cannot add an edge.
        e = Edge(v,w,element)               #create Edge object
        self._structure[v][w] = e           #create edge between vertices
        self._structure[w][v] = e           #...
        return e 

    def add_edge_pair(self,elist):          
        for (v,w) in elist:                 #if edge between vertices already exists
            self.add_edge(v,w,None)         #overwriting safely

    def highestdegreevertex(self):      
        hd = -1                             
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v 
        return hdv 

#testing graph
def test_graph():
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
