import numpy as np
from itertools import chain
from hyperedge_def import Hyperedge
from vertex_def import Vertex
    
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
