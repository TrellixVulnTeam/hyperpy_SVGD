import numpy as np
from itertools import chain

class Vertex:

    def __init__(self, hype, name, weight):
        """Constructor for Vertex class.

        Args:
            hype (Hypergraph): The hypergraph the vertex belongs to.
            name (String): The name of the vertex.
            weight (Float): The weight associated with the vertex.
        """
        self.__set_hype(hype)
        self.set_name(name)
        self.set_weight(weight)
    
    def parent_hypergraph(self):
        """Return the hypergraph that the vertex belongs to.

        Returns:
            [Hypergraph]: The hypergraph that the vertex belongs to.
        """
        return self.__hype

    def name(self):
        """Return the name of the vertex.

        Returns:
            String: The name of the vertex.
        """
        return self.__name
    
    def weight(self):
        """Return the weight of a vertex.

        Returns:
            Float: The weight associated with a vertex.
        """
        return self.__weight

    def __set_hype(self, hype):
        """Set the parent hypergraph of a vertex.

        Args:
            hype (Hypergraph): The parent hypergraph of the vertex.
        """
        self.__hype = hype

    def set_name(self, name):
        """Set the name of a vertex.

        Args:
            name (String): The new name for the vertex.
        """
        self.__name = name

    def set_weight(self, weight):
        """Set the weight of a vertex.

        Args:
            weight (Float): The new weight for the vertex.
        """
        self.__weight = weight

class Hyperedge:

    def __init__(self, hype, name, vertices, weight):
        """Constructor for Hyperedge class.

        Args:
            name (String): The name of the hyperedge
            vertices (list): A list of the vertices contained in the hyperedge
            weight (Float): The weight associated with the hyepredge.
        """
        self.__set_hype(hype)
        self.set_name(name)
        self.set_vertices(vertices)
        self.set_weight(weight)
    
    def parent_hypergraph(self):
        """Return the hypergraph that the hyperedge belongs to.

        Returns:
            Hypergraph: The hypergraph object that the hyperedge belongs to.
        """
        return self.__hype

    def name(self):
        """Access the name of the hyperedge.

        Returns:
            String: The name of the hyperedge.
        """
        return self.__name

    def vertices(self):
        """Access the vertices contained in the hyperedge.

        Returns:
            list: A list of the vertices contained in the hyperedge.
        """
        return self.__vertices
    
    def weight(self):
        """Access the weight of the hyperedge.

        Returns:
            Float: The weight asspciated with the hyperedge.
        """
        return self.__weight
    
    def __set_hype(self, hype):
        """Set the parent hypergraph of the hyperedge

        Args:
            hype (Hypergraph): The hypergraph the hyperedge is a member
        """
        self.__hype = hype
    
    def set_name(self, name):
        """Set the name of the hyperedge.

        Args:
            name (String): The new name of the hyperedge.
        """
        self.__name = name
    
    def set_vertices(self, vertices):
        """Set the vertices contained in a hyperedge.

        Args:
            vertices (list): A list of the vertices contained in the hyperedge.
        """
        self.__vertices = vertices
    
    def set_weight(self, weight):
        """Set the weight of the hyperedge.

        Args:
            weight (Float): The weight to set the hyperedge weight to.
        """
        self.__weight = weight
    
class Hypergraph:

    def __init__(self, elist, vnames, enames, vweights = None, eweights = None, name = "Hypergraph"):
        """Hypergraph Constructor

        Args:
            elist (list): Each hyperedge should have a list with the name of each of the vertices it contains. elist is a
                liist of those lists.
            vnames (list): A list of the names of the vertices.
            enames (list): A list of the names of the hyperedges.
            vweights (list, optional): A list of the weights of the vertices. Defaults to None that will assign a weight of 1
                to each vertex.
            eweights (list, optional): A list of the weights of the hyperedges. Defaults to None that will assign a weight of 1
                to each hyperedge.
            name (String, optional): The name of the hypergraph. Defaults to Hypergraph.
        """
        self.set_name(name)
        
        #Adding vertex and hyepredge weights if they are not given
        if (vweights is None):
            vweights = np.ones(len(vnames))
        if (eweights is None):
            eweights = np.ones(len(enames))
        
        #Creating vertex set
        vertex_set = []
        for i in range(len(vnames)):
            vertex_set.append(Vertex(hype = self, name = vnames[i], weight = vweights[i]))
        self.__vertex_set = vertex_set

        #Creating hyperedge set
        hyperedge_set = []
        for i in range(len(elist)):
            vertices = []
            for vname in elist[i]:
                vertex = self.get_vertex_by_name(vname)
                vertices.append(vertex)
            hyperedge_set.append(Hyperedge(hype = self, name = enames[i], vertices = vertices, weight = eweights[i]))
        self.__hyperedge_set = hyperedge_set


    #=========================METHODS===============================
    def get_vertex_by_name(self, name):
        """Find a vertex of a hypergraph using its name. Will return the first vertex it finds with the given name.

        Args:
            name (String): The name of the vertex to search for.

        Returns:
            Vertex: The first vertex found with the given name. If none are found will return None.
        """
        for v in self.vertex_set():
            if (v.name() == name):
                return v
        return None
    
    def get_hyperedge_by_name(self, name):
        """Find a hyperedge of a hypergraph using its name. Will return the furst hyperedge it finds with the given name.

        Args:
            name (String): The name of the hyperedge to search for.

        Returns:
            Hyperedge: The first hyperedge found with the given name. If none are found will return None.
        """
        for h in self.hyperedge_set():
            if (h.name() == name):
                return h

    #TODO Test this vertex_neighbours function
    def vertex_neighbors(self, vertex):
        """Find the neighbours of a given vertex of a hypergraph

        Args:
            vertex (Vertex): The vertex to find the neighbours of.

        Returns:
            list: A list of the vertices that are adjacent to the given vertices.
        """
        #Neighbours of the vertex
        neighbours = []
        #Check every hyperedge as to whether it contains the vertex then append all vertices in the hyperedge to neighbours
        for h in self.hyperedge_set():
            if vertex in h.vertices():
                neighbours.append(h.vertices())
        #Unnest the neighbours list
        neighbours = list(chain.from_iterable(neighbours))
        #Make sure every element of the list is unique
        neighbours_unique = []
        for v in neighbours:
            if (v not in neighbours_unique) & (v not in [vertex]):
                neighbours_unique.append(v)
        return neighbours_unique

    #=========================GETTERS AND SETTERS=========================
    def vertex_set(self):
        """Access the vertex set of a hypergraph.

        Returns:
            list: A list of the vertuces contained in the hypergraph.
        """
        return self.__vertex_set
    
    def hyperedge_set(self):
        """Access the hyperedge set of a hypergraph.

        Returns:
            list: A list of the hyperedges contained in the hypergraph.
        """
        return self.__hyperedge_set
    
    def name(self):
        """Access the name of a hypergraph.

        Returns:
            String: The name of the hypergraph.
        """
        return self.__name

    def set_name(self, name):
        """Set the name of a hypergraph.

        Args:
            name (String): The new name for the hypergraph.
        """
        self.__name = name
