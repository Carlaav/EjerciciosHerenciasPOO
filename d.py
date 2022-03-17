from lib2to3.pgen2.literals import simple_escapes


class Casa:
    def __init__(self):
        
        self.pared_norte = self.Pared("NORTE", 50)
        self.pared_oeste = self.Pared("OESTE", 30)
        self.pared_sur = self.Pared("SUR", 60)
        self.pared_este = self.Pared("ESTE", 100)
        
        
        
        self.ventana_norte = self.Ventana(self.pared_norte, 0.5) 
        self.ventana_oeste = self.Ventana(self.pared_oeste, 1) 
        self.ventana_sur = self.Ventana(self.pared_sur, 2) 
        self.ventana_este = self.Ventana(self.pared_este, 1) 
    
    class Pared:
        def __init__(self, orien, dimension):
            self.orientacion = orien
            self.dimension = dimension
        
    
    class Ventana:
        def __init__(self, pared, ven_dim):
            self.pared = pared
            self.dimen = ven_dim
            
    def dimensionesCasa(self):
        dimensiones = self.pared_norte.dimension - self.ventana_norte.dimen
        dimensiones = dimensiones + self.pared_oeste.dimension - self.ventana_oeste.dimen
        dimensiones = dimensiones + self.pared_sur.dimension - self.ventana_sur.dimen
        dimensiones = dimensiones + self.pared_este.dimension - self.ventana_este.dimen
        
        return dimensiones
    
casa = Casa()
print(casa.dimensionesCasa())