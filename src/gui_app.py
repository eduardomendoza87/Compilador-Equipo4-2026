"""
src/gui_app.py
---------------------------------------------------
Interfaz Gráfica de Usuario (GUI) basada en Tkinter.
Actúa como el 'Frontend' que conecta al usuario con el Analizador Léxico.

AUTOR: Equipo 7 - Compiladores 2026
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from lexer import AnalizadorLexico  # Importamos tu motor lógico

class CompiladorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador - Lenguajes y Autómatas II")
        self.root.geometry("1000x700")
        
        # Instancia del motor léxico
        self.lexer = AnalizadorLexico()
        
        # --- ESTILOS ---
        style = ttk.Style()
        style.theme_use('clam')  # Un tema un poco más moderno que el default
        style.configure("Treeview", font=('Consolas', 10), rowheight=25)
        style.configure("Treeview.Heading", font=('Arial', 11, 'bold'))

        # --- LAYOUT PRINCIPAL (Paneles divididos) ---
        # Usamos PanedWindow para que el usuario pueda redimensionar las áreas
        self.paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # PANEL IZQUIERDO: Editor de Código
        self.frame_editor = ttk.Labelframe(self.paned_window, text="Código Fuente")
        self.paned_window.add(self.frame_editor, weight=1)

        # Editor de texto con scroll
        self.text_area = scrolledtext.ScrolledText(self.frame_editor, wrap=tk.WORD, font=('Consolas', 12))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # PANEL DERECHO: Salidas (Pestañas)
        self.frame_resultados = ttk.Frame(self.paned_window)
        self.paned_window.add(self.frame_resultados, weight=1)

        # Crear el sistema de pestañas
        self.notebook = ttk.Notebook(self.frame_resultados)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña 1: Tabla de Tokens
        self.tab_tokens = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_tokens, text="Tabla de Tokens")
        self.tree_tokens = self._crear_tabla(self.tab_tokens, ["Línea", "Tipo", "Valor"])

        # Pestaña 2: Tabla de Símbolos (Variables únicas)
        self.tab_simbolos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_simbolos, text="Tabla de Símbolos")
        self.tree_simbolos = self._crear_tabla(self.tab_simbolos, ["Nombre", "Tipo", "Primera Aparición"])

        # Pestaña 3: Errores
        self.tab_errores = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_errores, text="Consola de Errores")
        self.console_errores = scrolledtext.ScrolledText(self.tab_errores, state='disabled', fg='red', font=('Consolas', 10))
        self.console_errores.pack(fill=tk.BOTH, expand=True)

        # --- BARRA DE BOTONES (Parte inferior) ---
        self.frame_botones = ttk.Frame(root)
        self.frame_botones.pack(fill=tk.X, padx=10, pady=10)

        btn_analizar = ttk.Button(self.frame_botones, text="▶ ANALIZAR", command=self.ejecutar_analisis)
        btn_analizar.pack(side=tk.LEFT, padx=5)

        btn_limpiar = ttk.Button(self.frame_botones, text="LIMPIAR", command=self.limpiar_todo)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        btn_cargar = ttk.Button(self.frame_botones, text="CARGAR ARCHIVO", command=self.cargar_archivo)
        btn_cargar.pack(side=tk.RIGHT, padx=5)

    def _crear_tabla(self, parent, columnas):
        """Método auxiliar para configurar tablas (Treeview) idénticas"""
        tree = ttk.Treeview(parent, columns=columnas, show='headings')
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side='right', fill='y')
        tree.pack(side='left', fill='both', expand=True)
        return tree

    def ejecutar_analisis(self):
        """Conecta el texto del editor con el Motor Léxico"""
        codigo = self.text_area.get("1.0", tk.END)
        
        # 1. Limpiar tablas anteriores
        self._limpiar_resultados()
        
        # Variables para lógica de Tabla de Símbolos
        simbolos_encontrados = set()
        
        # 2. Ejecutar el Lexer
        # Convertimos el generador a lista para poder contar errores
        tokens = list(self.lexer.analizar(codigo))
        errores = []

        for token in tokens:
            if token['tipo'] == 'ERROR_LEXICO':
                errores.append(f"Error en Línea {token['linea']}, Col {token['columna']}: {token['valor']}")
                continue # No lo agregamos a la tabla de tokens válidos
            
            # Agregar a Tabla de Tokens
            self.tree_tokens.insert("", tk.END, values=(token['linea'], token['tipo'], token['valor']))

            # Lógica para Tabla de Símbolos (Solo Identificadores únicos)
            if token['tipo'] == 'ID':
                if token['valor'] not in simbolos_encontrados:
                    simbolos_encontrados.add(token['valor'])
                    # Por ahora el "Tipo" es desconocido hasta el análisis semántico
                    self.tree_simbolos.insert("", tk.END, values=(token['valor'], "Identificador", f"Línea {token['linea']}"))

        # 3. Mostrar Errores
        self.console_errores.config(state='normal')
        if errores:
            for err in errores:
                self.console_errores.insert(tk.END, err + "\n")
            messagebox.showwarning("Análisis Completado", f"Se encontraron {len(errores)} errores léxicos.")
        else:
            self.console_errores.insert(tk.END, "Análisis completado sin errores léxicos.\n")
        self.console_errores.config(state='disabled')

    def limpiar_todo(self):
        self.text_area.delete("1.0", tk.END)
        self._limpiar_resultados()

    def _limpiar_resultados(self):
        for item in self.tree_tokens.get_children():
            self.tree_tokens.delete(item)
        for item in self.tree_simbolos.get_children():
            self.tree_simbolos.delete(item)
        self.console_errores.config(state='normal')
        self.console_errores.delete("1.0", tk.END)
        self.console_errores.config(state='disabled')

    def cargar_archivo(self):
        filepath = filedialog.askopenfilename(filetypes=[("Archivos de Texto", "*.txt"), ("Todos", "*.*")])
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as f:
                contenido = f.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", contenido)

# Función puente para main.py
def iniciar_app():
    root = tk.Tk()
    app = CompiladorGUI(root)
    root.mainloop()