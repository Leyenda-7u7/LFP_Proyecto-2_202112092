
UNIVESIDAD DE SAN CARLOS DE GUATEMALA
FACULTAD DE INGENIERIA
ESCUELA DE CIENCAS Y SISTEMAS
LANGUAJES FORMALES Y DE PROGRAMACION
SECCIÓN B+
PRIMER SEMESTRE 2023
AUX. DIEGO ANDRES OBIN ROSALES



<p align="center"> MANUAL TECNICO</p>



BRANDON EDUARDO PABLO GARCIA
202112092
Guatemala, febrero del 2023




# Introduccion

Este manual describe los pasos necesarios para cualquier persona que tenga ciertas bases de sistemas pueda realizar el código implementado en Python donde se creo una herramienta que permita el diseño y creación de sentencias de bases de datos no relacionales de una forma sencilla.  Esta aplicación tendrá un área de edición de código y un área de visualización de la sentencia final generada. 

 Cuando ya se cuente con las sentencias creadas inicialmente, se procederá a realizar la compilación respectiva lo que generar las sentencias de MongoDB que serán mostradas en el espacio de resultados que posteriormente se podrán aplicar a un entorno adecuado a MongoDb.



# Objetivos

* Brindar la información necesaria para poder  representar la funcionalidad técnica de la estructura, diseño y definición del aplicativo.

* Describir las herramientas utilizadas para el diseño y desarrollo del prototipo


# Requerimientos de funcion


|          Requerimientos      |     Descripcion |                                      
|----------------|-------------------------------|
|`Visual Studio Code`            |Se recomienda el uso de Visual Studio Code que fue la versión donde se programó el sistema de información. |       
|Tkinter         |Conocimiento sobre el uso de las librerias tkinter para el uso de la interfaz grafica |            |            |


## Switch to another file

![Crono](Este equipo/Descarga/.jpg)
![enter image description here](https://drive.google.com/file/d/1jZ_0uc93L8XWRb7BdmBpir1fyeFAqeBn/view?usp=sharing)

 

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

#	Contenido tecnico

El código presenta la definición de una clase en Python llamada `LToken`. La clase tiene cuatro atributos: `nombre`, `lexema`, `fila` y `columna`, todos de tipo `str` o `int`. El método constructor `__init__` toma como argumentos cuatro parámetros, `nombre`, `lexema`, `fila` y `columna`, que son asignados a los respectivos atributos de la instancia creada.

El método `__str__` devuelve una representación en forma de cadena de la instancia de la clase, en la que se muestra el valor de cada uno de sus atributos.

La variable `TIPOS_FUNCIONES` es una lista de cadenas que contiene los nombres de varios tipos de funciones.

		
    TIPOS_FUNCIONES  = ["CREAR_BD","ELIMINAR_BD","CREAR_COLECCION","ELIMINAR_COLECCION","INSERTAR_UNICO","ACTUALIZAR_UNICO","ELIMINAR_UNICO","BUSCAR_TODO","BUSCAR_UNICO"]

Para el analixar lexico se implemento la clase que contiene métodos para identificar y generar tokens a partir de una cadena de entrada dada llamada `AnalizadorLexico`. La clase tiene un `analizar`método que toma una cadena de entrada y la analiza carácter por carácter para identificar y generar tokens.

La clase usa una `AutomatasAnalizadorLexico`clase del `auto`módulo para identificar tokens. Los tokens se almacenan en el `tokens`atributo de lista de la clase.

Junto con esto se crearon la clase llamada "Analizador_sintactico" con unas listas las cuales son:

    self.operaciones  = []
    self.tokens  =  tokens
    self.atributo_lista  =[]
    self.identificador=  ""
    self.funcionesL  = []
    self.textoJson  =""


La clase tiene varios métodos, pero el principal es `Analizador_sintactico`. Es método es el encargado de leer una lista de tokens que se le pasan como argumento, y de acuerdo a los comandos definidos en la lista "comandos", ejecuta distintas acciones dependiendo del comando reconocido en el token actual.

Cada comando está definido como un método dentro de la clase cada una con su funcion las cuales son `crear_bd`, `eliminarbd`,`crear_coleccion`, `eliminar_colecion`, `buscar_todo`, `buscar_uno` , `insertar_uno`, `atributos_set`, `json`, `json2`, `json_set`. Estos métodos ejecutan distintas acciones según el comando reconocido.


Esto genera la siguiente gramatica.

Palabras Reservadas:
*CrearBD
EliminarBD
CrearColeccion
EliminarColeccion
InsertarUnico
ActualizarUnico
BuscarTodo
BuscarUnico
(
)
*;*
=*
*ID -> [a-z_A-Z_] [a-z_A-Z_0-9]**
NUMERO -> [0-9]+
STRING -> "[^"]"*
IGNORE  -> /t/r
COMENTARIOS -> //.*

init: 		instrucciones 
instrucciones: instruccion
