from interfaces.estudiante_interface import IEstudiante
from models.estudiante_model import estudiante
from schemas.estudiante_schema import EstudianteSchema
from database.conexion import conn
from sqlalchemy import or_


class EstudianteServices(IEstudiante):
    def listarTodos(self):
        try:
            return conn.execute(estudiante.select()).fetchall()
        except Exception as error:
            return error

    def grabarRegistro(self, registro: EstudianteSchema):
        try:
            datos = {
                "cedula": registro.cedula,
                "nombre": registro.nombre,
                "apellido": registro.apellido,
                "edad": registro.edad,
                "email": registro.email,
                "genero": registro.genero
            }
            conn.execute(estudiante.insert().values(datos))
        except:
            pass

    def obtenerRegistro(self, cedula: str, apellido: str):
        try:
            registro = conn.execute(estudiante.select().where(
                or_(
                    estudiante.c.cedula == cedula,
                    estudiante.c.apellido == apellido
                )
            )).fetchall()
            if len(registro) == 0:
                return {}
            return registro
        except Exception as error:
            return error

    def actualizarRegistro(self, registro: EstudianteSchema):
        try:
            conn.execute(
                estudiante.update().values(
                    cedula=registro.cedula,
                    nombre=registro.nombre,
                    apellido=registro.apellido,
                    edad=registro.edad,
                    email=registro.email,
                    genero=registro.genero
                )
                .where(estudiante.c.id == registro.id)
            )
        except:
            pass

    def eliminarRegistro(self, id: int):
        try:
            conn.execute(estudiante.delete().where(estudiante.c.id == id))
        except:
            pass
