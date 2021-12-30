from abc import ABC, abstractmethod

class Hypergraph(ABC):
    """An abstract class for representing hypergraphs.

    Attributes:
        __inc_mat (unassigned): The incidence matrix of the hypergraph.
        __vnames (list, optional): A list of vertex names. Defaults to None.
        __enames (list, optional): A list of hyperedge names. Defaults to None.
        __vweights (list, optional): A list of vertex names. Defaults to None.
        __eweights (list, optional): A list of hyperedge weights. Defaults to None.
    """

    #=========================CONSTRUCTOR=================================
    def __init__(self, inc_mat, vnames = None, enames = None, vweights = None, eweights = None):
        """Class constructor to create an abstract hypergraph object.

        Args:
            inc_mat (unassigned): A representation of the hypergraph incidence matrix.
            vnames (list, optional): A list of vertex names. Defaults to None.
            enames (list, optional): A list of hyperedge names. Defaults to None.
            vweights (list, optional): A list of vertex weights. Defaults to None.
            eweights (list, optional): A list of hyperedge weights. Defaults to None.
        """
        self.__inc_mat = inc_mat
        self.rename_vertices(vnames)
        self.rename_hyperedges(enames)
        self.set_vertex_weights(vweights)
        self.set_hyperedge_weights(eweights)
    
    #=========================GETTERS AND SETTERS=========================
    def vertices(self):
        """Access the names of the vertices of the hypergraph.

        Returns:
            list: The names of the vertices of the hypergraph
        """
        return self.__vnames

    def hyperedges(self):
        """Access the names of the hyperedges of the hypergraph

        Returns:
            list: The names of the hyperedges of the hypergraph
        """
        return self.__enames

    def vertex_weights(self):
        """Access the weights of the vertices of the hypergraph.

        Returns:
            list: A list of the weights of the vertices of the hypergraph.
        """
        return self.__vweights
    
    def hyperedge_weights(self):
        """Access the weights of the hyperedges of the hypergraph.

        Returns:
            list: A list of the weights of the hyperedges of the hypergraph.
        """
        return self.__eweights

    @abstractmethod
    def rename_vertices(self, vnames):
        """Set the names of the vertices of a hypergraph. If vnames is None then the vertex names are set to sequential
        integers (as strings).

        Args:
            vnames (list): A list of the names to use for the vertices of the hyeprgraph (if None then defaults are used).
        """
        self.__vnames = vnames
    
    @abstractmethod
    def rename_hyperedges(self, enames):
        """Set the names of the hyperedges of a hypergraph. If enames is None then the hyperedge names are set to sequential
        integers (as strings).

        Args:
            enames (list): A list of the names to use for the hyperedges of the hypergraph (if None then defaults are used).
        """
        self.__enames = enames

    @abstractmethod
    def set_vertex_weights(self, vweights):
        """Set the weights of the vertices of a hypergraph. If vweights is None then the vertex weights are all set to 1.

        Args:
            vweights (list): A list of the weights to use for the vertices of the hypergraph (if None then defaults are used).
        """
        self.__vweights = vweights

    @abstractmethod
    def set_hyperedge_weights(self, eweights):
        """Set the weights of the hyperedges of the hypergraph. If eweights is None then the hyperedge weights are all set to 1.

        Args:
            eweights (list): A list of the weights to use for the hyperedges of the hypergraph (if None then defaults are used).
        """
        self.__eweights = eweights