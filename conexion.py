import mysql.connector
from mysql.connector import Error


class BASE():

    def __init__(self):
        #try es el bloque con las sentencias que quieres ejecutar. 
        #Sin embargo, podrían llegar a haber errores de ejecución  y el bloque se dejará de ejecutarse.
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='universidad2'
            )
        #except se ejecutará cuando el bloque try falle debido a un error. 
        #Este bloque contiene sentencias que generalmente nos dan un contexto de lo que salió mal en el bloque try.
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC") #se enlistan los cursos ordenandolos de forma accendentes 
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', {2})" #insentar una materia nueva
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'" #selecionar una materia y modificarla
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'" #elegimos un codigo y lo eliminamos 
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
