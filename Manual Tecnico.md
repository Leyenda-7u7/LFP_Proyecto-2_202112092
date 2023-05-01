
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
|Visual Studio Code            |Se recomienda el uso de Visual Studio Code que fue la versión donde se programó el sistema de información. |       
|Tkinter         |Conocimiento sobre el uso de las librerias tkinter para el uso de la interfaz grafica |            |            |


##	Desarrollo

[![Crono.jpg](https://i.postimg.cc/0jqCq0fW/Crono.jpg)](https://postimg.cc/0McSYmhD)

 



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

*Palabras Reservadas:*

*CrearBD*

*EliminarBD*

*CrearColeccion*

*EliminarColeccion*

*InsertarUnico*

*ActualizarUnico*

*BuscarTodo*

*BuscarUnico*

*(*

*)*

*;*

*=**

*ID -> [a-z_A-Z_] [a-z_A-Z_0-9]**

*NUMERO -> [0-9]+*

*STRING -> "[^"]"**

*IGNORE  -> /t/r*

*COMENTARIOS -> //.**

*init: 		instrucciones* 

*instrucciones: instruccion	 instrucciones
										instruccion*

instrucion: 
*CrearBD*;

*EliminarBD*;

*CrearColeccion*;

*EliminarColeccion*;

*InsertarUnico*;

*ActualizarUnico*;

*BuscarTodo*;

*BuscarUnico*;

*crearBD : CrearBD ID = nueva CrearBD ()*

*elimnarBD : EliminarBD ID = nueva EliminarBD ()*

*crearColeccion : CrearColeccion  ID = nueva CrearColeccion( STRING )*

*eliminarColeccion : EliminarColeccion  ID  = nueva EliminarColeccion( STRING )*

*insertarUnico : InsertarUnico ID = nueva InsertarUnico( STRING; STRING )*

*actualizarUnico : ActualizarUnico ID = nueva ActualizarUnico( STRING, STRING )*

*eliminarUnico : EliminarUnico ID = nueva EliminarUnico( STRING )*

*buscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING )*

*buscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING )*

 # Interfaz
Para realizar la interfaz fue necesario la implementacion de la libreria tkinter la cual nos ayudo a crear una interfaz mas agradable al usuario, donde de la misma manera se uso para llenar de funciones las cuales ayudaron a generar respuestas de toda la parte logica del proyecto y generar muchas mas aplicaciones. 

La interfaz programada se presenta en la siguiente imagen, donde se encuentran tres botones los cuales uno es de analizar, Tokens y Errores, eso fue para implementar funciones a cada boton las cuales fueron las siguientes:

Para el boton analizar:

[![3004.png](https://i.postimg.cc/brT1fcdr/3004.png)](https://postimg.cc/30kk2qXQ)


Para el boton Tokens:

[![3004-1.png](https://i.postimg.cc/3J8gCRbv/3004-1.png)](https://postimg.cc/RqY6vMmS)

Para le boton Errores:
[![3004-1.png](https://i.postimg.cc/3J8gCRbv/3004-1.png)](https://postimg.cc/RqY6vMmS)



La interfaz quedaria de la siguiente manera donde podemos ver mas opciones en la parte de arriba.

[![Captura-de-pantalla-2023-04-30-195736.png](https://i.postimg.cc/6q9G0jzX/Captura-de-pantalla-2023-04-30-195736.png)](https://postimg.cc/ygbd6TwQ)

En la parte superior se encuentra mas opciones las cuales utlizaremos como lo serian abrir los documentos, entre otros.
[![Captura-de-pantalla-2023-04-30-203324.png](https://i.postimg.cc/0jY18Zqb/Captura-de-pantalla-2023-04-30-203324.png)](https://postimg.cc/bSwBgxrh)

[![Captura-de-pantalla-2023-04-30-203402.png](https://i.postimg.cc/654GhvfT/Captura-de-pantalla-2023-04-30-203402.png)](https://postimg.cc/QHst8VPr)
And this will produce a flow chart:

## Arbol generador 

La siguiente imagen represtan lo que seria el arbol generador para el codigo implementado en este proyecto. Donde cada funcion cumple condiciones y hace un recorrido llamado Post Orden 


[![Captura-de-pantalla-2023-04-30-210331.png](https://i.postimg.cc/hjCCW5vS/Captura-de-pantalla-2023-04-30-210331.png)

Un automata aproximado de la lectura seria le siguiente:

[![Captura-de-pantalla-2023-04-30-220311.png](https://i.postimg.cc/xCJW5m9j/Captura-de-pantalla-2023-04-30-220311.png)](https://postimg.cc/WFVWbhDx)
