"""
src/tokens.py
---------------------------------------------------
Definición de patrones (Expresiones Regulares) para los Tokens.
Este módulo contiene la 'Materia Prima' del Analizador Léxico.

AUTOR: Equipo 7 - Compiladores 2026
"""

# Lista de tuplas (NOMBRE_TOKEN, REGEX)
# ¡ADVERTENCIA DE PROFESOR!: El orden de esta lista es CRÍTICO.
# Los patrones más específicos (como '==') deben ir antes que los generales (como '=').
# Las Palabras Reservadas deben ir antes que los Identificadores.

TOKEN_REGEX = [
    # --- 1. Palabras Reservadas (Keywords) ---
    ('COMENTARIO',  r'//.*'),       # Comentarios de una línea (tipo C/Java)

    # Usamos \b para asegurar que "mientras" no haga match con "mientrasTanto"
    ('PR_MIENTRAS', r'\bmientras\b'),
    ('PR_SI',       r'\bsi\b'),
    ('PR_SINO',     r'\bsino\b'),
    ('PR_PARA',     r'\bpara\b'),
    ('PR_ENTERO',   r'\bentero\b'),
    ('PR_FLOTANTE', r'\bflotante\b'),
    ('PR_RETORNO',  r'\bretornar\b'),
    ('PR_VOID',     r'\bvoid\b'),
    ('PR_MAIN',     r'\bprincipal\b'),

    # --- 2. Operadores Complejos (Multicarácter) ---
    ('OP_LOGICO',   r'&&|\|\|'),        # AND, OR
    ('OP_RELACIONAL', r'>=|<=|==|!='),  # Mayor igual, Menor igual, Igualdad, Diferente

    # --- 3. Operadores Simples y Delimitadores ---
    ('ASIGNACION',  r'='),
    ('OP_SUMA',     r'\+'),             # Escapamos + porque es especial en regex
    ('OP_RESTA',    r'-'),
    ('OP_MULT',     r'\*'),
    ('OP_DIV',      r'/'),
    ('OP_REL_SIMPLE', r'<|>'),
    
    ('PARENT_IZQ',  r'\('),
    ('PARENT_DER',  r'\)'),
    ('LLAVE_IZQ',   r'\{'),
    ('LLAVE_DER',   r'\}'),
    ('CORCH_IZQ',   r'\['),
    ('CORCH_DER',   r'\]'),
    ('PUNTO_COMA',  r';'),
    ('COMA',        r','),

    # --- 4. Constantes (Números y Cadenas) ---
    # Flotantes primero (ej: 3.14) para que no detecte el "3" como entero y deje ".14"
    ('CONST_FLOAT', r'\d+\.\d+'),  
    ('CONST_ENTERO', r'\d+'),
    ('CADENA',      r'\".*?\"'),   # Cadenas entre comillas dobles

    # --- 5. Identificadores (Variables y Funciones) ---
    # Debe ir AL FINAL de las palabras clave para no solaparse
    ('ID',          r'[a-zA-Z_][a-zA-Z0-9_]*'),

    # --- 6. Ignorables y Errores ---
    ('COMENTARIO',  r'//.*'),       # Comentarios de una línea (tipo C/Java)
    ('SALTO_LINEA', r'\n'),         # Para contar líneas
    ('ESPACIO',     r'[ \t]+'),     # Espacios y tabuladores (se ignoran)
    ('ERROR',       r'.'),          # CUALQUIER otra cosa es un error
]