import tkinter as tk
import tkinter as t
import tkinter.scrolledtext as s
import tkinter.filedialog as fd
import sys
import os
from tkinter.messagebox import showinfo
import lexico
import lista_tokens
import sintactico as sint
import tabla_funciones as tfunciones
import webbrowser


class Ventana:

    FONDO_VENTANA = '#20147A'
    FONDO_MENU = '#EC7063'

    
    def __init__(self,PP):
        self.PP = PP
        self.PP.title('PANTALLA PRINCIPAL')
        self.PP['bg'] = self.FONDO_VENTANA
        self.PP.resizable(False, False)
        self.ruta_archivo_actual = ''
        self.lista_tokens_actual = []
        self.lista_funciones =None
        self.lista_tokens_usar =None
        
        self.ancho = 1000
        self.alto = 700
        x = (int(self.PP.winfo_screenwidth()) - int(self.ancho))//2
        y = (int(self.PP.winfo_screenheight()) - int(self.alto))//2
        self.PP.geometry(f'{self.ancho}x{self.alto}+{x}+{y}')

    
        self.titulo = t.Label(self.PP, text='[FLP] PROYECTO 2', font=("Arial Black", 18),bg="#20147A", width=20).place(x=380, y=25)
        '''# Área de texto izquierda
        self.texto1 = tk.Text(self.PP, width=55, height=30)
        self.texto1.pack(side=tk.LEFT, padx=35, pady=10)
        
        # Área de texto derecha
        self.texto2 = tk.Text(self.PP, width=55, height=30)
        self.texto2.pack(side=tk.RIGHT, padx=35, pady=10)'''
        
        # Botones inferiores
        self.boton1 = tk.Button(self.PP, text='Analizar', command=self.analizar ,font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=100, y=620)
        self.boton2 = tk.Button(self.PP, text='Tokens', command=self.ver_tokens, font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=500, y=620)
        self.boton3 = tk.Button(self.PP, text='Errores',command=self.llenar_funcion , font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=800, y=620)
    
        
        # Menú superior
        menubar = tk.Menu(self.PP)
        self.PP.config(menu=menubar)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir Archivo", command=self.cargar_archivo)
        filemenu.add_command(label="Guardar", command=self.guardar)
        filemenu.add_command(label="Guardar Como", command=self.guardar_como)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.salir)
        
        menubar.add_cascade(label="Archivo", menu=filemenu)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        self.PP.config(menu=menubar)
        filemenu.add_command(label="Manual de Usuario", command=self.abrir_manual_usuario)
        filemenu.add_command(label="Manual de Tecnico", command=self.abrir_manual_tecnico)
        filemenu.add_separator()
        filemenu.add_command(label="Ayuda", command=self.ayuda)

        menubar.add_cascade(label="Ayuda", menu=filemenu)

        self.area_texto = s.ScrolledText(self.PP)   
        self.area_texto['height'] = 20
        self.area_texto['width'] = 90
        self.area_texto['wrap'] = t.NONE
        self.area_texto.place(x=137, y=125)


    def cargar_archivo(self):
        extensiones = (('Todos los archivos', '*.*'),)

        self.ruta_archivo_actual = str(
            fd.askopenfilename(filetypes=extensiones))

        try:
            with open(self.ruta_archivo_actual, 'r') as archivo:
                texto = archivo.read()
                self.area_texto.delete('1.0', t.END)
                self.area_texto.insert('1.0', texto)
        except IOError:
            print('Error en la carga')

    def analizar(self):

        analizador = lexico.AnalizadorLexico()
        texto = self.area_texto.get('1.0', t.END)
        self.lista_tokens_usar = analizador.analizar(texto)
        self.lista_tokens_actual = self.lista_tokens_usar.copy()
        
        analizador_sint = sint.Analizador_sintactico(self.lista_tokens_actual)
        self.lista_funciones =analizador_sint.ejecutar_analizador()
        
        

            
        
    def ver_funciones(self):

        tfunciones.Ventana_Funciones(self.lista_funciones) 
        

    def borrar(self):
        self.area_texto.delete('1.0', t.END)
        
    def llenar_funcion(self):
        for fun in self.lista_funciones:
            print("las funciones son"+ fun)
    
        tfunciones.Ventana_Funciones(self.lista_funciones)
        
        
    def guardar(self):
        if self.ruta_archivo_actual == '':
            self.ruta_archivo_actual = self.guardar_como()
        else:
            texto = self.area_texto.get('1.0', t.END)
            with open(self.ruta_archivo_actual, 'w', encoding='utf-8') as archivo:
                archivo.write(texto)
            showinfo('Guardado', 'Archivo guardado exitosamente')

    def guardar_como(self):
        extensiones = (('Todos los archivos', '*.*'),)

        ruta_archivo = str(
            fd.asksaveasfilename(filetypes=extensiones))

        texto = self.area_texto.get('1.0', t.END)
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(texto)

        return ruta_archivo

    def salir(self):
        sys.exit(0)


    def ver_tokens(self):
        ventana = lista_tokens.Ventana_Token(self.lista_tokens_actual)

    def abrir_manual_usuario(self):
        try:  
            path = 'https://github.com/Leyenda-7u7/LFP_Proyecto-2_202112092/blob/main/Manual%20de%20Usuario.md'
            webbrowser.open_new(path)
        except:
            print("No se pudo abrir el archivo")
            
            
    def abrir_manual_tecnico(self):
        try:  
            path = 'https://github.com/Leyenda-7u7/LFP_Proyecto-2_202112092/blob/main/Manual%20Tecnico.md'
            webbrowser.open_new(path)
        except:
            print("No se pudo abrir el archivo")
    def ayuda(self):
        os.startfile( "informacion.pdf" )

if __name__ == '__main__':
    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()