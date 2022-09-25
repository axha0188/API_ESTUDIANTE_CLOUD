from fastapi import APIRouter
from typing import Union, List
from starlette.status import HTTP_200_OK
from schemas.estudiante_schema import EstudianteSchema
from controllers.estudiante_controllers import EstudianteControllers

estudiante = APIRouter()


@estudiante.get(
    "/api/estudiante",
    tags=["Estudiantes"],
    response_model=List[EstudianteSchema],
    description="lista todos los estudiantes",
)
def listar_todos():
    return EstudianteControllers().listarTodosAsync()


@estudiante.post(
    "/api/estudiante",
    tags=["Estudiantes"],
    status_code=HTTP_200_OK,
    description="graba un estudiante",
)
def grabar_registro(registro: EstudianteSchema):
    EstudianteControllers().grabarRegistroAsync(registro)
    return HTTP_200_OK


@estudiante.get(
    "/api/estudiante/{cedula}/{apellido}",
    tags=["Estudiantes"],
    response_model=Union[List[EstudianteSchema], dict],
    description="obtener estudiante por cedula o apellido",
)
def obtener_registro(cedula: str, apellido: str):
    return EstudianteControllers().obtenerRegistroAsync(cedula, apellido)


@estudiante.put(
    "/api/estudiante",
    tags=["Estudiantes"],
    status_code=HTTP_200_OK,
    description="actualizar estudiante por id",
)
def actualizar_estudiante(registro: EstudianteSchema):
    EstudianteControllers().actualizarRegistroAsync(registro)
    return HTTP_200_OK


@estudiante.delete(
    "/api/estudiante/{id}",
    tags=["Estudiantes"],
    status_code=HTTP_200_OK,
    description="eliminar estudiante por id"
)
def eliminar_estudiante(id: int):
    EstudianteControllers().eliminarRegistroAsync(id)
    return HTTP_200_OK
