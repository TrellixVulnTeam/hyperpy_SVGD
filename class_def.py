import numpy as np

class Vertex:

    def __int__(self, hype, name, weight):
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

    #TODO Write Hyeprgraph constructor
    def __init__(self, name, elist, vnames, enames, vweights = None, eweights = None):
        self.set_name(name)
        if (len(elist) != len(vnames)):
            raise ValueError
        if (len(elist) != len(enames)):
            raise ValueError
        if (vweights is None):
            vweights =np.ones(len(enames))
        elif (len(elist) != len(vnames)):
            raise ValueError
        if (eweights is None):
            eweights =np.ones(len(enames))
        elif (len(elist) != len(eweights)):
            raise ValueError
        
        vertex_set = []
        for i in range(len(enames)):
            vertex_set.append(Vertex(hype = self, name = vnames[i], weight = vweights[i]))
        self.__vertex_set = vertex_set

    
    def name(self):
        return self.__name
    
    def vertex_set(self):
        return self.__vertex_set
    
    def hyperedge_set(self):
        return self.__hyperedge_set
    
    def set_name(self, name):
        self.__name = name

v = [1,2,3,4,5,6,7,8,9]
print(v[[1,4,5]])