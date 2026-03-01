def main():
    # Inicialización de contadores
    total_alumnos = 0
    aceptados = 0
    rechazados = 0

    print("--- SISTEMA DE BECAS (Evaluación de 5 Alumnos) ---")

    # Ciclo principal para evaluar a 5 alumnos
    while total_alumnos < 5:
        print(f"\nEvaluando alumno #{total_alumnos + 1}")
        
        # Bloque de Entrada de Datos (Validación básica de tipos)
        try:
            edad = int(input("Ingrese edad: "))
            ingreso = float(input("Ingrese ingreso mensual familiar: "))
            promedio = float(input("Ingrese promedio (0-100): "))
        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos.")
            continue # Reinicia el ciclo para el mismo alumno si hay error de tipo

        # Lógica de Negocio (Reglas de Asignación)
        # Regla 1: Edad mayor a 18 y menor de 25
        if edad > 18 and edad < 25:
            
            # Regla 2: Ingreso mensual menor de 5000
            if ingreso < 5000:
                
                # Regla 3: Promedio de 90 a 100
                if 90 <= promedio <= 100:
                    print("RESULTADO: Alumno ACEPTADO para la beca.")
                    aceptados += 1
                else:
                    print("RESULTADO: Rechazado. (Promedio insuficiente o inválido)")
                    rechazados += 1
            else:
                print("RESULTADO: Rechazado. (Ingreso familiar superior al límite)")
                rechazados += 1
        else:
            print("RESULTADO: Rechazado. (Edad fuera del rango permitido)")
            rechazados += 1

        # Incremento del contador de alumnos
        total_alumnos += 1

    # Resumen Final
    print("\n--- RESUMEN FINAL ---")
    print(f"Total de alumnos aceptados: {aceptados}")
    print(f"Total de alumnos rechazados: {rechazados}")

if __name__ == "__main__":
    main()