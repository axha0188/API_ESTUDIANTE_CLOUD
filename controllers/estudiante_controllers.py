from services.estudiante_services import EstudianteServices
from schemas.estudiante_schema import EstudianteSchema


class EstudianteControllers:
    def __init__(self) -> None:
        self.__controller = EstudianteServices()

    def listarTodosAsync(self):
        return self.__controller.listarTodos()

    def grabarRegistroAsync(self, registro: EstudianteSchema):
        self.__controller.grabarRegistro(registro)

    def obtenerRegistroAsync(self, cedula: str, apellido: str):
        return self.__controller.obtenerRegistro(cedula, apellido)

    def actualizarRegistroAsync(self, registro: EstudianteSchema):
        self.__controller.actualizarRegistro(registro)

    def eliminarRegistroAsync(self, id: int):
        self.__controller.eliminarRegistro(id)
