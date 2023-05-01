class DropData:
    def __init__(self):
        self.eliminar= ""
        
    def crear_dropData(self):    
        self.eliminar = "db.dropDatabase();" 
        return self.eliminar 
        