
import drop
import funciones


class Analizador_sintactico: 
    
    def __init__(self,tokens):
        self.operaciones = []
        self.tokens = tokens
        self.atributo_lista =[]
        self.identificador= ""
        self.funcionesL = []
        self.textoJson =""
    
    def obtener_token(self):
        return self.tokens[0]

    def sacar_token(self):
        print("sacando este token:"+ self.tokens[0].lexema)
        return self.tokens.pop(0)

    def ejecutar_analizador(self):
        
        for f in self.tokens:
            print("son los tokens leidos" + f.nombre)
            
        
        
        
        comandos = ["CREAR_BD","ELIMINAR_BD","CREAR_COLECCION","ELIMINAR_COLECCION","INSERTAR_UNICO","TK_ACTUALIZAR_UNICO","TK_ELIMINAR_UNICO","TK_BUSCAR_TODO","TK_BUSCAR_UNICO"]


        tokenA = self.obtener_token()
        
        
            
            
        
        if tokenA.nombre in comandos:
            
            if tokenA.nombre == "CREAR_BD":
                
                self.crear_bd()
                
            elif tokenA.nombre == "ELIMINAR_BD":

                self.eliminarbd()
                
                
            elif tokenA.nombre== "CREAR_COLECCION":
                self.crear_coleccion()
                
            elif tokenA.nombre == "ELIMINAR_COLECCION":        
                self.eliminar_coleccion()
                
            elif tokenA.nombre== "INSERTAR_UNICO":
                self.insertar_uno()
                
                
            elif tokenA.nombre== "TK_ACTUALIZAR_UNICO":
                
                self.actualizar_unico()
                
            elif tokenA.nombre == "TK_ELIMINAR_UNICO":    
                
                self.eliminar_unico()
                
            elif tokenA.nombre == "TK_BUSCAR_TODO":
                
                self.buscar_todo()
                
            elif tokenA.nombre == "TK_BUSCAR_UNICO":     

                self.buscar_uno()
                

            ## despues, se verifica si se puede reconocer otro comando
            if len(self.tokens) > 0:
                tokenA = self.obtener_token()

                if tokenA.nombre in comandos:
                    self.ejecutar_analizador()
                else:
                    print('No hay mas comandos')
                    

        return self.funcionesL    
    
    
    
    def crear_bd(self):
        tokenA = self.obtener_token()

        if tokenA.nombre == "CREAR_BD":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
                self.identificador = tokenA.lexema
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "CREAR_BD":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                
                                if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                    self.sacar_token()
                                    tokenA=self.obtener_token()
                                    if tokenA.nombre == "TOKEN_PUNTOCOMA":

                                        f_use= funciones.Use(self.identificador)
                                        use1=f_use.crear_use()
                                        self.funcionesL.append(use1)
                                        self.identificador= ""
                                        self.sacar_token()
                                        print(use1)
                                            
                                            
                                            
                                            
    def eliminarbd(self):
        
        tokenA = self.obtener_token()
        

        if tokenA.nombre == "ELIMINAR_BD":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "ELIMINAR_BD":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":

                                self.sacar_token()
                                tokenA=self.obtener_token()

                                if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                    self.sacar_token()
                                    tokenA=self.obtener_token()

                                    if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                        self.sacar_token()
                                        f_drop= drop.DropData()
                                        drop1=f_drop.crear_dropData()
                                        self.funcionesL.append(drop1)
                                        self.identificador= ""
                                        print(drop1)

    def crear_coleccion(self):
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "CREAR_COLECCION":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "CREAR_COLECCION":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacar_token()

                                            f_coleccion= funciones.Create_collection(self.identificador)
                                            col1=f_coleccion.crear_coleccion()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""

                                    
    def eliminar_coleccion(self):
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "ELIMINAR_COLECCION":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "ELIMINAR_COLECCION":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacar_token()

                                            f_coleccion= funciones.DropCollection(self.identificador)
                                            col1=f_coleccion.crear_dropCo()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                    #print(col1)                                            

    def buscar_todo(self):
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "TK_BUSCAR_TODO":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "TK_BUSCAR_TODO":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacar_token()

                                            f_coleccion= funciones.Find(self.identificador)
                                            col1=f_coleccion.crear_find()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                            #print(col1)                                            


    def buscar_uno(self):
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "TK_BUSCAR_UNICO":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "TK_BUSCAR_UNICO":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()
                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()
                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                            self.sacar_token()

                                            f_coleccion= funciones.Find_one(self.identificador)
                                            col1=f_coleccion.crear_findOne()
                                            self.funcionesL.append(col1)
                                            self.identificador= ""
                                            #print(col1)                                            

#revisar el json 
    def insertar_uno(self):
        string_json=""
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "INSERTAR_UNICO":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "INSERTAR_UNICO":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacar_token()
                                            tokenA=self.obtener_token()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json()

                                                tokenA = self.obtener_token()
                                                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    string_json += "\n}"
                                                    self.sacar_token()

                                                    tokenA = self.obtener_token()
                                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                        self.sacar_token()
                                                        tokenA=self.obtener_token()
                                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                            self.sacar_token()
                                                            f_coleccion= funciones.InsertOne(self.identificador,string_json)
                                                            col1=f_coleccion.crear_insert()
                                                            self.funcionesL.append(col1)
                                                            self.identificador= ""
                                                            #print(string_
                                                                                                                                                        
    def actualizar_unico(self):
        string_json=""
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "TK_ACTUALIZAR_UNICO":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "TK_ACTUALIZAR_UNICO":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacar_token()
                                            tokenA=self.obtener_token()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json2()

                                                tokenA = self.obtener_token()
                                                if tokenA.nombre == "TOKEN_COMA":
                                                    # viene un json con set
                                                    self.sacar_token()
                                                    string_json += " ,\n" + self.json_set()
                                                    tokenA = self.obtener_token()
                                                    if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                        self.sacar_token()
                                                        string_json += "    \n}"
                                                elif tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    self.sacar_token()
                                                    string_json += "\n}"

                                                print(string_json)
                                                tokenA = self.obtener_token()
                                                if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                    self.sacar_token()
                                                    tokenA=self.obtener_token()
                                                    if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                        self.sacar_token()
                                                        f_coleccion= funciones.ActualizaOne(self.identificador,string_json)
                                                        col1=f_coleccion.crear_actu1()
                                                        self.funcionesL.append(col1)
                                                        self.identificador= ""
                                        
    
