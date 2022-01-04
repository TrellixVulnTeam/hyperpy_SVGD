class Vertex:

    #=========================CONSTRUCTOR=========================
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
    
    #=========================GETTERS AND SETTERS=========================
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