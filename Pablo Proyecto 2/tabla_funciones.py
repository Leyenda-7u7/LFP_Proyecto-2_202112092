import tkinter as t
import tkinter.ttk as ttk
import tkinter as tk

class Ventana_Funciones:

    FONDO_VENTANA = '#20147A'
    FONDO_MENU = '#EC7063'
    FONDO_TABLA = '#FFFFFF'
    ANCHO = '1000'
    FUENTE = 'Arial'
    ALTO = '700'
    COLOR_FUENTE = 'black'

    def __init__(self, lista_funciones):
        self.marco = t.Tk()
        self.marco.title('VENTANA TOKENS')
        self.marco['bg'] = self.FONDO_VENTANA
        self.marco.resizable(False, False)
        self.ruta_archivo_actual = ''

        self.ancho = 1000
        self.alto = 700
        x = (int(self.marco.winfo_screenwidth()) - int(self.ancho))//2
        y = (int(self.marco.winfo_screenheight()) - int(self.alto))//2
        self.marco.geometry(f'{self.ancho}x{self.alto}+{x}+{y}')

        self.titulo = t.Label(self.marco, text='ERRORES (TOKENS)', font=("Arial Black", 18),bg="#20147A", width=20).place(x=254, y=50)

        # definir columnas
        encabezados = ('No.','Lexema')
        self.tabla = ttk.Treeview(self.marco, columns=encabezados,show='headings', height=20)

        # definir encabezados
        self.tabla.heading('No.', text='No.')
        self.tabla.column('No.', anchor=t.CENTER, width=100)
        
        self.tabla.heading('Lexema', text='funciones')
        self.tabla.column('Lexema', anchor=t.CENTER, width=300)

        # estilo de tabla
        estilo = ttk.Style(self.tabla)
        estilo.theme_use('clam')
        estilo.configure(
            'Treeview.Heading',
            background=self.FONDO_TABLA,
            foreground=self.COLOR_FUENTE,
            font=(self.FUENTE, 12, 'bold'))
        estilo.configure('Treeview', font=(self.FUENTE, 10),
                        background=self.FONDO_TABLA)

        # Añadir datos a la tabla
        contador = 1
        for funcion in lista_funciones:
            datos = [str(contador),funcion]
            self.tabla.insert('', t.END, values=datos)
            contador += 1

        self.tabla.place(x=99, y=150)

        self.boton = tk.Button(self.marco, text='Volver', command=self.volver, font=("Arial Black", 15), fg="black", bg="#8373FB", width=10).place(x=450, y=620)

        self.marco.mainloop()

    def volver(self):
        self.marco.destroy()