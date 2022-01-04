from hypergraph_def import Hypergraph
from vertex_def import Vertex
class Hyperedge:

    #=========================CONSTRUCTOR=========================
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
    
    #=========================GETTERS AND SETTERS=========================
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