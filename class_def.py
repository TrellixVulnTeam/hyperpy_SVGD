import numpy as np

class Vertex:

    def __init__(self, hype, name, weight):
        """Constructor for Vertex class.

        Args:
            hype (Hypergraph): The hypergraph the vertex belongs to.
            name (String): The name of the vertex.
            weight (Float): The weight associated with the vertex.
        """
        #TODO Validate the hype input
        self.__hype = hype
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
        #TODO Validate the hype input
        self.__hype = hype
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
            name (String, optional): The name of the hypergraph. Defaults to Hypergraph.
            elist (list): [description]
            vnames (list): [description]
            enames (list): [description]
            vweights (list, optional): [description]. Defaults to None.
            eweights ([type], optional): [description]. Defaults to None.
        """
        self.set_name(name)
        
        if (vweights is None):
            vweights = np.ones(len(vnames))
        if (eweights is None):
            eweights = np.ones(len(enames))
        
        vertex_set = []
        for i in range(len(vnames)):
            vertex_set.append(Vertex(hype = self, name = vnames[i], weight = vweights[i]))
        self.__vertex_set = vertex_set

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
        for v in self.vertex_set():
            if (v.name() == name):
                return v
        return None
    
    def get_hyperedge_by_name(self, name):
        for h in self.hyperedge_set():
            if (h.name() == name):
                return h


    #=========================GETTERS AND SETTERS=========================
    def name(self):
        return self.__name
    
    def vertex_set(self):
        return self.__vertex_set
    
    def hyperedge_set(self):
        return self.__hyperedge_set
    
    def set_name(self, name):
        self.__name = name