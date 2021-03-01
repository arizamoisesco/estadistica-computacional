class Campo:

    def __init__(self):
        #Donde andan los borrachos en este campo
        self.coordenadas_borracho = {}
    
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_borracho[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_borracho[borracho]
        nueva_coordenada = coordenada_actual.mover(deltax, delta_y)

        self.coordenadas_borracho[borracho] = nueva_coordenada 

    def obtener_coordenada(self, borracho):
        return self.coordenadas_borracho[borracho]
