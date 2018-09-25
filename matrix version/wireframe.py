import math
import numpy as np

class Wireframe:
    def __init__(self):
        self.nodes = np.zeros((0,4))
        self.edges = []

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    def addEdges(self, edgeList):
        self.edges += edgeList

    def outputNodes(self):
        print("\n --- Nodes ---")
        for i, (x,y,z, _) in enumerate(self.nodes):
            print(" %d: (%.2f, %.2f, %.2f)" % (i, x, y, z))

    def outputEdges(self):
        print("\n --- Edges ---")
        for i, (node1,node2) in enumerate(self.edges):
            print("   %d: %d -> %d" % (i, node1, node2))

    def transform(self, matrix):
        """apply a transformation definded by a given matrix"""
        #this means that the nature of the matrix determines the transformation (translation,scaling..)
        self.nodes = np.dot(self.nodes, matrix)

    def findCentre(self):
        num_nodes = self.nodes.shape[0]
        sumas = np.sum(self.nodes,axis=0)
        meanX = sumas[0] / num_nodes
        meanY = sumas[1] / num_nodes
        meanZ = sumas[2] / num_nodes

        return (meanX, meanY, meanZ)

#--------------- Auxiliar functions -------------------

def translationMatrix(dx=0,dy=0,dz=0):
    """return matrix for translation along vector (dx,dy,dz)"""
    return np.array([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,0],
                     [dx,dy,dz,1]])

def scaleMatrix(sx=0,sy=0,sz=0):
    """return matrix for scaling equally (point of reference TODO)"""
    return np.array([[sx,0,0,0],
                     [0,sy,0,0],
                     [0,0,sz,0],
                     [0,0,0,1]])

def rotateZMatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[c, -s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def rotateXMatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[1, 0, 0, 0],
                     [0, c, -s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])

def rotateYMatrix(radians):
    c = np.cos(radians)
    s = np.sin(radians)
    return np.array([[c, 0, s, 0],
                     [0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [0, 0, 0, 1]])