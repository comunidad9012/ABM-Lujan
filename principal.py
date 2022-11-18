from BD.conexion import BASE
import funciones

#este es un menu. de 5 opciones 
def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar cursos")
            print("2.- Registrar curso")
            print("3.- Actualizar curso")
            print("4.- Eliminar curso")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema! ¡Que tenga un buen dia!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    base = BASE()
#te muestra la lista de los cursos o materias registrado
    if opcion == 1:
        try:
            cursos = base.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
#te da la opcion de restrar una materia o curso
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            base.registrarCurso(curso)
        except:
            print("Ocurrió un error...")
#opcion para actualiza o modificar un curso o materia
    elif opcion == 3:
        try:
            cursos = base.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    base.actualizarCurso(curso)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
#opcion para eliminar un curso o materia 
    elif opcion == 4:
        try:
            cursos = base.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    base.eliminarCurso(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal()
