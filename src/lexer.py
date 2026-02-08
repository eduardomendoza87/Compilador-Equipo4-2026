import re
from tokens import TOKEN_REGEX

class AnalizadorLexico:
    def __init__(self):
        # Compilamos la "Super Regex" al iniciar para no perder tiempo después.
        # Unimos todos los patrones con un OR (|) y usamos grupos nombrados (?P<nombre>...)
        # Esto crea algo como: (?P<MIENTRAS>mientras)|(?P<ENTERO>\d+)|...
        self.regex_combinado = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_REGEX))

    def analizar(self, codigo_fuente):
        """
        Recibe el código fuente (string) y genera una secuencia de tokens.
        Usa 'yield' para ser eficiente con la memoria (Generador).
        """
        linea_actual = 1
        posicion_inicio_linea = 0

        # re.finditer es ideal porque encuentra todas las coincidencias sin bloquear la memoria
        for match in self.regex_combinado.finditer(codigo_fuente):
            tipo = match.lastgroup  # El nombre del token (ej. PR_MIENTRAS)
            valor = match.group()   # El texto encontrado (ej. "mientras")
            
            # --- Manejo de Casos Especiales ---

            if tipo == 'SALTO_LINEA':
                linea_actual += 1
                posicion_inicio_linea = match.end()
                continue # No generamos token, solo contamos línea

            elif tipo == 'ESPACIO':
                continue # Ignoramos los espacios en blanco

            elif tipo == 'COMENTARIO':
                continue # Ignoramos los comentarios (o podrías guardarlos si quisieras)

            elif tipo == 'ERROR':
                # Reportamos el error pero NO detenemos el compilador (Recuperación de errores)
                yield {
                    'tipo': 'ERROR_LEXICO',
                    'valor': f"Carácter inesperado '{valor}'",
                    'linea': linea_actual,
                    'columna': match.start() - posicion_inicio_linea + 1
                }
            
            else:
                # --- ÉXITO: Token Válido Encontrado ---
                yield {
                    'tipo': tipo,
                    'valor': valor,
                    'linea': linea_actual,
                    'columna': match.start() - posicion_inicio_linea + 1
                }

# --- Bloque de prueba unitaria (Solo se ejecuta si corres este archivo directamente) ---
if __name__ == '__main__':
    # Código de prueba rápida
    codigo_test = """
    mientras (x <= 10) {
        entero y = 3.14; // Comentario
        @
    }
    """
    lexer = AnalizadorLexico()
    print(f"{'LÍNEA':<6} | {'TIPO':<15} | {'VALOR'}")
    print("-" * 40)
    for token in lexer.analizar(codigo_test):
        print(f"{token['linea']:<6} | {token['tipo']:<15} | {token['valor']}")