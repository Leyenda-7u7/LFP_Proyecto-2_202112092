import tokenL as t
import analisis


class AutomatasAnalizadorLexico:

    def __init__(self):
        self.aut_crear_bd = self.automata_crearBD()
        self.aut_eliminar_bd = self.automata_eliminarBD()
        self.aut_crear_coleccion = self.automata_crear_coleccion()
        self.aut_eliminar_coleccion = self.automata_eliminar_coleccion()
        self.aut_insertar_unico = self.automata_insertar_unico()
        self.aut_actualizar_unico = self.automata_actualizar_unico()
        self.aut_eliminar_unico = self.automata_eliminar_unico()
        self.aut_buscar_todo = self.automata_buscar_todo()
        self.aut_buscar_unico = self.automata_buscar_unico()
        self.aut_nueva = self.automata_nueva()
        self.aut_numero = self.automata_numero()
        self.aut_cadena = self.automata_cadena()
        self.aut_identificador = self.automata_identificador()
        self.aut_set = self.automata_set()

    def automata_crearBD(self) :
        token = "CREAR_BD"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', True)

        x0.agregar_transicion('C', x1)
        x1.agregar_transicion('r', x2)
        x2.agregar_transicion('e', x3)
        x3.agregar_transicion('a', x4)
        x4.agregar_transicion('r', x5)
        x5.agregar_transicion('B', x6)
        x6.agregar_transicion('D', x7)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7]
        inicio = x0

        automata = analisis.analisis("Crear BD", estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_eliminarBD(self) :
        token = "ELIMINAR_BD"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', True)

        x0.agregar_transicion('E', x1)
        x1.agregar_transicion('l', x2)
        x2.agregar_transicion('i', x3)
        x3.agregar_transicion('m', x4)
        x4.agregar_transicion('i', x5)
        x5.agregar_transicion('n', x6)
        x6.agregar_transicion('a', x7)
        x7.agregar_transicion('r', x8)
        x8.agregar_transicion('B', x9)
        x9.agregar_transicion('D', x10)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
        inicio = x0

        automata = analisis.analisis('Automata Eliminar BD', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_crear_coleccion(self) :
        token = "CREAR_COLECCION"
        nombre = 'Automata Crear Coleccion'

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', False)
        x12 = analisis.Estado('x12', False)
        x13 = analisis.Estado('x13', False)
        x14 = analisis.Estado('x14', True)

        x0.agregar_transicion('C', x1)
        x1.agregar_transicion('r', x2)
        x2.agregar_transicion('e', x3)
        x3.agregar_transicion('a', x4)
        x4.agregar_transicion('r', x5)
        x5.agregar_transicion('C', x6)
        x6.agregar_transicion('o', x7)
        x7.agregar_transicion('l', x8)
        x8.agregar_transicion('e', x9)
        x9.agregar_transicion('c', x10)
        x10.agregar_transicion('c', x11)
        x11.agregar_transicion('i', x12)
        x12.agregar_transicion('o', x13)
        x13.agregar_transicion('n', x14)

        estados = [x0, x1, x2, x3, x4, x5, x6,
                   x7, x8, x9, x10, x11, x12, x13, x14]
        inicio = x0

        automata = analisis.analisis('Automata Crear Coleccion', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_eliminar_coleccion(self):
        token = "ELIMINAR_COLECCION"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', False)
        x12 = analisis.Estado('x12', False)
        x13 = analisis.Estado('x13', False)
        x14 = analisis.Estado('x14', False)
        x15 = analisis.Estado('x15', False)
        x16 = analisis.Estado('x16', False)
        x17 = analisis.Estado('x17', True)

        x0.agregar_transicion('E', x1)
        x1.agregar_transicion('l', x2)
        x2.agregar_transicion('i', x3)
        x3.agregar_transicion('m', x4)
        x4.agregar_transicion('i', x5)
        x5.agregar_transicion('n', x6)
        x6.agregar_transicion('a', x7)
        x7.agregar_transicion('r', x8)
        x8.agregar_transicion('C', x9)
        x9.agregar_transicion('o', x10)
        x10.agregar_transicion('l', x11)
        x11.agregar_transicion('e', x12)
        x12.agregar_transicion('c', x13)
        x13.agregar_transicion('c', x14)
        x14.agregar_transicion('i', x15)
        x15.agregar_transicion('o', x16)
        x16.agregar_transicion('n', x17)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8,
                   x9, x10, x11, x12, x13, x14, x15, x16, x17]
        inicio = x0

        automata = analisis.analisis('Automata Eliminar Coleccion', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_insertar_unico(self) :
        token = "INSERTAR_UNICO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', False)
        x12 = analisis.Estado('x12', False)
        x13 = analisis.Estado('x13', True)

        x0.agregar_transicion('I', x1)
        x1.agregar_transicion('n', x2)
        x2.agregar_transicion('s', x3)
        x3.agregar_transicion('e', x4)
        x4.agregar_transicion('r', x5)
        x5.agregar_transicion('t', x6)
        x6.agregar_transicion('a', x7)
        x7.agregar_transicion('r', x8)
        x8.agregar_transicion('U', x9)
        x9.agregar_transicion('n', x10)
        x10.agregar_transicion('i', x11)
        x11.agregar_transicion('c', x12)
        x12.agregar_transicion('o', x13)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]
        inicio = x0

        automata = analisis.analisis('Automata Insertar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_actualizar_unico(self) :
        token = "TK_ACTUALIZAR_UNICO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', False)
        x12 = analisis.Estado('x12', False)
        x13 = analisis.Estado('x13', False)
        x14 = analisis.Estado('x14', False)
        x15 = analisis.Estado('x15', True)

        x0.agregar_transicion('A', x1)
        x1.agregar_transicion('c', x2)
        x2.agregar_transicion('t', x3)
        x3.agregar_transicion('u', x4)
        x4.agregar_transicion('a', x5)
        x5.agregar_transicion('l', x6)
        x6.agregar_transicion('i', x7)
        x7.agregar_transicion('z', x8)
        x8.agregar_transicion('a', x9)
        x9.agregar_transicion('r', x10)
        x10.agregar_transicion('U', x11)
        x11.agregar_transicion('n', x12)
        x12.agregar_transicion('i', x13)
        x13.agregar_transicion('c', x14)
        x14.agregar_transicion('o', x15)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7,
                   x8, x9, x10, x11, x12, x13, x14, x15]
        inicio = x0

        automata = analisis.analisis('Automata Actualizar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_eliminar_unico(self) :
        token = "TK_ELIMINAR_UNICO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', False)
        x12 = analisis.Estado('x12', False)
        x13 = analisis.Estado('x13', True)

        x0.agregar_transicion('E', x1)
        x1.agregar_transicion('l', x2)
        x2.agregar_transicion('i', x3)
        x3.agregar_transicion('m', x4)
        x4.agregar_transicion('i', x5)
        x5.agregar_transicion('n', x6)
        x6.agregar_transicion('a', x7)
        x7.agregar_transicion('r', x8)
        x8.agregar_transicion('U', x9)
        x9.agregar_transicion('n', x10)
        x10.agregar_transicion('i', x11)
        x11.agregar_transicion('c', x12)
        x12.agregar_transicion('o', x13)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]
        inicio = x0

        automata = analisis.analisis('Automata Eliminar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_buscar_todo(self) :
        token = "TK_BUSCAR_TODO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', True)

        x0.agregar_transicion('B', x1)
        x1.agregar_transicion('u', x2)
        x2.agregar_transicion('s', x3)
        x3.agregar_transicion('c', x4)
        x4.agregar_transicion('a', x5)
        x5.agregar_transicion('r', x6)
        x6.agregar_transicion('T', x7)
        x7.agregar_transicion('o', x8)
        x8.agregar_transicion('d', x9)
        x9.agregar_transicion('o', x10)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]
        inicio = x0

        automata = analisis.analisis('Automata Buscar Todo', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_buscar_unico(self):
        token = "TK_BUSCAR_UNICO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', False)
        x6 = analisis.Estado('x6', False)
        x7 = analisis.Estado('x7', False)
        x8 = analisis.Estado('x8', False)
        x9 = analisis.Estado('x9', False)
        x10 = analisis.Estado('x10', False)
        x11 = analisis.Estado('x11', True)

        x0.agregar_transicion('B', x1)
        x1.agregar_transicion('u', x2)
        x2.agregar_transicion('s', x3)
        x3.agregar_transicion('c', x4)
        x4.agregar_transicion('a', x5)
        x5.agregar_transicion('r', x6)
        x6.agregar_transicion('U', x7)
        x7.agregar_transicion('n', x8)
        x8.agregar_transicion('i', x9)
        x9.agregar_transicion('c', x10)
        x10.agregar_transicion('o', x11)

        estados = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
        inicio = x0

        automata = analisis.analisis('Automata Buscar Unico', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_nueva(self) :
        token = "TK_NUEVA"
    

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', False)
        x5 = analisis.Estado('x5', True)

        x0.agregar_transicion('n', x1)
        x1.agregar_transicion('u', x2)
        x2.agregar_transicion('e', x3)
        x3.agregar_transicion('v', x4)
        x4.agregar_transicion('a', x5)

        estados = [x0, x1, x2, x3, x4, x5]
        inicio = x0

        automata = analisis.analisis('Automata Nueva', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_numero(self) :
        token = "TK_NUMERO"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', True)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', True)

        #x0.agregar_transicion('+', x1)
        x0.agregar_transicion('-', x1)
        x2.agregar_transicion('.', x3)
        for i in range(0, 10):
            x0.agregar_transicion(str(i), x2)
            x1.agregar_transicion(str(i), x2)
            x2.agregar_transicion(str(i), x2)
            x3.agregar_transicion(str(i), x4)
            x4.agregar_transicion(str(i), x4)

        estados = [x0, x1, x2, x3, x4]
        inicio = x0

        automata = analisis.analisis('Automata Numero', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_identificador(self) :
        token = "IDENTIFICADOR"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', True)

        for i in range(65, 91):
            x0.agregar_transicion(chr(i), x1)
            x1.agregar_transicion(chr(i), x1)

        for i in range(97, 123):
            x0.agregar_transicion(chr(i), x1)
            x1.agregar_transicion(chr(i), x1)

        for i in range(0, 10):
            x1.agregar_transicion(str(i), x1)

        x1.agregar_transicion('_', x1)

        estados = [x0, x1]
        inicio = x0

        automata = analisis.analisis('Automata Identificador', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_cadena(self) :
        token = "TK_CADENA"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', True)

        x0.agregar_transicion('"', x1)
        for i in range(32, 127):
            if i != 34:
                x1.agregar_transicion(chr(i), x2)
                x2.agregar_transicion(chr(i), x2)
        x1.agregar_transicion('"', x3)
        x2.agregar_transicion('"', x3)

        estados = [x0, x1, x2, x3]
        inicio = x0

        automata = analisis.analisis('Automata Cadena', estados, token)
        automata.establecer_inicio(inicio)

        return automata

    def automata_set(self) :
        token = "TK_SET"
        

        x0 = analisis.Estado('x0', False)
        x1 = analisis.Estado('x1', False)
        x2 = analisis.Estado('x2', False)
        x3 = analisis.Estado('x3', False)
        x4 = analisis.Estado('x4', True)

        x0.agregar_transicion('$', x1)
        x1.agregar_transicion('s', x2)
        x2.agregar_transicion('e', x3)
        x3.agregar_transicion('t', x4)

        estados = [x0, x1, x2, x3, x4]
        inicio = x0

        automata = analisis.analisis('Automata Set', estados, token)
        automata.establecer_inicio(inicio)

        return automata