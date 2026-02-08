import sys
import os

# Truco para que Python encuentre la carpeta 'src' correctamente
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui_app import iniciar_app

if __name__ == "__main__":
    iniciar_app()