##      Abygail Stiekman    ##
##           aes15d         ##

from __future__ import print_function
import string

class Graph(object):

        def __init__(self):
                self.vertexlist = []
                self.edgelist = []
                self.numedge = 0
                self.numvertices = 0

        def add_vertex(self, name):
                """add vertex identified by the string name"""
                check = False
                for item in self.vertexlist:
                        if name == item:
                                check = True
                                break
                if check is False:
                        self.vertexlist.append(name)
                        self.numvertices = self.numvertices+1
                else:
                        print ("A vertex with name %s already exists." % name)

        def add_edge(self, start,end):
                """adds a directed edge between the vertices"""
                if start not in self.vertexlist:
                        self.vertexlist.append(start)
                        self.numvertices +=1

                if end not in self.vertexlist:
                        self.vertexlist.append(end)
                        self.numvertices += 1

        def remove_vertex(self, name):
                """removes the vertex identified by the string name"""
                if name in self.vertexlist:
                        self.vertexlist.remove(name)
                        self.numvertices = self.numvertices -1

        def remove_edge(self, start,end):
                """removes a single directed edge between the vertices"""
                for item in self.edgelist:
                        if item[0] is start and item[1] is end:
                                self.vertexlist.remove(name)
                                self.numvertices = self.numvertices -1
        def vertices(self):
                """return a list of vertex names"""
                return self.vertexlist

        def print_edges(self):
                """prints each directed graph edge on a new line"""
                for i in self.edgelist:
                        print (i[0] + " -> " + i[1])

        def is_connected(self, start,end):
                """returns T or F if edges are connected"""
                for item in self.edgelist:
                        if item[0] is start and item[1] is end:
                                return True
                return False

        def print_paths(self, start,end):
                """prints all possible paths from start to end"""
                temp = self.finder(start, end)
                print (temp)

        def finder(self, begin, finish, s = None):
                if s is None:
                        s = []
                s = s + [begin]
                if begin == finish:
                        return [s]
                path = []
                for item in self.edgelist:
                        if item[0] not in s:
                                new_path = self.finder(item[0], finish,s)
                                for i in new_path:
                                        path.append(i)
                return path



class UndirectedGraph(Graph):

        def __init__(self):
                Graph.__init__(self)

        def add_edge(self, start, end):
                """adds edge and numvertices, both aways"""
                if end not in self.vertexlist:
                        self.vertexlist.append(end)
                        self.numvertices +=1

                if start not in self.vertexlist:
                        self.vertexlist.append(start)
                        self.numvertices += 1

        def remove_edge(self, start, end):
                 for item in self.edgelist:
                        if item[1] is start and item[0] is end:
                                self.vertexlist.remove(name)
                                self.numvertices = self.numvertices -1

        def print_edges(self):
                """works either way for undirected graph"""
                for i in self.edgelist:
                        print (i[0] + " <-> " + i[1])

        def print_paths(self, start,end):
                """prints all possible paths from start to end"""
                temp = self.finder(start, end)
                print (temp)

        def finder(self, begin, finish, s = None):
                if s is None:
                        s = []
                s = s + [begin]
                if begin == finish:
                        return [s]
                path = []
                for item in self.edgelist:
                        if item[0] not in s:
                                new_path = self.finder(item[0], finish,s)
                                for i in new_path:
                                        path.append(i)
                        if item[1] not in s:
                                new_path = self.finder(item[1], finish,s)
                                for i in new_path:
                                        path.append(i)
                return path
