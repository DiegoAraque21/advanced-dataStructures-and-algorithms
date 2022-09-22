

class Graph:


    def __init__(self) :
        
        self.adj_list = {} #Crea una lista de adyacencia en la que se guardan las conexiones
        #de cada vertice

    
    def addVertex( self, vertex ):
    
        #Verificar si no existe ese vertice
        # por que no puede haber repetidos
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        
        return False
    

    def addEdge(self,v1,v2):
        '''
        Funcion que agrega un vinculo entre dos vertices
        '''
        
        #Verificar que ambos vertices existan antes de crear una conexion
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

            return True
        
        return False

        
    def remove_edge(self,v1,v2):
        #Solo se puede borrar conexion si ambos items existen y ademas si existe una conexion entre ellos
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():

            try:
                    
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass

            return True

        return False

    
    def remove_vertex(self,v):
        '''
        Funcion que borra un elemento del grafo
        '''
        #Checar si exist el elemento
        if v in self.adj_list.keys():
            
            #Iterar en la lista del elemento para encontrar las conexiones con otros vertices
            for other_vertex in self.adj_list[v]:
                    
                #Si encuentr una conexion, entoneces ir a la lista de conexiones
                # del otro vertice y borrar el que se desea eliminar
                self.adj_list[other_vertex].remove(v) 

            #Borrar el vertice del mapa
            del self.adj_list[v]
            return True
        
        return False



    def print_graph(self):


        for vertex in self.adj_list:

            print( f'{vertex} : {self.adj_list[vertex]}')