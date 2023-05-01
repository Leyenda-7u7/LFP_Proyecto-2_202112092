
import tokenL as t
import auto as aal
from typing import List


class AnalizadorLexico:

    def __init__(self):
        self.fila = 1
        self.columna = 1
        self.puntero = 0
        self.posicion_actual = 0
        self.entrada = ''
        self.automatas = aal.AutomatasAnalizadorLexico()
        self.tokens: List[t.LToken] = []
        self.alfanumericos = ['_']

        for i in range(65, 91):
            self.alfanumericos.append(chr(i))
        
        for i in range(97, 123):
            self.alfanumericos.append(chr(i))

        for i in range(0, 10):
            self.alfanumericos.append(str(i))

    def analizar(self, entrada):
        self.entrada = entrada
        cadena_auxiliar = ''

        while self.puntero < len(self.entrada):
            cadena_auxiliar += self.entrada[self.puntero]
            self.columna += 1

            if cadena_auxiliar == ' ':
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '=':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_IGUAL", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '\n' or cadena_auxiliar == '\r':
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
                self.fila += 1
                self.columna = 1
            elif cadena_auxiliar == ',':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_COMA", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ';':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "TOKEN_PUNTOCOMA", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ':':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "TOKEN_DOSPUNTOS", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '(':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_PARENTESISABRE",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ')':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_PARENTESISCIERRA",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '{':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken(
                    "TOKEN_LLAVEABRE", cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '}':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_LLAVECIERRA",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == '[':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_CORCHETEABRE",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            elif cadena_auxiliar == ']':
                fila = self.fila
                columna = self.columna - len(cadena_auxiliar)
                token = t.LToken("TOKEN_CORCHETECIERRA",cadena_auxiliar, fila, columna)
                self.tokens.append(token)
                self.posicion_actual += len(cadena_auxiliar)
                cadena_auxiliar = ''
                self.puntero = self.posicion_actual
            else:
                self.columna -= 1
                resultado = self.analizar_crearBD()

                if resultado is None:
                    resultado = self.analizar_eliminarBD()

                    if resultado is None:
                        resultado = self.analizar_crear_coleccion()

                        if resultado is None:
                            resultado = self.analizar_eliminar_coleccion()

                            if resultado is None:
                                resultado = self.analizar_insertar_unico()

                                if resultado is None:
                                    resultado = self.analizar_actualizar_unico()

                                    if resultado is None:
                                        resultado = self.analizar_eliminar_unico()

                                        if resultado is None:
                                            resultado = self.analizar_buscar_todo()

                                            if resultado is None:
                                                resultado = self.analizar_buscar_unico()

                                                if resultado is None:
                                                    resultado = self.analizar_nueva()

                                                    if resultado is None:
                                                        resultado = self.analizar_set()

                                                        if resultado is None:
                                                            resultado = self.analizar_numero()

                                                            if resultado is None:
                                                                resultado = self.analizar_cadena()

                                                            if resultado is None:
                                                                resultado = self.analizar_identificador()

                if resultado is None:
                    print('Error')
                else:
                    cadena_auxiliar = resultado[0]
                    token = resultado[1]
                    fila = self.fila
                    columna = self.columna - len(cadena_auxiliar)
                    token.fila = fila
                    token.columna = columna
                    self.tokens.append(token)
                    self.posicion_actual += len(cadena_auxiliar)
                    cadena_auxiliar = ''
                    self.puntero = self.posicion_actual

        
        print('\n++++++++++++++++++++++++++ TOKENS ++++++++++++++++++++++++++')
        for token in self.tokens:
            print(token)

        
        return self.tokens    

        

    def analizar_crearBD(self):
        columna = self.columna
        puntero_inicial = self.puntero

        cadena = ''
        longitud = len(self.entrada)
        # Se construye la cadena y se intenta validar
        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_crear_bd.analizar(cadena)
            
            self.columna += 1
            self.puntero += 1
            
            # si no retorna None es porque la cadena es valida
            # se verifica el siguiente caracter para ver si se trata de un identificador o una palabra reservada
            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.puntero = puntero_inicial
        self.columna = columna
        return resultado

    def analizar_eliminarBD(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_bd.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_crear_coleccion(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_crear_coleccion.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_eliminar_coleccion(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_coleccion.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_insertar_unico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_insertar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_actualizar_unico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_actualizar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_eliminar_unico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_eliminar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_buscar_todo(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_buscar_todo.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_buscar_unico(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_buscar_unico.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_nueva(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_nueva.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_set(self):
        columna = self.columna
        puntero_inicial = self.puntero
        #caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_set.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                if caracter_actual in self.alfanumericos:
                    resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado
    
    def analizar_numero(self):
        columna = self.columna
        puntero_inicial = self.puntero
        caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while caracter_actual != ' ' and caracter_actual != '\n' and caracter_actual != ',':
            cadena += caracter_actual
            self.columna += 1
            self.puntero += 1
            caracter_actual = self.entrada[self.puntero]

        resultado = self.automatas.aut_numero.analizar(cadena)

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return None

    def analizar_cadena(self):
    
        columna = self.columna
        puntero_inicial = self.puntero
     
        cadena = ''

        while self.puntero < len(self.entrada):
            caracter_actual = self.entrada[self.puntero]
            cadena += caracter_actual

            resultado = self.automatas.aut_cadena.analizar(cadena)

            self.columna += 1
            self.puntero += 1

            if resultado is not None:
                caracter_actual = self.entrada[self.puntero]
                # if caracter_actual in self.alfanumericos:
                #     resultado = None
                break

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return resultado

    def analizar_identificador(self):
        columna = self.columna
        puntero_inicial = self.puntero
        caracter_actual = self.entrada[self.puntero]
        cadena = ''

        while caracter_actual in self.alfanumericos:
            cadena += caracter_actual
            self.columna += 1
            self.puntero += 1
            caracter_actual = self.entrada[self.puntero]

        resultado = self.automatas.aut_identificador.analizar(cadena)

        if resultado is not None:
            return [cadena, resultado]

        self.columna = columna
        self.puntero = puntero_inicial
        return None    