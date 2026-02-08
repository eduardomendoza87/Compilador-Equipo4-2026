 # 🦁 Compilador Equipo 4

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GUI](https://img.shields.io/badge/Interface-Tkinter-green)
![Status](https://img.shields.io/badge/Fase-Análisis_Léxico-orange)
![Curso](https://img.shields.io/badge/Materia-Lenguajes_y_Autómatas_II-red)

> Proyecto semestral para la materia de **Lenguajes y Autómatas II**. Este repositorio aloja el desarrollo incremental de un compilador completo, desde el análisis léxico hasta la generación de código objeto.

---

## 📋 Descripción del Proyecto

Este software es una herramienta diseñada para analizar código fuente escrito en un lenguaje personalizado. Actualmente, el sistema se encuentra en la **Fase 1 (Análisis Léxico)**, capaz de identificar tokens, reportar errores y gestionar una tabla de símbolos básica mediante una interfaz gráfica intuitiva.

El núcleo del analizador está construido en **Python** utilizando expresiones regulares optimizadas (`re`) y sigue una arquitectura modular para facilitar la escalabilidad hacia las fases sintáctica y semántica.

## 🚀 Funcionalidades Actuales (Fase Léxica)

### 1. Análisis de Tokens
El sistema reconoce y categoriza los siguientes elementos del lenguaje:
- **Palabras Reservadas:** `mientras`, `si`, `sino`, `entero`, `flotante`, `principal`, etc.
- **Identificadores:** Variables y nombres de funciones (ej. `contador`, `calcularSuma`).
- **Operadores:** Aritméticos (`+`, `-`, `*`, `/`), Relacionales (`<`, `>=`, `==`) y Lógicos (`&&`, `||`).
- **Constantes:** Números enteros y flotantes.
- **Comentarios:** Líneas ignoradas que inician con `//`.
- **Delimitadores:** `(`, `)`, `{`, `}`, `;`.

### 2. Interfaz Gráfica (GUI)
- **Editor de Código:** Área de texto con numeración de líneas.
- **Tabla de Tokens:** Visualización en tiempo real de `Línea | Tipo | Valor`.
- **Tabla de Símbolos:** Extracción automática de identificadores únicos.
- **Consola de Errores:** Reporte detallado de errores léxicos (caracteres inválidos) indicando fila y columna.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librería Gráfica:** Tkinter (Nativo)
* **Patrón de Diseño:** MVC Simplificado (Separación entre Lógica `lexer.py` e Interfaz `gui_app.py`).
* **Control de Versiones:** Git & GitHub.

---

## 📂 Estructura del Proyecto

La arquitectura de directorios está diseñada para mantener el orden y la escalabilidad:

```text
Compiler_Eq7_S26/
├── src/                  # Código Fuente
│   ├── main.py           # Punto de entrada de la aplicación
│   ├── lexer.py          # Motor lógico del analizador léxico
│   ├── tokens.py         # Definición de Expresiones Regulares (Reglas)
│   └── gui_app.py        # Interfaz Gráfica (Tkinter)
│
├── tests/                # Archivos de prueba
│   ├── test_basico.txt   # Prueba de funcionalidad estándar
│   └── test_error.txt    # Prueba de manejo de errores
│
├── docs/                 # Documentación del proyecto
│   └── automata.png      # Diagramas y recursos visuales
│
└── README.md             # Información del proyecto

🔧 Instalación y Ejecución
Sigue estos pasos para probar el compilador en tu entorno local:

Clonar el repositorio:

Bash
git clone [https://github.com/](https://github.com/)[TU_USUARIO]/Compilador-Equipo7-2026.git
cd Compilador-Equipo7-2026
Ejecutar la aplicación: Asegúrate de tener Python instalado. Desde la raíz del proyecto ejecuta:

Bash
python src/main.py
Uso:

Escribe código en el editor o carga un archivo .txt desde el botón "CARGAR ARCHIVO".

Presiona "▶ ANALIZAR" para ver los resultados.