#     
    def atributos_set(self):
        clave = ""
        lexema = ""
        texto = ""

        tokenA = self.obtener_token()
        if tokenA.nombre == "TK_SET":
            clave = tokenA.lexema
            self.sacar_token()

            tokenA = self.obtener_token()
            if tokenA.nombre == "TOKEN_DOSPUNTOS":
                self.sacar_token()

                tokenA = self.obtener_token()

                if tokenA.nombre == "TOKEN_LLAVEABRE":
                    lexema = self.json2()
                    tokenA = self.obtener_token()
                    texto = clave + ":" + lexema
                    if tokenA.nombre == "TOKEN_LLAVECIERRA":
                        return texto
            
            

    def json(self):
        texto = ""
        self.sacar_token()
        texto += "  {\n"

        tokenA = self.obtener_token()
        if tokenA.nombre == "TK_CADENA":
            texto += self.atributos()

            tokenA = self.obtener_token()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacar_token()

                texto += "  \n}"

                tokenA = self.obtener_token()
                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                    return texto

    def json2(self):
        texto = ""
        self.sacar_token()
        texto += "  {\n"

        tokenA = self.obtener_token()
        if tokenA.nombre == "TK_CADENA":
            texto += self.atributos()

            tokenA = self.obtener_token()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacar_token()

                texto += "  \n}"
                return texto 

    def json_set(self):
        texto = ""
        self.sacar_token()
        texto += "  {\n"

        tokenA = self.obtener_token()
        if tokenA.nombre == "TK_SET":
            texto += self.atributos_set()

            tokenA = self.obtener_token()
            if tokenA.nombre == "TOKEN_LLAVECIERRA":
                self.sacar_token()

                texto += "  \n}"
                return texto                     
                                                                            
    def atributos(self):
        clave = ""
        lexema = ""
        texto = ""

        tokenA = self.obtener_token()
        if tokenA.nombre == "TK_CADENA":
            clave = tokenA.lexema
            self.sacar_token()

            tokenA = self.obtener_token()
            if tokenA.nombre == "TOKEN_DOSPUNTOS":
                self.sacar_token()

                tokenA = self.obtener_token()
                # este if valida el tipo de token que se espera para el lexema
                if tokenA.nombre == "TK_CADENA":
                    lexema = tokenA.lexema
                    self.sacar_token()

                    texto = clave + ":" + lexema
                    tokenA = self.obtener_token()
                    # puede venir coma o llave de cierre
                    if tokenA.nombre == "TOKEN_COMA":
                        self.sacar_token()
                        texto += ",\n"
                        texto += self.atributos()
                        return texto
                    elif tokenA.nombre == "TOKEN_LLAVECIERRA":
                        return texto

                                
                                                                            
    def eliminar_unico(self):  
        string_json=""
        tokenA = self.obtener_token()
        ##llave apertur inicial
        if tokenA.nombre == "TK_ELIMINAR_UNICO":

            self.sacar_token()
            tokenA=self.obtener_token()

            if tokenA.nombre == "IDENTIFICADOR":
            
                self.sacar_token()
                tokenA=self.obtener_token()
                if tokenA.nombre == "TOKEN_IGUAL":
                    self.sacar_token()
                    tokenA=self.obtener_token()
                    if tokenA.nombre == "TK_NUEVA":
                        self.sacar_token()
                        tokenA=self.obtener_token()
                        if tokenA.nombre == "TK_ELIMINAR_UNICO":
                            self.sacar_token()

                            tokenA=self.obtener_token()
                            if tokenA.nombre == "TOKEN_PARENTESISABRE":
                                self.sacar_token()
                                tokenA=self.obtener_token()
                                if tokenA.nombre == "TK_CADENA":
                                    self.identificador = tokenA.lexema

                                    self.sacar_token()
                                    tokenA=self.obtener_token()


                                    if tokenA.nombre == "TOKEN_COMA":
                                        self.sacar_token()
                                        tokenA=self.obtener_token()

                                        if tokenA.nombre == "TOKEN_LLAVEABRE":
                                            self.sacar_token()
                                            tokenA=self.obtener_token()
                                            string_json += "{\n"


                                            if tokenA.nombre == "TOKEN_LLAVEABRE":
                                                string_json += self.json()

                                                tokenA = self.obtener_token()
                                                if tokenA.nombre == "TOKEN_LLAVECIERRA":
                                                    string_json += "\n}"
                                                    self.sacar_token()

                                                    tokenA = self.obtener_token()
                                                    if tokenA.nombre == "TOKEN_PARENTESISCIERRA":
                                                        self.sacar_token()
                                                        tokenA=self.obtener_token()
                                                        if tokenA.nombre == "TOKEN_PUNTOCOMA":
                                                            self.sacar_token()
                                                        
                                                        
                                                            f_coleccion= funciones.DeleteOne(self.identificador,string_json)
                                                            col1=f_coleccion.crear_delete_one()
                                                            self.funcionesL.append(col1)
                                                            self.identificador= ""  





