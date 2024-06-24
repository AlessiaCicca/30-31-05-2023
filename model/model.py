import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.getNazioni=DAO.getNazione()
        self.grafo = nx.Graph()
        self.allrivenditori=DAO.getAllRivenditori()
        self._idMap = {}
        for v in self.allrivenditori:
            self._idMap[v.Retailer_code] = v
        self._idMapNome = {}
        for v in self.allrivenditori:
            self._idMapNome[v.Retailer_name] = v

    def creaGrafo(self,nazione, anno, numeroProdotti):
        self.nodi = DAO.getNodi(nazione)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges( nazione,anno, numeroProdotti)
        return self.grafo

    def addEdges(self,  nazione,anno, numeroProdotti):
         self.grafo.clear_edges()
         allEdges = DAO.getConnessioni(nazione,anno, numeroProdotti)
         for connessione in allEdges:
             nodo1 = self._idMap[connessione.v1]
             nodo2 = self._idMap[connessione.v2]
             if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                 if self.grafo.has_edge(nodo1, nodo2) == False:
                     self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)
    def getArchi(self):
        lista=[]
        for arco in self.grafo.edges:
            lista.append((arco[0],arco[1], self.grafo[arco[0]][arco[1]]["weight"]))
        ordinaLista=sorted(lista,key=lambda x:x[2], reverse=False)
        return ordinaLista
    def getAnalisi(self,rivenditore):
        rivenditoreNodo=self._idMapNome[rivenditore]
        somma=0
        nodiConnessi= list(nx.node_connected_component(self.grafo,rivenditoreNodo))
        sottoGrafo=self.grafo.subgraph(nodiConnessi)
        for arco in sottoGrafo.edges:
            somma+= self.grafo[arco[0]][arco[1]]["weight"]
        return len(nodiConnessi), somma


