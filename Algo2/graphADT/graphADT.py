#class VERTEX
class Vertex:
    def __init__(self, element):
        self._element = element

    def __str__(self):
        ...

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
        sellf._element = element

    def __str__(self):
        ...

    def vertices():
        return self._vertices

    def opposite():
        if self._vertices[0]
#class Graph

