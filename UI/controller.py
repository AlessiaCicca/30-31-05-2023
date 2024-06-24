import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        nazione = self._view.dd_nazione.value
        if nazione is None:
            self._view.create_alert("Selezionare una Nazione")
            return
        anno = self._view.dd_anno.value
        if anno is None:
            self._view.create_alert("Selezionare un Anno")
            return
        nProdotti= self._view.txt_prodotti.value
        if nProdotti == "":
            self._view.create_alert("Inserire un valore numerico per il numero di prodotti in comune")
            return
        grafo = self._model.creaGrafo(nazione, int(anno), int(nProdotti))
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for rivenditore in grafo.nodes:
            self._view.txt_result.controls.append(ft.Text(f"{rivenditore}"))
            self._view.dd_rivenditore.options.append(ft.dropdown.Option(
                text=rivenditore))

        archiOrdinati=self._model.getArchi()
        for (arco1,arco2,peso) in archiOrdinati:
            self._view.txt_result.controls.append(ft.Text(f"{peso}:{arco1}<->{arco2}"))
        self._view.update_page()

    def handle_analizza(self,e):
        rivenditore = self._view.dd_rivenditore.value
        if rivenditore is None:
            self._view.create_alert("Selezionare un rivenditore")
            return
        dimensione,peso=self._model.getAnalisi(rivenditore)
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa di {rivenditore} ha dimensione {dimensione} e il "
                                                      f"peso totale degli archi della componente connessa è {peso}"))
        self._view.update_page()

    def fillDD(self):
        ann="201"
        for i in range(5,9):
            anno=ann+str(i)
            self._view.dd_anno.options.append(ft.dropdown.Option(
                               text=anno))
        nazioni=self._model.getNazioni
        for nazione in nazioni:
            self._view.dd_nazione.options.append(ft.dropdown.Option(
                text=nazione))
